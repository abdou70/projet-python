#exo13calendrier.py
jj=input("veuillez saisir le jour")
jj=int(jj)
mm=input("Veillex saisir le mois")
mm=int(mm)
aa=input("Veuillez saisir l'année")
aa=int(aa)
if(jj>31 or  mm>12) :
  print("cette n'est pas valide")
if(jj==29 and (aa % 400 !=0)):
 print("Cette date est invalide")
if (jj==29 and aa% 100 ==0):
 print("Cette date n'est pas invalide")
