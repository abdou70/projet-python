#exocalen.py
jj=input("veuillez saisir le jour")
jj=int(jj)
mm=input("Veillex saisir le mois")
mm=int(mm)
aa=input("Veuillez saisir l'année")
aa=int(aa)
if ((aa % 4==0 and aa% 100!=0) or aa %400==0):
    print("Cette année est bisextille")
else :
    print("cette année n'est pas bissextile")