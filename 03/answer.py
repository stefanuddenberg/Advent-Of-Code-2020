from functools import reduce
import numpy as np

TREE_CHAR = "#"
OPEN_CHAR = "."
SLOPES = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]


def get_maze(filename="input.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()
        return lines


def get_tree_count(step_right=3, step_down=1):
    maze = get_maze()
    row, col = 0, 0
    line_length = len(maze[0].strip())
    tree_count = 0
    for row, line in enumerate(maze[::step_down]):
        line = line.strip()
        col %= line_length
        if line[col] == TREE_CHAR:
            tree_count += 1
        col += step_right
    return tree_count


def get_second_answer(slopes=SLOPES):
    tree_counts = [
        float(get_tree_count(step_right, step_down)) for step_right, step_down in slopes
    ]
    print(tree_counts)
    return np.prod(tree_counts)  # reduce((lambda a, b: a * b), tree_counts)


print(f"Tree count for 'three right, one down' = {get_tree_count()}")
print(f"Product of tree counts for all the slopes  = {get_second_answer()}")

