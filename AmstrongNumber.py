num = int(input("Enter numer : "))

temp = num
print(num)
sum = 0
digit = 0

while temp > 0:
    digit = temp % 10
    sum =sum + digit**3
    temp=temp//10

if num == sum:
    print(num,"Amstorng number")
else:
    print(num,"not a Amstrong number")

