# different ways to count word(s) in a given sententence or word
# By Aminu Ahmadh GITHUB @AminuAhmadh

from collections import Counter


sentence = input('Enter a sentence: ').split()
print(Counter(sentence))

# Alternatively, here's a function
def WordCount(words):
    count = dict()
    for word in words.split():
        if word not in count:
            count[word] = 1
        else:
            count[word] = count[word] +1
    return (count)


''' alternatively, here's another function that read text file 
and count the occurence of words'''


def wordcount(fname):  
    try: 
        fhand=open(fname) 
    except:
        print('File can not be opened') 
        exit() 
    count=dict() 
    for line in fhand: 
        words=line.split() 
        for word in words: 
            if word not in count: 
                count[word]=1  
            else: 
                count[word]+=1 
    return(count)