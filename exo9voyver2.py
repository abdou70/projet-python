#exo9voyver2
hd=input("veuillez l'heure de depart")
hd=int(hd)
md=input("veuillez saisir les minute de l'heure de depart")
md=int(md)
ha=input("veuillez saisir l'heure d'arrivé")
ha=int(ha)
ma=input("veuillez saisir les minutes de l'heure d'arrivé")
ma=int(ma)
if (ma+60-md>60):
    print("Votre voyage a durée :",24+ha-hd,"heures",ma-md,"minutes")
else:
    print("Votre voyage a durée :",23+ha-hd,"heures",60+ma-md,"minutes")

