import itertools

import helper.parsing as parsing
import re

def data2boards(data):
    boards = []
    i = 2
    while i < len(data):
        boards.append(data[i:i+5])
        i += 6
    return data[0], boards

def check_board(board):
    # rows
    for i in range(5):
        complete = True
        for j in range(5):
            if board[i][j] is not None:
                complete = False
                break
        if complete:
            return True
    # columns
    for j in range(5):
        complete = True
        for i in range(5):
            if board[i][j] is not None:
                complete = False
                break
        if complete:
            return True
    return False



def part1(numbers, boards):
    for number in numbers:
        for board in boards:
            # Mark numbers
            for i, j in itertools.product(*(range(5), range(5))):
                if board[i][j] == number: board[i][j] = None
            if check_board(board):
                sum_unmarked_numbers = sum(sum(filter(lambda x : x is not None, row)) for row in board)
                print(f"Solution for part 1: {sum_unmarked_numbers * number}")
                return

def part2(numbers, boards):
    for number in numbers:
        boards_to_remove = []
        for board in boards:
            # Mark numbers
            for i, j in itertools.product(*(range(5), range(5))):
                if board[i][j] == number:
                    board[i][j] = None
            if check_board(board):
                boards_to_remove.append(board)
                if len(boards) - len(boards_to_remove) == 0:
                    sum_unmarked_numbers = sum(sum(filter(lambda x : x is not None, row)) for row in board)
                    print(f'Answer for part 2: {sum_unmarked_numbers * number}')
                    return
        for board in boards_to_remove:
            boards.remove(board)


if __name__ == '__main__':
    input_data = parsing.file2data("../day4/input4.txt", lambda x : [int(y.strip()) if y != '' else None for y in re.split(',|\s+', x.strip())])
    input_numbers, input_boards = data2boards(input_data)
    part1(input_numbers, input_boards)
    part2(input_numbers, input_boards)