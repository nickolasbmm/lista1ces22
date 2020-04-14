import sys

def test(did_pass):
    # Print the result of a test
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)


def is_palindrome(st):
    #Turn string into a list
    li=list(st)
    li_rev = list(st)
    li_rev.reverse()
    if(li == li_rev):
        return True
    else:
        return False


def test_suite():
    # Run the suite of tests for code in this file
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))

test_suite()