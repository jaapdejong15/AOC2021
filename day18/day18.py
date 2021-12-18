import copy
import math

from helper import parsing

class OperationHappened(Exception):
    pass

class TreeNode:
    def __init__(self, depth):
        self.depth = depth
        pass

    def __add__(self, o):
        self.increase_depth()
        o.increase_depth()
        return Node(self, o, depth=0)

    def increase_depth(self):
        self.depth += 1

    def check_explosion(self):
        return None, None

    def add_leftmost(self, number):
        pass

    def add_rightmost(self, number):
        pass

    def check_split(self):
        return None

    def get_magnitude(self):
        return 0

class Node(TreeNode) :
    def __init__(self, left_child, right_child, depth):
        super().__init__(depth)
        self.left_child : TreeNode = left_child
        self.right_child : TreeNode = right_child

    def __repr__(self):
        return f'[{self.left_child.__repr__()}, {self.right_child.__repr__()}]'

    def increase_depth(self):
        self.depth += 1
        self.left_child.increase_depth()
        self.right_child.increase_depth()

    def check_explosion(self):
        if self.depth == 3:
            if isinstance(self.left_child, Node):
                left_grandchild = self.left_child.left_child.value
                right_grandchild = self.left_child.right_child.value
                self.left_child = Leaf(0, depth=4)
                self.right_child.add_leftmost(right_grandchild)
                return left_grandchild, None
            elif isinstance(self.right_child, Node):
                left_grandchild = self.right_child.left_child.value
                right_grandchild = self.right_child.right_child.value
                self.right_child = Leaf(0, depth=4)
                self.left_child.add_rightmost(left_grandchild)
                return None, right_grandchild
            else: return None, None
        else:
            left_value, right_value = self.left_child.check_explosion()
            if right_value is not None:
                self.right_child.add_leftmost(right_value)
                raise OperationHappened()
            elif left_value is not None: return left_value, None
            else:
                left_value, right_value = self.right_child.check_explosion()
                if right_value is not None: return None, right_value
                elif left_value is not None:
                    self.left_child.add_rightmost(left_value)
                    raise OperationHappened()
                else: return None, None

    def add_leftmost(self, number):
        self.left_child.add_leftmost(number)

    def add_rightmost(self, number):
        self.right_child.add_rightmost(number)

    def check_split(self):
        left_result = self.left_child.check_split()
        if left_result is not None:
            self.left_child = left_result
            raise OperationHappened()
        right_result = self.right_child.check_split()
        if right_result is not None:
            self.right_child = right_result
            raise OperationHappened()
        return None

    def get_magnitude(self):
        return 3 * self.left_child.get_magnitude() + 2 * self.right_child.get_magnitude()

class Leaf(TreeNode) :
    def __init__(self, value, depth):
        super().__init__(depth)
        self.value: int = value

    def __repr__(self):
        return f'{self.value}'

    def add_leftmost(self, number):
        self.value += number

    def add_rightmost(self, number):
        self.value += number

    def check_split(self):
        if self.value > 9:
            return Node(Leaf(math.floor(self.value / 2), self.depth + 1), Leaf(math.ceil(self.value / 2), self.depth + 1), self.depth)
        else: return None

    def get_magnitude(self):
        return self.value

def part1(trees):
    last_tree = trees[0]
    for tree in trees[1:]:
        new_tree = last_tree + tree
        operations_happened = True
        while operations_happened:
            operations_happened = False
            try:
                left_value, right_value = new_tree.check_explosion()
                if left_value is not None or right_value is not None: raise OperationHappened()
                if new_tree.check_split() is not None: raise OperationHappened()
            except OperationHappened: operations_happened = True
        last_tree = new_tree
    print(f'Answer for part 1: {last_tree.get_magnitude()}')

def part2(trees):
    max_magnitude = 0
    for tree_a in trees:
        for tree_b in trees:
            if tree_a != tree_b:
                new_tree = copy.deepcopy(tree_a) + copy.deepcopy(tree_b)
                operations_happened = True
                while operations_happened:
                    operations_happened = False
                    try:
                        left_value, right_value = new_tree.check_explosion()
                        if left_value is not None or right_value is not None: raise OperationHappened()
                        if new_tree.check_split() is not None: raise OperationHappened()
                    except OperationHappened: operations_happened = True
                max_magnitude = max(max_magnitude, new_tree.get_magnitude())

    print(f'Answer for part 2: {max_magnitude}')

def parse_list(l, depth):
    if len(l) == 1:
        return Leaf(int(l), depth)
    pos = 0
    num_opening = 0
    num_closing = 0
    while True:
        if l[pos] == '[': num_opening += 1
        elif l[pos] == ']': num_closing += 1
        elif l[pos] == ',':
            if num_closing == num_opening - 1:
                return Node(parse_list(l[1:pos], depth+1), parse_list(l[pos+1:-1], depth+1), depth)
        pos += 1

if __name__ == '__main__':
    input_data = parsing.file2data("../day18/input18.txt", lambda y : parse_list(y.strip(), 0))
    part1(copy.deepcopy(input_data))
    part2(input_data)
