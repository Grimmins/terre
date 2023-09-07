import sys

if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
    print("erreur d'argument, entrez un entier positif")
else:
    x = int(sys.argv[1])
    if x > 1:
        for i in range(2, int(x**0.5)+1):
            if (x % i) == 0:
                print("Non, " + str(x) + " n'est pas un nombre premier")
                break
        else:
            print("Oui, " + str(x) + " est un nombre premier")

    else:
        print("Non, " + str(x) + " n'est pas un nombre premier")
