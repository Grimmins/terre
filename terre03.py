import string
import sys
letter = sys.argv[1]
alphabet = string.ascii_lowercase
for i in alphabet:
    if i == letter:
        ltrId = alphabet.index(i)
print(alphabet[ltrId:])