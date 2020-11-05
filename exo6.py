valeurSec = input("valeur en seconde : ")
seconde = int(valeurSec)
heure = seconde // 3600
reste = seconde % 3600
minute = reste // 60
reste1 = seconde % 60
sec = reste1
print(heure, "heure ", minute,"min", reste1, "seconde")