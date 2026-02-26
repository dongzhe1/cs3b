#################################################
# CS03B - Winter 2026
# Assignment 3 - Question 1
# Student Name: Zhe Dong
# SID: 20703849
#################################################


def findNonExistNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]

def run():
    arr = [4,3,2,7,8,2,3,1]
    print(f"Input: {arr}")
    print(f"Output: {findNonExistNumbers(arr)}")


if __name__ == "__main__":
    run()