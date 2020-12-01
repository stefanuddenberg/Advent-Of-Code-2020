import numpy as np


def get_sorted_input_array(filename="input.txt"):
    with open(filename, "r") as f:
        data = f.read()

    arr = [int(i) for i in data.split()]
    arr.sort()
    return arr


def find_target_pair(arr, sum=2020):
    """Find a pair of numbers in an array
    that add up to the target sum."""
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == sum:
            return (arr[left], arr[right])
        elif arr[left] + arr[right] < sum:
            left += 1
        else:
            right -= 1
    return None


def find_target_triplet(arr, sum=2020):
    """Find a triplet of numbers in an array
    that add up to the target sum."""
    for left_index, left_value in enumerate(arr):
        right_arr = arr[left_index + 1 : len(arr)]
        target_sum = sum - left_value
        target_pair = find_target_pair(right_arr, sum=target_sum)
        if target_pair:
            return (left_value, *target_pair)

    return None


arr = get_sorted_input_array()
target_pair = find_target_pair(arr)
first_answer = np.product(target_pair)
print(f"First answer: {first_answer}")
target_triplet = find_target_triplet(arr)
second_answer = np.product(target_triplet)
print(f"Second answer: {second_answer}")
