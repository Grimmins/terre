import sys

if len(sys.argv) > 2 or len(sys.argv) == 1 or sys.argv[1].isnumeric():
    print("erreur.")
else:
    count = 0
    for char in sys.argv[1]:
        count += 1
    print(count)
