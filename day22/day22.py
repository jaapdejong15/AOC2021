import itertools
import re

from helper import parsing

def part1(data):
    grid = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]
    for state, x_l, x_u, y_l, y_u, z_l, z_u in data:
        if -50 <= x_l <= 50:
            if state == 'on':
                for x,y,z in itertools.product(range(x_l, x_u + 1), range(y_l, y_u + 1), range(z_l, z_u + 1)):
                    grid[z][y][x] = 1
            if state == 'off':
                for x,y,z in itertools.product(range(x_l, x_u + 1), range(y_l, y_u + 1), range(z_l, z_u + 1)):
                    grid[z][y][x] = 0
    print(f'Answer for part 1: {sum(sum(sum(row) for row in l) for l in grid)}')

class Box:
    __slots__ = ['x', 'y', 'z', 'excluded_regions']

    def __init__(self, x_l, x_u, y_l, y_u, z_l, z_u):
        self.x = x_l, x_u
        self.y = y_l, y_u
        self.z = z_l, z_u
        self.excluded_regions = []

    def overlap(self, other):
        bounds = self.get_overlap_bounds(other)
        if bounds is None: return 0
        (lower_x, upper_x), (lower_y, upper_y), (lower_z, upper_z) = bounds
        return (upper_x - lower_x + 1) * (upper_y - lower_y + 1) * (upper_z - lower_z + 1)

    def get_overlap_bounds(self, other):
        lower_x = max(self.x[0], other.x[0])
        upper_x = min(self.x[1], other.x[1])
        lower_y = max(self.y[0], other.y[0])
        upper_y = min(self.y[1], other.y[1])
        lower_z = max(self.z[0], other.z[0])
        upper_z = min(self.z[1], other.z[1])
        if lower_x <= upper_x and lower_y <= upper_y and lower_z <= upper_z:
            return (lower_x, upper_x), (lower_y, upper_y), (lower_z, upper_z)
        return None

    def get_size(self):
        off_boxes_size = sum(x.get_size() for x in self.excluded_regions)
        return (self.x[1] - self.x[0] + 1) * (self.y[1] - self.y[0] + 1) * (self.z[1] - self.z[0] + 1) - off_boxes_size

    def exclude_region(self, b):
        bounds = self.get_overlap_bounds(b)
        if bounds is None: return
        (lower_x, upper_x), (lower_y, upper_y), (lower_z, upper_z) = bounds
        overlap = Box(lower_x, upper_x, lower_y, upper_y, lower_z, upper_z)
        for box in self.excluded_regions:
            box.exclude_region(overlap)
        self.excluded_regions.append(overlap)

def part2(data):
    boxes : list[Box] = []
    for state, x_l, x_u, y_l, y_u, z_l, z_u in data:
        b = Box(x_l, x_u, y_l, y_u, z_l, z_u)
        for box in boxes: box.exclude_region(b)
        if state == 'on': boxes.append(b)

    print(f'Answer for part 2: {sum(b.get_size() for b in boxes)}')


if __name__ == '__main__':
    input_data = parsing.file2data("../day22/input22.txt", lambda y : tuple(x if x in ['on', 'off'] else int(x) for x in re.findall('(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)', y)[0]))
    part1(input_data)
    part2(input_data)