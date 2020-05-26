#exo19somentiersaisi
i=1
som=0
while i !=0:
  prix=input("veuillez saisir le prix du produit qui suit")
  prix=int(prix)
  som=som+prix
  i=input("taper 0 si y'a plus de produit")
  i=int(i)
print (som)