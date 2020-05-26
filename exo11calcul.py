#exo11calcul
a=input("veuillez saisir la valeur de a")
a=int(a)
op=input("taper 1 pour l'addition , 2 pour la soustraction , 3 pour la multiplication et 4 pour la division " )
op=int(op)
b=input("veuillez saisir la valeut de b")
b=int(b)
if (op ==1):
  print (a+b) 
if (op ==2):
    print(a-b)
if (op==3):
    print(a*b)
if (op ==4):
    print(a/b)