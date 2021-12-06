import helper.parsing as parsing

def run_for_n_days(data, n):
    num_lantern_fish = [0] * 9
    for d in data:
        num_lantern_fish[d] += 1

    for i in range(n):
        num_new_lantern_fish = num_lantern_fish[0]
        for j in range(1, 9):
            num_lantern_fish[j-1] = num_lantern_fish[j]
        num_lantern_fish[6] += num_new_lantern_fish
        num_lantern_fish[8] = num_new_lantern_fish
    return sum(num_lantern_fish)

def part1(data):
    print(f'Answer for part 1: {run_for_n_days(data, 80)}')


def part2(data):
    print(f'Answer for part 2: {run_for_n_days(data, 256)}')


if __name__ == '__main__':
    input_data = parsing.file2data("../day6/input6.txt", lambda x : [int(y) for y in x.split(',')])
    part1(input_data[0])
    part2(input_data[0])