from helper import parsing
from queue import PriorityQueue

class Node:
    __slots__ = 'x', 'y', 'heuristic', 'cost'

    def __init__(self, x, y, heuristic, cost):
        self.x = x
        self.y = y
        self.heuristic = heuristic
        self.cost = cost

    def __lt__(self, other):
        return self.heuristic + self.cost < other.heuristic + other.cost

neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def solve(data):
    visited = set()
    dest_x = len(data[0]) - 1
    dest_y = len(data) - 1
    start = Node(0, 0, dest_x + dest_y, 0)
    q = PriorityQueue()
    q.put(start)
    while not q.empty():
        c = q.get()
        if (c.x, c.y) in visited: continue
        for dx, dy in neighbors:
            nx, ny = c.x+dx, c.y+dy
            if 0 <= nx < len(data[0]) and 0 <= ny < len(data) and (nx, ny) not in visited:
                if nx == dest_x and ny == dest_y: return c.cost + data[dest_y][dest_x]
                neighbor_cost = data[ny][nx]
                neighbor = Node(nx, ny, dest_x - nx + dest_y - ny, c.cost + neighbor_cost)
                q.put(neighbor)
        visited.add((c.x, c.y))

if __name__ == '__main__':
    input_data = parsing.file2data("../day15/input15.txt", lambda x : list(int(y) for y in x.strip()))
    print(f'Answer for part 1: {solve(input_data)}')
    input_data = sum((list(map(lambda z : list(map(lambda y : ((y + k - 1) % 9) + 1, z)),[sum((list(map(lambda x : ((x + j - 1) % 9) + 1, row)) for j in range(5)), []) for row in input_data])) for k in range(5)), [])
    print(f'Answer for part 2: {solve(input_data)}')
