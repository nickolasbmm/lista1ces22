import sys

def test(did_pass):
    # Print the result of a test
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok." .format(linenum)
    else:
        msg = "Test at line {0} FAILED.".format(linenum)
    print(msg)

def words_to_sam(li):
    words=0
    found_sam=False
    #For loop to go though all words
    for i in li:
        if not found_sam:
            if(i == "sam"):
                found_sam=True
                words+=1
            else:
                words+=1
    return words


def test_suite():
    # Run the suite of tests for code in this file
    test(words_to_sam(["banana","rosa","maca"]) == 3)
    test(words_to_sam(["banana","sam","rosa","maca"]) == 2)
    test(words_to_sam(["sam","banana","rosa","maca"]) == 1)
    test(words_to_sam(["banana","rosa","maca","sam","sam"]) == 4)

test_suite()