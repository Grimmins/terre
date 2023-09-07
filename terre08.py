import sys

if len(sys.argv) != 3 or not sys.argv[2].isnumeric() or not sys.argv[1].lstrip('-+').isnumeric():
    print("erreur d'arguments, entrez un entier quelconque et un entier positif ou nul")
else:
    x = int(sys.argv[1])
    n = int(sys.argv[2])
    print(x**n)