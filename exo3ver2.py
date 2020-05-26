R1=input("veuillez saisir la résistance R1")
R1=int(R1)
R2=input("veuillez saisir la résistance R2")
R2=int(R2)
R3=input("veuillez saisir la resitance R3")
R3=int(R3)
a=input("veuillez taper 1 ou 2 pour la resistance")
a=int(a)
if a==1:
 print("la résistance en série est :" ,R1+R2+R3)
else:
 print("la resistance en parallele est :",(R1*R2*R3)/(R1*R2+R1*R3+R2*R3))

