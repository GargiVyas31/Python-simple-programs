__author__ = 'DELL'
string = input("Enter a sentence")
words = string.split()
words.sort()
for word in words:
    print(word)
