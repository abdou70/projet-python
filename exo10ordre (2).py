#exo10ordre
A=input("veuillez saisir la valeur de A")
A=int(A)
B=input("veillez saisir la valeur de B")
B=int(B)
C=input("Veuillez saisir la valeur de C")
C=int(C)
if (A<B and B<C):
    print(A<B<C)
elif (A<C and C<B):
    print(A<C<B)
if (B<A and A<C):
    print(B<A<C)
elif (B<C and C<A):
    print(B<C<A)
if (C<A and A<B):
    print(C<A<B)
elif (C<B and B<A):
    print (C<B<A)

