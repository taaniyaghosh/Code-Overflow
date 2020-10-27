import array as arr
a= arr.array('i',[])
n= int(input('Enter Size of the array:"))
for i in range(0,n):
    x= int(input("Enter values:"))
    a.append(x)
for i in range(n):
    print(a[i],'')
#For finding maximum and minimum
max=min=a[0]
for i in range(n):
    if a[i]>max:
        max=a[i]
    if a[i]<min:
        min=a[i]
print('Maximum number:',max,'Minimum number:',min)


