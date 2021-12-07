import helper.parsing as parsing
import re

def part1(data):
    print('Start of part 1')
    def insert_into_points(point):
        if point in points: points[point] += 1
        else: points[point] = 1
    points = dict()
    for x1, y1, x2, y2 in data:
        if x1 == x2 or y1 == y2:
            x_step = 1 if x2 > x1 else -1 if x2 < x1 else 0
            y_step = 1 if y2 > y1 else -1 if y2 < y1 else 0
            insert_into_points((x1,y1))
            while x1 != x2 or y1 != y2:
                x1 += x_step
                y1 += y_step
                insert_into_points((x1,y1))
    print(f'Answer for part 1: {len(list(filter(lambda z: z >= 2, points.values())))}')

def part2(data):
    def insert_into_points(point):
        if point in points: points[point] += 1
        else: points[point] = 1
    points = dict()
    for x1, y1, x2, y2 in data:
        x_step = 1 if x2 > x1 else -1 if x2 < x1 else 0
        y_step = 1 if y2 > y1 else -1 if y2 < y1 else 0
        insert_into_points((x1,y1))
        while x1 != x2 or y1 != y2:
            x1 += x_step
            y1 += y_step
            insert_into_points((x1,y1))
    print(f'Answer for part 2: {len(list(filter(lambda z: z >= 2, points.values())))}')

if __name__ == '__main__':
    input_data = parsing.file2data("../day5/input5.txt", lambda x : tuple(int(i) for i in re.search('(\d+),(\d+) -> (\d+),(\d+)', x).groups()))
    part1(input_data)
    part2(input_data)