import math

import helper.parsing as parsing

def part1(data):
    pos = sorted(data)[math.floor(len(data) / 2)]
    print(f'Answer for part 1: {sum(abs(pos - x) for x in data)}')

def part2(data):
    pos = int(sum(data) / len(data))
    print(f'Answer for part 2: {min(sum(int(abs(pos - x + i) * (abs(pos - x + i) + 1) / 2) for x in data) for i in range(2))}')


if __name__ == '__main__':
    input_data = parsing.file2data("../day7/input7.txt", lambda x : [int(y) for y in x.split(',')])
    part1(input_data[0])
    part2(input_data[0])