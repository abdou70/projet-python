# exo24jeu2.py
a=int(input("veuillez entrer nombre"))
b= ()
while(b!=a):
    b=int(input("veuillez devinez le nombre saisi par l'utilisateur"))
    if (a > b):
      print("trop petit")
    if (a < b):
        print(" trop grand")
        continue
    if (a==b):
      print("C'est trouver")
     