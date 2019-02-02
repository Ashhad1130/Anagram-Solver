from itertools import permutations
import nltk
string=input("Enter the string\n")
perms=[]
two_letter=[]
three_letter=[]
four_letter=[]
five_letter=[]
six_letter=[]
seven_letter=[]
all_words = set(nltk.corpus.words.words())
for i in range(2,len(string)+1):
    for p in permutations(string,r=i):
        t="".join(p)
        perms.append(t)
set(perms)
print("Output:")
for i in perms:
    if i in all_words:
        if(len(i)==2):
            two_letter.append(i)
        elif(len(i)==3):
            three_letter.append(i)
        elif(len(i)==4):
            four_letter.append(i)
        elif(len(i)==5):
            five_letter.append(i)
        elif(len(i)==6):
            six_letter.append(i)
        elif(len(i)==7):
            seven_letter.append(i)
print("Two Letter Words :")
for i in two_letter:
    print(i,end=' ')
print("\nThree Letter Words :")
for i in three_letter:
    print(i,end=' ')
print("\nFour Letter Words :")
for i in four_letter:
    print(i,end=' ')
print("\nFive Letter Words :")
for i in five_letter:
    print(i,end=' ')
print("\nSix Letter Words :")
for i in six_letter:
    print(i,end=' ')
print("\nSeven Letter Words :")
for i in seven_letter:
    print(i,end=' ')
