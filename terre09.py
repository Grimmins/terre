import sys

if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
    print("erreur d'argument, entrez un entier positif")
else:
    x = sys.argv[1]
    print(int(x)**0.5)