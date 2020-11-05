a = int(input("valeur entier: "))
somme = 0
for nombre in range(0, a+1):
    somme += (nombre ** 2)

if a == 1:
    somme = 1

print(somme)