def prime_range(lower_lim,upper_lim):
    ans = []
    for num in range(lower_lim, upper_lim + 1):
    # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                ans.append(num)
    return ans

""" Taking lower and upper limit from the user """

lower_lim = int(input())
upper_lim = int(input())

print("Prime numbers between", lower_lim, "and", upper_lim, "are:")
print(prime_range(lower_lim,upper_lim))

