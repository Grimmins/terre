import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
if a==b or b==c or a==c:
    print("erreur.")
else:
    if a < b:
        if b < c:
            print(b)
        elif a < c:
            print(c)
        else:
            print(a)
    else:
        if a < c:
            print(a)
        elif b < c:
            print(c)
        else:
            print(b)
