from collections import Counter, defaultdict
from functools import lru_cache

from helper import parsing



def part1(template, rules):
    new_template = [template[0]]
    for i in range(10):
        for j in range(1, len(template)):
            last = new_template[-1]
            key = last + template[j]
            insert = rules[key]
            new_template.append(insert)
            new_template.append(template[j])
        template = new_template
        new_template = [template[0]]
    c = Counter(template)
    least_used_value = min(c.values())
    most_used_value = max(c.values())
    print(f'Answer for part 1: {most_used_value - least_used_value}')
    pass

def part2(template, rules, iterations):
    @lru_cache(maxsize=None)
    def calculate_num_elements(first, last, remaining_rounds):
        if remaining_rounds == 0:
            counts = defaultdict(lambda : 0)
            counts[first] += 1
            return counts
        middle = rules[first + last]
        left_counts = calculate_num_elements(first, middle, remaining_rounds-1)
        right_counts = calculate_num_elements(middle, last, remaining_rounds-1)
        new_counts = defaultdict(lambda : 0)
        for k,v in right_counts.items():
            new_counts[k] += v
        for k,v in left_counts.items():
            new_counts[k] += v
        return new_counts

    count = defaultdict(lambda : 0)
    for i in range(1, len(template)):
        new_count = calculate_num_elements(template[i-1], template[i], iterations)
        for k, v in new_count.items():
            count[k] += v
    count[template[-1]] += 1
    least_used_value = min(count.values())
    most_used_value = max(count.values())
    print(f'Answer for part 2: {most_used_value - least_used_value}')

if __name__ == '__main__':

    input_data = parsing.file2data("../day14/input14.txt", lambda x : list(x.strip()) if len(x) > 3 and x[3] != '-' else tuple(x.strip().split(' -> ')))

    part1(input_data[0], dict(input_data[2:]))
    part2(input_data[0], dict(input_data[2:]), 40)