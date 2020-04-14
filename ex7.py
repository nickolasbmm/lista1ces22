import sys

def test(did_pass):
    # Print the result of a test
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def sum_of_squares(li):
    sum=0
    #For loop to go though all numbers
    for i in li:
        sum = sum + i*i
    return sum

def test_suite():
    # Run the suite of tests for code in this file
    test(sum_of_squares([2,3,4])==29)
    test(sum_of_squares([])==0)
    test(sum_of_squares([2,-3,4])==29)

test_suite()