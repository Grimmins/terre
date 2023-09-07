import sys

arg = sys.argv[1]
if arg[5:7] == "PM":
    ch = str(int(arg[0:2]) + 12) + ":" + arg[3:5]
else:
    ch= arg[0:2] + ":" + arg[3:5]
print(ch)