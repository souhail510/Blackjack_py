def sommeListePos_rec(l,n):
    if n==1 and l[n-1]>0 : # longueur de liste egale a 1
        somme=l[n-1]
    elif n>1 and l[n-1]>0:
        somme=sommeListePos_rec(l,n-1)+l[n-1] #index positif
    elif n>1 and l[n-1]<=0:
        somme=sommeListePos_rec(l,n-1) #index negatif
    else:
        somme=0
    return somme


k=input("entrer des valeurs separes par des virgules:")
l1=list(eval(k))
print(sommeListePos_rec(l1,len(l1)))
