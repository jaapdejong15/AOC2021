from copy import copy

import helper.parsing as parsing

error_values = {')':3, ']':57, '}':1197, '>':25137}
map_opening_to_closing = {'(': ')', '[':']', '{':'}', '<':'>'}

def part1(data):
    total = 0
    incomplete_lines = []
    for line in data:
        line_copy = copy(line)
        stack = []
        corrupted = False
        while line:
            char = line.pop(0)
            if char in ['(', '[', '{', '<']: stack.append(char)
            else:
                matching_char = stack.pop()
                if char != map_opening_to_closing[matching_char]:
                    total += error_values[char]
                    corrupted = True
                    break
        if not corrupted: incomplete_lines.append(line_copy)
    print(f'Answer for part 1: {total}')
    return incomplete_lines

autocomplete_values = {'(':1,'[':2,'{':3, '<':4}

def part2(data):
    scores = []
    for line in data:
        stack = []
        while line:
            char = line.pop(0)
            if char in ['(', '[', '{', '<']: stack.append(char)
            else: stack.pop()
        line_score = 0
        while stack: line_score += 4 * line_score + autocomplete_values[stack.pop()]
        scores.append(line_score)
    print(f'Answer for part 2: {sorted(scores)[int(len(scores)/2)]}')


if __name__ == '__main__':
    input_data = parsing.file2data("../day10/input10.txt", lambda x : list(x.strip()))
    part2(part1(input_data))