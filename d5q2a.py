def etoile1(x):
     print(x*"*")
     if x>1:
      etoile1(x-1)#nombre d'etoiles de x a 1
      
def etoile2(k,x):
    print(k*"*")
    if k<x:
     etoile2(k+1,x) #nombre d'etoiles de 1 a x 

def etoiles(x):
   etoile1(x)
   etoile2(1,x)
while True:
 try:   
  n=int(input("entrer un entier positif"))
  if n>0 and type(n)==int:
      break
 except ValueError:
       if type(n)!=int:
        print("entrer un entier positif")

etoiles(n)





