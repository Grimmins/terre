import string

ord1 = ord("a") # 97 si on le sait directement
for i in range(ord1, ord1+26):
    print(chr(i), end="")
print("\n")

# peut se faire avec les constantes définies :
# print(string.ascii_lowercase)