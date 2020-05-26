#exo10ordre
a=input("veuillez saisir la valeur de A")
a=int(a)
b=input("veillez saisir la valeur de B")
b=int(b)
c=input("Veuillez saisir la valeur de C")
c=int(c)
if (a<b<c):
        print("A est inferieur à B qui est inferieur à C")
if (a<c and c<b):
     print("A est inferieur à C qui est inferieur à  B")
if (b<a and a<c):
     print("B est inferieur à A qui est inferieur à C")
if (b<c and c<a):
     print("B est inferieur à C qui est inferieur à A")
if (c<a and a<b):
     print("C est inferieur à A qui est inferieur à B")
if (c<b and b<a):
     print ("C est inferieur à B qui inferieur à A")
     

