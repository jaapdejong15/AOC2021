import copy

from helper import parsing

def solve(alg, image, num_iterations):
    margin = 2 * num_iterations
    padded_image = [[0 for _ in range(len(image[0]) + 2 * margin)] if i < margin or i >= len(image) + margin else [0 if j < margin or j >= len(image) + margin else 1 if image[i-margin][j-margin] == '#' else 0 for j in range(len(image) + 2 * margin)] for i in range(len(image) + 2 * margin)]
    for i in range(num_iterations):
        new_image = [[0 for _ in range(len(padded_image[0]))] for _ in range(len(padded_image))]
        for y in range(1, len(padded_image) - 1):
            for x in range(1, len(padded_image[0]) - 1):
                kernel = [padded_image[y - 1][x - 1:x + 2], padded_image[y][x - 1:x + 2], padded_image[y + 1][x - 1:x + 2]]
                new_image[y][x] = 1 if alg[int(''.join(map(lambda z : ''.join(map(lambda w: str(w), z)), kernel)), 2)] == '#' else 0
        padded_image = copy.deepcopy(new_image)
    return sum(sum(row[num_iterations:-num_iterations]) for row in padded_image[num_iterations:-num_iterations])

if __name__ == '__main__':
    input_data = parsing.file2data("../day20/input20.txt", lambda y : y.strip())
    image_enhancement_algorithm = input_data[0]
    input_image = input_data[2:]
    print(f'Answer for part 1: {solve(image_enhancement_algorithm, input_image, 2)}')
    print(f'Answer for part 2: {solve(image_enhancement_algorithm, input_image, 50)}')