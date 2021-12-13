from helper import parsing

def part1(dots, folds):
    axis, num = folds[0]
    num = int(num)
    if axis == 'x':
        for i in range(len(dots)):
            x, y = dots[i]
            if x > num:
                dots[i] = 2 * num - x, y
    if axis == 'y':
        for i in range(len(dots)):
            x, y = dots[i]
            if y > num:
                dots[i] = x, 2 * num - y
    print(f'Answer for part 1: {len(set(dots))}')

def part2(dots, folds):
    for axis, num in folds:
        num = int(num)
        if axis == 'x':
            for i in range(len(dots)):
                x, y = dots[i]
                if x > num:
                    dots[i] = 2 * num - x, y
        if axis == 'y':
            for i in range(len(dots)):
                x, y = dots[i]
                if y > num:
                    dots[i] = x, 2 * num - y
    max_x = max(dots[:][0])
    max_y = max(dots[:][1])
    data = [[0 for _ in range(max_x + 2)] for _ in range(max_y + 2)]
    for x, y in dots:
        data[y][x] = 1

    print('Answer for part 2:')
    for row in data:
        for cell in row:
            print('██' if cell == 1 else '  ', end='')
        print()

def parse_line(line):
    if line[0] == 'f':
        return tuple(line.strip().split(' ')[-1].split('='))
    elif line.strip() != '':
        return tuple(int(x) for x in line.strip().split(','))

if __name__ == '__main__':
    input_data = parsing.file2data("../day13/input13.txt", parse_line)
    separator = input_data.index(None)
    input_dots = input_data[:separator]
    input_folds = input_data[separator+1:]
    part1(input_dots, input_folds)
    part2(input_dots, input_folds)