def is_palindrome(str):
    #Turn string into a list
    li=list(str)
    li_rev = li
    li_rev.reverse()
    if(li == li_rev):
        return True
    else:
        return False

print(is_palindrome("abba"))
print(not is_palindrome("abab"))
print(is_palindrome("tenet"))