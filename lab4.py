# Challenge 2


def number_analysis():
    """Number Analysis Program"""
    numbers = []
    for i in range(20):
        num = float(input(f"Enter number {i + 1} of 20: "))
        numbers.append(num)

    lowest = min(numbers)
    highest = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    print(f"Input list: {numbers}")
    print(f"Lowest number: {lowest}")
    print(f"Highest number: {highest}")
    print(f"Total: {total}")
    print(f"Average: {average}")


def get_initials():
    """Initials"""
    full_name = input("Enter your full name (First Middle Last): ")
    parts = full_name.split()

    initials = ""
    for name in parts:
        initials += name[0].upper() + ". "

    print(f"Initials: {initials.strip()}")

if __name__ == "__main__":
    print("===Number Analysis Program===")
    number_analysis()

    print("\n===Initials===")
    get_initials()