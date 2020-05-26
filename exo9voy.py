#exo9voy
hd=input("veuillez l'heure de depart")
hd=int(hd)
md=input("veuillez saisir les minute de l'heure de depart")
md=int(md)
ha=input("veuillez saisir l'heure d'arrivé")
ha=int(ha)
ma=input("veuillez saisir les minutes de l'heure d'arrivé")
ma=int(ma)
if (ma<md):
    print("Votre voyage a durée :",ha-1-hd,"heures",ma+60-md,"minutes")
else:
    print("Votre voyage a durée :",ha-hd,"heures",ma-md,"minutes")
