# A program that makes an acronym based on the full meaning of an organization or concept givnen to it
# By Aminu Ahmadh
# GITHUB @AminuAhmadh


Sentence = input('Enter the full meaning of an organization or Concept: \n')
print()
words = Sentence.split()
acronym = ''
for word in words:
    acronym+=word[0]
print('Acronym:',acronym.upper())