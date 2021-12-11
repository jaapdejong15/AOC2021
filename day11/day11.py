import itertools

from helper import parsing

directions = list(itertools.product([-1,0,1],[-1,0,1]))
directions.remove((0,0))

def part1(data):
    num_flashes = 0
    for i in range(100):
        data = list(map(lambda x : list(map(lambda y : y + 1, x)), data))
        flashed = True
        while flashed:
            flashed = False
            for x, y in itertools.product(range(len(data[0])), range(len(data))):
                if data[y][x] > 9:
                    flashed = True
                    num_flashes += 1
                    data[y][x] = 0
                    for dx, dy in directions:
                        if 0 <= x+dx < len(data[0]) and 0 <= y+dy < len(data) and data[y+dy][x+dx] != 0:
                            data[y+dy][x+dx] += 1
    print(f'Answer for part 1: {num_flashes}')

def part2(data):
    i = 0
    round_flashes = 0
    while round_flashes < len(data) * len(data[0]):
        round_flashes = 0
        data = list(map(lambda x : list(map(lambda y : y + 1, x)), data))
        flashed = True
        while flashed:
            flashed = False
            for x, y in itertools.product(range(len(data[0])), range(len(data))):
                if data[y][x] > 9:
                    flashed = True
                    round_flashes += 1
                    data[y][x] = 0
                    for dx, dy in directions:
                        if 0 <= x+dx < len(data[0]) and 0 <= y+dy < len(data) and data[y+dy][x+dx] != 0:
                            data[y+dy][x+dx] += 1
        i += 1
    print(f'Answer for part 2: {i}')

if __name__ == '__main__':
    input_data = parsing.file2data("../day11/input11.txt", lambda x : list(map(lambda y : int(y), x.strip())))
    part1(input_data)
    part2(input_data)