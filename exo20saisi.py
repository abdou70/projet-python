#exo25suitenom
for i in range (1,11):
    print(i*[i])
#-----commmit-------
a=int(input("veuillez saisir un entier a"))
div = a//2
if (a == 2 or a==3):
    print (a, "est un nombre premier")
div = 0
for i in range (4 , div+1):
     div = div + a % i
     if (div != 0):
        print(a , " est pas premier")
     if (div == 0):
        print(a , " n'est pas premier")