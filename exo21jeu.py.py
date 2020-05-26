a=int(input("veuilles saisir un entier a"))
b= ()
tour = 0
while(a!=b):
    b=int(input("veuillez saisir un entier b"))
    if (a>b):
        print("trop petit")
    if (a<b):
        print(" trop grand")
    tour = tour + 1
    continue
if (a==b):
    print("bravo vous l'avez trouvé et vous avez fait " ,tour, "tentatives")
