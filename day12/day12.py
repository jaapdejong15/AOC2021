from collections import defaultdict
from copy import copy
from functools import lru_cache

from helper import parsing


def part1(data):
    def find_all_paths(s, visited):
        new_visited = copy(visited)
        if s == 'end': return 1
        paths = 0
        if s[0].islower():
            new_visited.add(s)
        for n in connections[s]:
            if n not in new_visited:
                paths += find_all_paths(n, new_visited)
        return paths

    connections = defaultdict(lambda : set())
    for start, dest in data:
        connections[start].add(dest)
        connections[dest].add(start)
    print(f'Answer for part 1: {find_all_paths("start", set())}')


def part2(data):
    @lru_cache
    def find_all_paths(s, visited, visited_twice):
        new_visited = set(copy(visited))
        if s == 'end':
            return 1
        paths = 0
        if s[0].islower():
            new_visited.add(s)
        for n in connections[s]:
            if n not in new_visited:
                paths += find_all_paths(n, frozenset(new_visited), visited_twice)
            if not visited_twice and n in new_visited and n not in ['start', 'end']:
                paths += find_all_paths(n, frozenset(new_visited), True)
        return paths

    connections = defaultdict(lambda : set())
    for start, dest in data:
        connections[start].add(dest)
        connections[dest].add(start)
    print(f'Answer for part 2: {find_all_paths("start", frozenset(), False)}')


if __name__ == '__main__':
    input_data = parsing.file2data("../day12/input12.txt", lambda x : tuple(x.strip().split('-')))
    part1(input_data)
    part2(input_data)