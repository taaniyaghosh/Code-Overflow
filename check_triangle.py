# A function to check if a triangle is equilateral, isosceles or scalene.


def check_triangle(x, y, z):
    if x == y == z:
        print("This is an equilateral triangle.")
    elif x == y or x == z or y == z:
        print("This is an isosceles triangle.")
    else:
        print("The triangle is a scalene triangle.")


a = input("Enter the first side of the triangle: ")
b = input("Enter the second side of the triangle: ")
c = input("Enter the third side of the triangle: ")
check_triangle(a, b, c)
