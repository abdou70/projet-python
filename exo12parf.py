nombre=input("Veuillez saisir un nombre")
nombre=int(nombre)
demi=nombre/2
i=1
som = 0
while (i <= demi) :
    if nombre % 1 ==0 :
     som = som + i
     i=i+1
if som==nombre :   
    print(nombre,"est un nombre parfait")
else:
    print(nombre,"n'est pas un nombre parfait")

