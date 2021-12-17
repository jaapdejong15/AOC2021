import math
import re
from helper import parsing

def part1(data):
    lower_x, upper_x, lower_y, upper_y = data
    dy = -lower_y-1
    y = 0
    max_y = 0
    while y >= lower_y:
        y += dy
        dy -= 1
        if y > max_y: max_y = y
        else:
            print(f'Answer for part 1: {max_y}')
            return

def part2(data):
    lower_x, upper_x, lower_y, upper_y = data
    max_y = -lower_y-1
    min_x = math.floor((1 + math.sqrt(1 + 8 * lower_x)) / 2)
    min_y = lower_y

    count = 0
    for o_dx in range(min_x, upper_x+1):
        for o_dy in range(min_y, max_y+1):
            dx, dy = o_dx, o_dy
            x, y = 0, 0
            while y >= lower_y:
                x += dx
                y += dy
                dx += 1 if dx < 0 else -1 if dx > 0 else 0
                dy -= 1
                if lower_x <= x <= upper_x and lower_y <= y <= upper_y:
                    count += 1
                    break
    print(f'Answer for part 2: {count}')

if __name__ == '__main__':
    input_data = parsing.file2data("../day17/input17.txt", lambda y : tuple(int(x) for x in re.findall('target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', y)[0]))[0]
    part1(input_data)
    part2(input_data)