from copy import copy
from functools import lru_cache

def part1(data):
    pos = copy(data)
    turn = 0
    die_value = 1
    die_throws = 0
    score = [0,0]
    while score[0] < 1000 and score[1] < 1000:
        step = 0
        for i in range(3):
            step += die_value
            die_value = (die_value % 10) + 1
            die_throws += 1
        pos[turn] = (pos[turn] + step - 1) % 10 + 1
        score[turn] += pos[turn]
        turn = (turn + 1) % 2

    print(f'Answer for part 1: {min(score) * die_throws}')

def part2(data):
    @lru_cache(maxsize=None)
    def roll(pos_0, pos_1, turn, score_0, score_1) -> tuple[int, int]:
        if score_0 >= 21: return 1, 0
        elif score_1 >= 21: return 0, 1
        wins = 0, 0
        new_turn = (turn + 1) % 2
        for throw1 in range(1, 4):
            for throw2 in range(1, 4):
                for throw3 in range(1, 4):
                    step = throw1 + throw2 + throw3
                    temp_pos_0, temp_pos_1 = pos_0, pos_1
                    temp_score_0, temp_score_1 = score_0, score_1
                    if turn == 0:
                        temp_pos_0 = (pos_0 + step - 1) % 10 + 1
                        temp_score_0 += temp_pos_0
                    elif turn == 1:
                        temp_pos_1 = (pos_1 + step - 1) % 10 + 1
                        temp_score_1 += temp_pos_1
                    win1, win2 = roll(temp_pos_0, temp_pos_1, new_turn, temp_score_0, temp_score_1)
                    wins = wins[0]+win1, wins[1]+win2
        return wins

    print(f'Answer for part 2: {max(roll(data[0], data[1], 0, 0, 0))}')






if __name__ == '__main__':
    input_data = [8,1]
    part1(input_data)
    part2(input_data)
