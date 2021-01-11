#google coding interviw question 1 
def converttonum(word):
    dict1={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'} #to fill with string
    string=''
    for i in word:
        for k,v in dict1.items():
            if i in v:
                string+=k
    return string
def possiblestrings(phoneno,listofstrings):
    # 1st approach would be to map the string to numbers and find it in the phone number
    listofnums=list(map(converttonum,listofstrings))
    listpair=list(zip(listofnums,listofstrings))
    possiblestrings1=[]
    for num,word in listpair:
        if num in phoneno:
            possiblestrings1.append(word)
    return possiblestrings1

phone=input('enter phone no.: ')
phone=phone.replace('-','')
x=int(input('enter no of test words: '))
lst=[]
for i in range(x):
    lst.append(input(f'enter  word {i+1}: '))
    