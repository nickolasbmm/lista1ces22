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


a = ["banana","rosa","maca"]
b = ["banana","sam","rosa","maca"]
c=["sam","banana","rosa","maca"]
d=["banana","rosa","maca","sam","sam"]
print(words_to_sam(a))
print(words_to_sam(b))
print(words_to_sam(c))
print(words_to_sam(d))