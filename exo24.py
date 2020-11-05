sommeAdd = 0
sommeMulti = 1
valeur = int(valeur)
for i in range(1,101): #range(1,4) = [1,2,3]
    sommeAdd += i
    sommeMulti *= i
    
print(sommeAdd,sommeMulti)