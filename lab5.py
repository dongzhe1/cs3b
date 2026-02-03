

def recursive_power(number, exponent):
    """
    Challenge 2: Recursive Power Method
    """
    if exponent == 0:
        return 1

    return number * recursive_power(number, exponent - 1)


if __name__ == "__main__":
    base_num = 2
    exp_num = 3

    result = recursive_power(base_num, exp_num)

    print(f"{base_num} to the power of {exp_num} is {result}")