import helper.parsing as parsing

def part1(data):
    frequency = [sum(s[i] for s in data) for i in range(len(data[0]))]

    gamma = [1 if j > 0.5 * len(data) else 0 for j in frequency]
    epsilon = [0 if j == 1 else 1 for j in gamma]

    gamma_i = int(''.join(map(str, gamma)),2)
    epsilon_i = int(''.join(map(str, epsilon)),2)

    print(f'Answer for part 1: {gamma_i * epsilon_i}')

def part2(data):
    def do_iterations(start_data, is_oxygen):
        bit_position = 0
        while len(start_data) > 1:
            if is_oxygen:
                bit_criteria = 1 if sum(s[bit_position] for s in start_data) >= 0.5 * len(start_data) else 0
            else:
                bit_criteria = 1 if sum(s[bit_position] for s in start_data) < 0.5 * len(start_data) else 0
            new_data = list(filter(lambda x : x[bit_position] == bit_criteria, start_data))
            start_data = new_data
            bit_position += 1
        return start_data[0]

    answer = int(''.join(map(str, do_iterations(data, True))), 2) * int(''.join(map(str, do_iterations(data, False))), 2)
    print(f'Answer for part 2: {answer}')



if __name__ == '__main__':

    input_data = parsing.file2data("../day3/input3.txt", lambda x : [int(i) for i in x.strip()])
    part1(input_data)
    part2(input_data)