def knapsack(W,wt,val,n):
  if n==0 or w==0:
    return
  if wt[n-1]>w:
    return knapsack(W,wt,val,n-1)
  else:
    return max(val[n-1]+knapsack(W-wt,wt,val,n-1), knapsack(W,wt,val,n-1))
val = list(map(int,input().split())) 
wt = list(map(int,input(.split())))
W = int(input())
n = len(val) 
print knapSack(W, wt, val, n) 
