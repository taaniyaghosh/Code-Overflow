def fizz_buzz(n):
    n=int(input("Enter the number:"))
    if (n%3==0)&(n%5==0):
        print("fizz buzz")
    elif n%3 == 0:
        print("fizz")
    elif n% 5 == 0:
        print("buzz")
    elif n%15!=0:
        print(n)
    else:
        print("invalid arguement")
fizz_buzz(n)