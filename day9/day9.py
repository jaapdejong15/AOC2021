import helper.parsing as parsing
import math

neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def part1(data):
    answer = 0
    low_points = []
    for y in range(len(data)):
        for x in range(len(data[y])):
            height = data[y][x]
            lowest_point = True
            for dx, dy in neighbors:
                if 0 <= x + dx < len(data[y]) and 0 <= y + dy < len(data):
                    if data[y+dy][x+dx] <= height:
                        lowest_point = False
                        break
            if lowest_point:
                answer += height + 1
                low_points.append((x, y))
    print(f'Answer for part 1: {answer}')
    return low_points

def part2(data, low_points):
    basin_sizes = []
    for point in low_points:
        basin_size = 0
        unexplored = [point]
        explored = set()
        while len(unexplored) != 0:
            x, y = unexplored.pop(0)
            for dx, dy in neighbors:
                if 0 <= x + dx < len(data[y]) and 0 <= y + dy < len(data):
                    if (x+dx, y+dy) in explored or (x+dx, y+dy) in unexplored: continue
                    if data[y][x] < data[y+dy][x+dx] < 9:
                        unexplored.append((x+dx, y+dy))
            explored.add((x,y))
            basin_size += 1
        basin_sizes.append(basin_size)
    answer = math.prod(sorted(basin_sizes)[-3:])
    print(f'Answer for part 2: {answer}')

if __name__ == '__main__':
    input_data = parsing.file2data("../day9/input9.txt", lambda x : [int(y) for y in x.strip()])
    lp = part1(input_data)
    part2(input_data, lp)