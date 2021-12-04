import helper.parsing as parsing

def part1(data):
    answer = 0
    iterator = iter(data)
    last_number = next(iterator)
    for number in iterator:
        if number > last_number:
            answer += 1
        last_number = number
    print(f'Answer for part 1: {answer}')

def part2(data):
    answer = 0
    moving_sum = 0
    iter1 = iter(data)
    moving_sum += sum(next(iter1) for _ in range(3))
    iter2 = iter(data)
    for val in iter1:
        last_moving_sum = moving_sum
        moving_sum += val
        moving_sum -= next(iter2)
        if moving_sum > last_moving_sum:
            answer += 1
    print(f'Answer for part 2: {answer}')

if __name__ == '__main__':
    input_data = parsing.file2data('../day1/input1.txt', int)
    part1(input_data)
    part2(input_data)
