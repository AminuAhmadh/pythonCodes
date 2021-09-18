"""
A word is a palindrome if it has thesame spelling when reversed. Like "MOM".
"""


words = input('Give me a list of words separated by space: ').lower()
palindrome_count = 0
not_palindrome = 0
for word in words.split():
    if word[::-1] == word:
        print(word, 'is a palindrome')
        palindrome_count+=1
    else:
        print(word, 'is not a palindrome!')
        not_palindrome += 1
print()
print(str(palindrome_count), 'word(s) are palindrome.')
print(str(not_palindrome), 'word(s) are not Palindrome.')

