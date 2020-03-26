def sum_to(n):
    sum=0
    #For loop to go though all numbers
    for i in range(1,n+1):
        sum = sum + i
    return sum

#Test at n=10
print(sum_to(10))