import helper.parsing as parsing

# Intersections of segments used by numbers with the same number of segments
displays = {2: ['c', 'f'],
            3: ['a', 'c', 'f'],
            4: ['b', 'c', 'd', 'f'],
            5: ['a', 'd', 'g'],
            6: ['a', 'b', 'f', 'g'],
            7: ['a', 'b', 'c', 'd', 'e', 'f', 'g']}

# Converts combinations of segments to integers
segments_to_int = {'abcefg':0, 'cf':1, 'acdeg':2, 'acdfg':3, 'bcdf':4, 'abdfg':5, 'abdefg':6, 'acf':7, 'abcdefg':8, 'abcdfg':9}

def solve(data, part):
    answer = 0
    for numbers, outputs in data:
        # Create dictionary with all options for a certain segment
        possible_combinations = dict([(chr(i+97), set(chr(j+97) for j in range(7))) for i in range(7)])

        # Rule out options based on number of segments per character
        for length in displays.keys():
            w = list(frozenset(y for y in x) for x in filter(lambda z : len(z) == length, numbers))
            letters = w[0].intersection(*w[1:])
            for possible_segment in displays[length]:
                possible_combinations[possible_segment] = set(filter(lambda x : x in letters, possible_combinations[possible_segment]))

        # Rule out options based on options for other segments
        max_length = 7
        while max_length > 1:
            f = [list(possible_combinations[x])[0] for x in filter(lambda y : len(possible_combinations[y]) == 1, possible_combinations.keys())]
            for i in possible_combinations.keys():
                if len(possible_combinations[i]) > 1:
                    possible_combinations[i] = set(filter(lambda x : x not in f, possible_combinations[i]))
            max_length = max(len(i) for i in possible_combinations.values())

        reverse_dict = {list(value)[0] : key for key, value in possible_combinations.items()}

        # Read last numbers and determine values
        final_number = 0
        for i, number in enumerate(outputs):
            changed_number = sorted(reverse_dict[x] for x in number)
            int_number = segments_to_int["".join(changed_number)]

            if part == 1: answer += 1 if int_number in [1, 4, 7, 8] else 0
            else: final_number += int_number * 10**(3-i)
        if part == 2: answer += final_number
    print(f'Answer for part {part}: {answer}')


def part1(data):
    solve(data, 1)

def part2(data):
    solve(data, 2)

if __name__ == '__main__':
    input_data = parsing.file2data("../day8/input8.txt", lambda x : tuple(y.split() for y in x.strip().split(' | ')))
    part1(input_data)
    part2(input_data)