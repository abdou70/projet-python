#exo23lapin
i= 2
first = 2
first1 = 2
while (i <= 10):
   nomb = first1 + first
   first = first1
   first1 = nomb
   i = i + 1
   continue
print("Au bout d'un an on aura ", nomb , "de lapin")
# Au bout de combien d'année depasse t-on le milliard de lapin
j= 2
first = 2
first1 = 2
nombre = 0
while (nombre < 10**9):
    nombre = first1 + first
    first = first1
    first1 = nombre
    j = j + 1
    continue
print("on depassera 1 milliar de lapin en",j, " mois")