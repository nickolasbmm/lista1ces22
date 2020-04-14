import sys
from random import randint

def test(did_pass):
    # Print the result of a test
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def is_prime(n):
    if(n==1):
        return False

    for i in range(2,int(n/2)):
        if(n%i==0):
            return False
    return True

def test_suite():
    # Run the suite of tests for code in this file
    test(is_prime(11))
    test(not is_prime(35))
    test(is_prime(19911121))
    test(is_prime(9829) == True)
    #My birthday is not a prime day
    test(is_prime(19990404) == False)

#Prime day test

def generatebirthday():
    year = '199' + str(randint(0,9))
    month = randint(1,12)
    if month <= 9:
        month = '0' + str(month)
    else:
        month = str(month)
    if month == '02':
        day = randint(1,28)
    if month == '01' or month == '03' or month == '05' or month == '07' or month == '08' or month == '10' or month == '12':
        day = randint(1,31)
    else:
        day = randint(1,30)
    if day <=9:
        day = '0' + str(day)
    else:
        day = str(day)

    birthday = year + month + day
    birthday = int(birthday)
    return birthday

def class_of_100_test():
    number_of_primes = 0
    for i in range(100):
        #Generate birthday and check if birthday is a prime
        birthday = generatebirthday()
        if is_prime(birthday):
            number_of_primes+=1
    return number_of_primes

def average_prime_birthdays(n):
    #repeat class_of_100_test n times and find the average number of prime birthdays
    total_num_primes=0
    for i in range(n):
        print("Generating class number: ",i+1)
        total_num_primes+=class_of_100_test()
    
    average = int(total_num_primes/n)
    return average

test_suite()

#Find average number of students with prime birth dates, repeat experiment 5 times

print("The average number of students with prime birth dates in a class of 100 is:",average_prime_birthdays(5))
