import sys

arg = sys.argv[1]
if int(arg[0:2]) > 12:
    ch = str(int(arg[0:2]) - 12) + ":" + arg[3:5] + "PM"
else:
    ch= arg[0:2] + ":" + arg[3:5] + "AM"
print(ch)

