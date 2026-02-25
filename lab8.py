
# Challenge 2
def find_peak_index_binary_search(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


def find_peak_index_linear(arr: list[int]) -> int:
    for i in range(1, len(arr) - 1):
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            return i

    return -1

if __name__ == "__main__":
    print(find_peak_index_binary_search([0, 1, 0]))
    print(find_peak_index_binary_search([3, 4, 5, 1]))
    print(find_peak_index_binary_search([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))

    print(find_peak_index_linear([0, 1, 0]))
    print(find_peak_index_linear([3, 4, 5, 1]))
    print(find_peak_index_linear([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))