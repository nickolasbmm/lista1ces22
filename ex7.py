def sum_of_squares(li):
    sum=0
    #For loop to go though all numbers
    for i in li:
        sum = sum + i*i
    return sum

#Test
print(sum_of_squares([2,-3,4]))