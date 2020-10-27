# A function to check if a number is an odd or even number
def check_number(number):
    if number % 2 == 0:
        print(f"The number {number} is an even number.")
    else:
        print(f"The number {number} is an odd number.")


num = int(input("Enter a number, I'll tell you if it is even or odd: "))
check_number(num)
