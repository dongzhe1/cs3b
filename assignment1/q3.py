#################################################
# CS03B - Winter 2026
# Assignment 1 - Question 3
# Student Name: Zhe Dong
# SID: 20703849
#################################################

class Employee:
    def __init__(self, name="", number=""):
        self.__name = name
        self.__number = number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class ProductionWorker(Employee):
    def __init__(self, name="", number="", shift=1, pay_rate=0.0):
        super().__init__(name, number)
        self.__shift = shift
        self.__pay_rate = pay_rate

    @property
    def shift(self):
        return self.__shift

    @shift.setter
    def shift(self, value):
        self.__shift = value

    @property
    def pay_rate(self):
        return self.__pay_rate

    @pay_rate.setter
    def pay_rate(self, value):
        self.__pay_rate = value


def run():
    name = input("enter productionWorker name: ")
    number = input("enter productionWorker number: ")
    try:
        shift = int(input("enter productionWorker shift number: "))
        pay_rate = float(input("enter productionWorker hourly pay rate: "))
    except ValueError:
        print("Invalid input. Using default values for shift and pay rate.")
        shift = 1
        pay_rate = 0.0

    productionWorker = ProductionWorker(name, number, shift, pay_rate)

    print("\n--- production worker information ---")
    print(f"name: {productionWorker.name}")
    print(f"number: {productionWorker.number}")

    shift_map = {1: "day", 2: "night"}
    print(f"shift: {productionWorker.shift}({shift_map.get(productionWorker.shift, "unknown")})")
    print(f"hourly pay rate: {productionWorker.pay_rate:.2f}")


if __name__ == "__main__":
    run()