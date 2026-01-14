#################################################
# CS03B - Winter 2026
# Assignment 1 - Question 1
# Student Name: Zhe Dong
# SID: 20703849
#################################################
import math

class Circle:
    def __init__(self, x=0, y=0, radius=1):
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def getArea(self):
        return math.pi * (self.__radius ** 2)

    def getPerimeter(self):
        return 2 * math.pi * self.__radius

    def containPoint(self, x, y):
        distance = math.sqrt((self.__x - x) ** 2 + (self.__y - y) ** 2)
        return distance <= self.__radius

    def containCircle(self, other_circle):
        distance = math.sqrt(
            (self.__x - other_circle.x) ** 2 + (self.__y - other_circle.y) ** 2)
        return distance <= (self.__radius - other_circle.radius)

    def overlaps(self, other_circle):
        distance = math.sqrt(
            (self.__x - other_circle.x) ** 2 + (self.__y - other_circle.y) ** 2)
        return distance < (self.__radius + other_circle.radius)


def run():
    c0 = Circle(5, 5, 5)
    c1 = Circle(2, 5, 2)
    c2 = Circle(8, 8, 3)
    c3 = Circle(4, 0, 2)
    circles = [c0, c1, c2, c3]

    print("--- print out the area and perimeter of each circle ---")
    for i in range(0, len(circles)):
        print(f"circle {i}: x: {circles[i].x}, y: {circles[i].y}, radius: {circles[i].radius}, area = {circles[i].getArea():.2f}, perimeter = {circles[i].getPerimeter():.2f}")

    print("\n--- check if the point (5, 5) lies inside any of your circles ---")
    px, py = 5, 5
    for i in range(0, len(circles)):
        if circles[i].containPoint(px, py):
            print(f"point ({px}, {py}) is inside circle {i}")
        else:
            print(f"point ({px}, {py}) is outside circle {i}")


    print("\n--- check if any of your circles contains any other circle ---")
    for i in range(0, len(circles)):
        for j in range(0, len(circles)):
            if i != j:
                if circles[i].containCircle(circles[j]):
                    print(f"circle {i} contains circle {j}")

    print("\n--- check if any of your circles overlaps any other circle ---")
    for i in range(0, len(circles)):
        for j in range(0, len(circles)):
            if i != j:
                if circles[i].overlaps(circles[j]):
                    print(f"circle {i} overlaps circle {j}")


if __name__ == "__main__":
    run()