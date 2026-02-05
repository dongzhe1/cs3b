#################################################
# CS03B - Winter 2026
# Assignment 2 - Question 4
# Student Name: Zhe Dong
# SID: 20703849
#################################################


def generate_row_recursive(n, memo):
    if n == 1:
        row = "0"
        memo.append(row)
        return row

    prev_row = generate_row_recursive(n - 1, memo)
    current_row = "".join("01" if char == "0" else "10" for char in prev_row)
    memo.append(current_row)

    return current_row


def K_Grammar(n, k):
    memo = []

    final_row = generate_row_recursive(n, memo)
    result = int(final_row[k - 1])

    return result, memo


def run():
    NKPairs = [(1, 1), (2, 2), (4, 5)]

    for (N, K) in NKPairs:
        result, memo = K_Grammar(N, K)
        print(f"\nInput: N = {N}, K = {K}")
        print(f"Output: {result}")
        if N > 2:
            print("Explanation:")
            for idx, row in enumerate(memo):
                print(f"row {idx + 1}: {row}")


if __name__ == "__main__":
    run()