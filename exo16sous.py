# exo16sous
a=input("Veuillez saisir un entier a")
a=int(a)
b=input("Veuillez saisir un entier b")
b=int(b)
quot=0
r=a-b
i=1
while r>=b:
     r=r-b
     i = i +1
print("le quotient de ", a ,"divisé par", b ,"est :", i)