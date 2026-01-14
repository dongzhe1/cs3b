#################################################
# CS03B - Winter 2026
# Assignment 1 - Question 2
# Student Name: Zhe Dong
# SID: 20703849
#################################################
import math


class Triangle:
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    @property
    def side1(self):
        return self.__side1

    @side1.setter
    def side1(self, value):
        self.__side1 = value

    @property
    def side2(self):
        return self.__side2

    @side2.setter
    def side2(self, value):
        self.__side2 = value

    @property
    def side3(self):
        return self.__side3

    @side3.setter
    def side3(self, value):
        self.__side3 = value

    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3

    def getArea(self):
        s = self.getPerimeter() / 2
        area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

        return area

    def toString(self):
        return f"Triangle: side1: {self.__side1}, side2: {self.__side2}, side3: {self.__side3}"


def run():
    t1 = Triangle()
    t2 = Triangle(3.0, 4.0, 5.0)  # Classic right triangle
    triangles = [t1, t2]

    print("--- the area and perimeter of each triangle: ---")
    for i in range(0, len(triangles)):
        print(f"{i}: {triangles[i].toString()}, perimeter: {triangles[i].getPerimeter():.2f}, area: {triangles[i].getArea():.2f}")


if __name__ == "__main__":
    run()