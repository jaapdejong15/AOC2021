import copy
import itertools
from queue import PriorityQueue

from helper import parsing

cost_per_type = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
type_to_x_coord = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
possible_wait_locations = [(1,1), (2,1), (4,1), (6, 1), (8, 1), (10,1), (11,1)]

class Amphipod:
    __slots__ = 'x', 'y', 't', 'moves', 'on_goal'

    def __init__(self, x, y, t, moves, on_goal):
        self.x, self.y = x, y
        self.t = t
        self.moves = moves
        self.on_goal = on_goal

    def __repr__(self):
        return f'Pod(({self.x}, {self.y}), {self.t})'

class Goal:
    __slots__ = 'x', 'y',

    def __init__(self, x, y):
        self.x, self.y = x, y


class State:

    def __init__(self, amphipods, cost, agent_positions):
        self.amphipods = amphipods
        self.cost = cost
        self.heuristic = self.get_heuristic()
        self.agent_positions = agent_positions

    def __lt__(self, other):
        v1 = self.heuristic + self.cost
        v2 = other.heuristic + other.cost
        if v1 == v2:
            return self.heuristic < other.heuristic
        return v1 < v2

    def get_heuristic(self):
        h = 0
        num_on_goal = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        for amphipod in self.amphipods:
            goal_x = goals[amphipod.t][0].x
            if goal_x == amphipod.x:
                # On goal
                num_on_goal[amphipod.t] += 1
            else:
                h += (abs(goal_x - amphipod.x) + amphipod.y) * cost_per_type[amphipod.t]
        for k, v in num_on_goal.items():
            h += cost_per_type[k] * (3 - num_on_goal[k])
        return h

    def expand(self):
        next_states = []
        for i, amphipod in enumerate(self.amphipods):
            if amphipod.moves >= 2:
                continue
            possible_move_locations = []

            destination_room_ready = True
            possible_goal_move = None
            for goal in goals[amphipod.t]:
                if (goal.x, goal.y) in self.agent_positions:
                    if self.agent_positions[(goal.x, goal.y)] != amphipod.t:
                        destination_room_ready = False
                else: possible_goal_move = (goal.x, goal.y)
                if not destination_room_ready: break
            if destination_room_ready:
                possible_move_locations.append(possible_goal_move)

            if amphipod.moves == 0:
                possible_move_locations.extend(possible_wait_locations)

            for possible_move_location in possible_move_locations:
                # Check if path is clear
                # Decrease y until y == 1
                y = amphipod.y
                valid_move = True
                num_steps = 0
                while y > 1:
                    y -= 1
                    num_steps += 1
                    if (amphipod.x, y) in self.agent_positions:
                        valid_move = False
                        break
                if not valid_move: continue

                # Change x until x = destination x
                dx = 1 if possible_move_location[0] > amphipod.x else -1
                x = amphipod.x
                while x != possible_move_location[0]:
                    x += dx
                    num_steps += 1
                    if (x, y) in self.agent_positions:
                        valid_move = False
                        break
                if not valid_move: continue

                # Increase y until y == destination y
                while y < possible_move_location[1]:
                    y += 1
                    num_steps += 1
                    if (x,y) in self.agent_positions: # TODO: Is it necessary to check for agents here?
                        valid_move = False
                        break
                if not valid_move: continue

                new_agent_positions : dict[tuple[int, int], int] = copy.deepcopy(self.agent_positions) # TODO: Deepcopy necessary?
                new_agent_positions[(x,y)] = new_agent_positions.pop((amphipod.x, amphipod.y))
                new_agents = copy.deepcopy(self.amphipods)
                new_agents[i] = Amphipod(x, y, amphipod.t, amphipod.moves + y, y > 1)
                new_state = State(new_agents, self.cost + num_steps * cost_per_type[amphipod.t], new_agent_positions)
                next_states.append(new_state)
        return next_states

def solve(data, part):
    global goals
    amphipods = []
    agent_positions = dict()
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c in ['A', 'B', 'C', 'D']:
                amphipods.append(Amphipod(x, y, c, 1 if c in ['C', 'D'] else 0, False))
                agent_positions[(x,y)] = c

    num_goals = 2 * part
    goals = {'A': [Goal(3, y) for y in range(2, 2 + num_goals)],
             'B': [Goal(5, y) for y in range(2, 2 + num_goals)],
             'C': [Goal(7, y) for y in range(2, 2 + num_goals)],
             'D': [Goal(9, y) for y in range(2, 2 + num_goals)],
             }
    initial_state = State(amphipods, 0, agent_positions)
    state_queue = PriorityQueue()
    state_queue.put(initial_state)
    cost = 0
    while not state_queue.empty():
        current_state = state_queue.get()
        winning_state = True
        for pod in current_state.amphipods:
            if pod.x != type_to_x_coord[pod.t]:
                winning_state = False
                break
        if winning_state:
           cost = current_state.cost
           break
        next_states = current_state.expand()
        for state in next_states:
            state_queue.put(state)
        if state_queue.qsize() % 10000 < 10:
            print(f'PQ length: {state_queue.qsize()}    Current cost+heuristic: {current_state.cost + current_state.heuristic}')

    print(f'Answer for part {part}: {cost}')




grid = []
goals = dict()
if __name__ == '__main__':
    input_data = parsing.file2data("../day23/input23.txt", lambda y : list(y))
    solve(input_data, 1)
