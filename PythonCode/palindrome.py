words = input('Give me a list of five words separated by space: ').lower()
count =0
for word in words.split():
    if word[::-1] == word:
        print(word, 'is a palindrome')
        count+=1
    else:
        print(word, 'is not a palindrome!')
print(str(count), 'words are/is palindrome and the rest are not')

