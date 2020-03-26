def sum_to_even(li):
    sum=0
    found_even=False
    #For loop to go though all numbers
    for i in li:
        if not found_even:
            if(i%2==1):
                sum+=i
            else:
                found_even=True
    return sum


a = [1,3,5,1,2]
b = [1,3,5,1]
c=[2,8,5,7,8]
d=[1,3,2,5,1]
print(sum_to_even(a))
print(sum_to_even(b))
print(sum_to_even(c))
print(sum_to_even(d))