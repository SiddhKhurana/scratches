#google coding interviw question 1 
def converttonum(word):
    dict1={}
    string=''
    for i in word:
        string.append(dict1[i])
    return string
def possiblestrings(phoneno,listofstrings):
    # 1st approach would be to map the string to numbers and find it in the phone number
    listofnums=list(map(converttonum,listofstrings))
    listpair=list(zip(listofnums,listofstrings))
    possiblestrings1=[]
    for num,word in listpair:
        if num in phoneno:
            possiblestrings.append(word)
    return possiblestrings1

print(possiblestrings('1800-356-9377',['flowers']))
