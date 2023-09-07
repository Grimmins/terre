import sys

arg = sys.argv[1]
if arg.lstrip('-+').isnumeric():
    if int(arg)%2==0:
        print("pair")
    else:
        print("impair")
else:
    print("Tu ne me la mettras pas à l'envers")