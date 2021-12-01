import helper.parsing as parsing

def part1(data):
    answer = 0
    iterator = data.__iter__()
    last_number = iterator.__next__()
    for number in iterator:
        if number > last_number:
            answer += 1
        last_number = number
    print(f'Answer for part 1: {answer}')

def part2(data):
    answer = 0
    moving_sum = 0
    iter1 = data.__iter__()
    moving_sum += sum(iter1.__next__() for _ in range(3))
    iter2 = data.__iter__()
    for val in iter1:
        last_moving_sum = moving_sum
        moving_sum += val
        moving_sum -= iter2.__next__()
        if moving_sum > last_moving_sum:
            answer += 1
    print(f'Answer for part 2: {answer}')

if __name__ == '__main__':
    input_data = parsing.file2data('../day1/input1.txt', int)
    part1(input_data)
    part2(input_data)