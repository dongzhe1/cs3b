

# challenge 2
def get_value(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        return None

my_list = ['a', 'b', 'c']


if __name__ == "__main__":
    for i in range(0, 4):
        print(f"index: {i}: {get_value(my_list, i)}")