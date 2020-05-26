montant=input("veuillez saisir votre montant en euro")
montant=int(montant)
billet20=montant//20
rest=montant % 20
billet10=rest //10
rest=rest % 10
billet5= rest //5
rest=rest % 5
piece2= rest // 2
print("dans votre billet il y'a",billet20,"billet de 20",billet10,"de billet de 10",billet5,"de billet de 5 et",piece2,"de piéce de 2euros et le reste c'est des piéces de un euro" )
