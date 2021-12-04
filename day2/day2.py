import helper.parsing as parsing

def part1(data) :
    horizontal_pos = 0
    depth = 0
    for instruction, amount in data:
        if instruction == 'forward':
            horizontal_pos += amount
        elif instruction == 'up':
            depth -= amount
        elif instruction == 'down':
            depth += amount

    print(f'Answer for part 1: {horizontal_pos * depth}\n')

def part2(data) :
    horizontal_pos = 0
    depth = 0
    aim = 0
    for instruction, amount in data:
        if instruction == 'forward':
            horizontal_pos += amount
            depth += aim * amount
        elif instruction == 'up':
            aim -= amount
        elif instruction == 'down':
            aim += amount

    print(f'Answer for part 2: {horizontal_pos * depth}')


if __name__ == '__main__':
    def parse_line(x : str):
        s = x.split()
        return s[0], int(s[1])
    input_data = parsing.file2data("../day2/input2.txt", parse_line)

    part1(input_data)
    part2(input_data)
