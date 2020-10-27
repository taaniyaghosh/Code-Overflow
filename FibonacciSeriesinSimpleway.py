limit = int(input("Enter Limit : "))

a = 0
b = 1
c = 1

print(a, b, end=" ")

while c<= limit:
    print(c, end=" ")
    a=b
    b=c
    c=a+b
