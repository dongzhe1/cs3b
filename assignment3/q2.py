#################################################
# CS03B - Winter 2026
# Assignment 3 - Question 2
# Student Name: Zhe Dong
# SID: 20703849
#################################################


def generate(numRows):
    if numRows == 0:
        return []

    res = [[1]]
    for i in range(1, numRows):
        prev_row = res[-1]
        curr_row = [1]

        for j in range(1, i):
            curr_row.append(prev_row[j - 1] + prev_row[j])
        curr_row.append(1)

        res.append(curr_row)

    return res


def run():
    numRows = 5
    print(f"Input: {numRows}")
    print(f"Output: {generate(numRows)}")


if __name__ == "__main__":
    run()