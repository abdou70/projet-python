def solution (a,b,c):
    delta=(b*b)-(4*a*c)
    if (delta < 0):
      print("l'equation n'a pas de solution")
    if(delta==0):
        return (-b-((delta)**(1/2)))/(2*a),(b-((delta)**(1/2)))/(2*a) 
    if (delta == 0):
      return (-b/(2*a))
     
            
