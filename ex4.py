import sys

def test(did_pass):
    # Print the result of a test
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


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

def test_suite():
    # Run the suite of tests for code in this file
    test(sum_to_even([1,3,5,1,2]) == 10)
    test(sum_to_even([1,3,5,1]) == 10)
    test(sum_to_even([2,8,5,7,8]) == 0)
    test(sum_to_even([1,3,2,5,1]) == 4)

test_suite()