import sys


if len(sys.argv) > 2:
    print("erruer d'argument, entre UN UNIQUE string")
else:
    arg = sys.argv[1]
    print(arg)
    print("______________")
    ch = ""
    for i in range(len(arg)-1, -1, -1):
        ch += arg[i]
    print(ch)