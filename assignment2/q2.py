#################################################
# CS03B - Winter 2026
# Assignment 2 - Question 2
# Student Name: Zhe Dong
# SID: 20703849
#################################################
from collections import Counter


def match_key_values(dict_x, dict_y):
    for key, value in dict_x.items():
        if key in dict_y and dict_y[key] == value:
            print(f"{key}: {value} is present in both x and y")


def sort_counter_by_value(data):
    return sorted(data.items(), key=lambda d: d[1], reverse=True)


def run():
    print("A. Match key values in two dictionaries.")
    x = {'key1': 1, 'key2': 3, 'key3': 2}
    y = {'key1': 1, 'key2': 2}
    print(f"Input: {x}, {y}")
    print(f"Output: ", end="")
    match_key_values(x, y)

    print("\nB. Sort Counter by value.")
    data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
    print(f"Input: {data}")
    print(f"Output: {sort_counter_by_value(data)}")

if __name__ == "__main__":
    run()