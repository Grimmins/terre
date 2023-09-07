import sys
# reprenons les notations de la division Euclidienne :
# a = bq + r  avec  0 <= r < b

a = int(sys.argv[1])
b = int(sys.argv[2])
if b == 0 or b > a:
    print("erreur.")
else:
    print("résultat : " + str(a//b))
    print("reste : " + str(a%b))
