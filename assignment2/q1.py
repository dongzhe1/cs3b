#################################################
# CS03B - Winter 2026
# Assignment 2 - Question 1
# Student Name: Zhe Dong
# SID: 20703849
#################################################


def convert_to_list_of_dicts(colors, codes):
    return [{'color_name': name, 'color_code': code} for name, code in zip(colors, codes)]


def create_dict_with_sets(keys, values):
    result = {}
    for k, v in zip(keys, values):
        if k not in result:
            # Using a set to match the sample output format
            # Although a list would be required to truly preserve all duplicate values.
            result[k] = set()
        result[k].add(v)
    return result

def run():
    print("A. Convert list to list of dictionaries: ")
    color_names = ["Black", "Red", "Maroon", "Yellow"]
    color_codes = ["#000000", "#FF0000", "#800000", "#FFFF00"]
    print("Input: ")
    print(color_names)
    print(color_codes)
    print("Output: ")
    print(convert_to_list_of_dicts(color_names, color_codes))

    print("\nB. Create a dictionary from two lists without losing duplicate values.")
    classes = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
    ids = [1, 2, 2, 3]
    print("Input: ")
    print(classes)
    print(ids)
    print("Output: ")
    print(create_dict_with_sets(classes, ids))

if __name__ == "__main__":
    run()