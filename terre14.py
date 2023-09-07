import sys
args = sys.argv
args.remove(args[0])
errArg = False
print(args)
print(len(args))
for i in args:
    if not i.isnumeric():
        errArg = True

if errArg or len(args) == 0:
    print("erreur.")
else:
    intArgs = [int(x) for x in args]
    test = False
    i = 1
    while i < len(intArgs):
        if intArgs[i] < intArgs[i - 1]:
            test = True
        i += 1
    if not test:
        print("Yes, List is sorted.")
    else:
        print("No, List is not sorted.")