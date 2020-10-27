"""
    Bottom Up Dynamic Programming Approach for Fibonnaci Series
"""

def fib(n): 
  
    # array declaration 
    f = [0]*(n+1) 
  
    # base case assignment 
    f[1] = 1
  
    # calculating the fibonacci and storing the values 
    for i in range(2 , n+1): 
        f[i] = f[i-1] + f[i-2] 
    return f 
  
# Calling the function
print("Enter no of elements you want")
print("Fibonnaci Series is ",fib(int(input())))

