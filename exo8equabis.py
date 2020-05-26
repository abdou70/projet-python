from math import *
print("veuillez saisir les coefficient de l'equation du second degrés")
a=input("saisir le cofficient de x2")
a=float(a)
b=input("veuillez saisir le coffecient de x")
b=int(b)
c=input("veuillez saisir la constante ")
c=int(c)
delta =(b**2)- (4*a*c)
if (delta <0):
    print("l'equation n'a pas de solution")
if (delta >0):

    x1 = (b-sqrt(delta))/2(a)
    x2 = (-b-sqrt(delta))/2(a)
    print("l'equation admet deux solutions", x1 ,"et",x2)
if (delta ==0):
    x= -(b/2(a))
    print("l'equation admet une solution double", x)
