def fib(n):
  arr=[0]*(n+2)
  arr[0],arr[1]=0,1
  if n<=1:
    return n
  else:
    if arr[n-1]==0:
      arr[n-1]=fib(n-1)
    if arr[n-2]==0:
      arr[n-2]=fib(n-2)
    arr[n]=fib(n-1)+fib(n-2)
    return arr
  
n=int(input())
for i in range(n+1):
  print(fib(i),end=" ")
