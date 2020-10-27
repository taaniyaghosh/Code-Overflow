# A program to find the simple interest given principal amount, rate of interest and time.
def simple_interest(principal, rate, time):
    print(f"The principal amount is {principal}")
    print(f"The rate of interest is {rate}")
    print(f"The time range is {time} years.")
    si = (principal * rate * time) / 100
    print(f"The Simple Interest is {si}")
    return si


p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time range: "))
simple_interest(p, r, t)
