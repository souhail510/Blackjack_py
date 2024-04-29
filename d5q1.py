from random import shuffle

class Blackjack:
 valeurs={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
 
 def joue(self):
  '''jour un jeu'''   
  d = JeuDeCartes()
  d.battre()
  
  banque = Main('Banque')
  joueur = Main('Joueur')

  # donne deux cartes au joueur et deux cartes a la banque
  for i in range(2):  
    joueur.ajouteCarte(d.tireCarte())
    banque.ajouteCarte(d.tireCarte())
  
  # montre les mains
  banque.montreMain()
  joueur.montreMain()
  # tant que le joueur demande Carte!, la banque tire des cartes
  reponse = input('Carte? Oui ou non? (Par défaut oui) ')
  while reponse in ['','o','O','oui','Oui']:
    c = d.tireCarte()
    print("Vous avez:")
    print(c)
    joueur.ajouteCarte(c)
    if self.total(joueur) > 21:
       print("Vous avez dépassé 21. Vous avez perdu.")
       return   
    reponse = input('Carte? Oui ou non? (Par défaut oui) ')

  # la banque joue avec ses regles  
  while self.total(banque) < 17:
    c = d.tireCarte()
    print("La banque a:")
    print(c)

    banque.ajouteCarte(c)
    if self.total(banque) > 21:
       print("La banque a dépassé 21. Vous avez gagné.")
       return

  # si 21 n'est pas depassée, compare les mains pour trouver le gagnat  
  self.compare(banque, joueur)

      
 def total(self, main):
    ''' (Main) -> int
    calcule la somme des valeur de toutes les cartes dans la main
    '''

    # calculez la somme de toutes les valeurs de la main
    somme=0
    for i in main.main:
       temp=i.valeur
       if temp=="A":
           temp=11
       elif temp=="J" or temp=="K" or temp=="Q":
           temp=10
       somme=somme+int(temp)
    
    # while la somme > 21 et il y a des As, deduisez 10 points pour chaque As
    for j in main.main:
        if somme>21 and j.valeur=="A":
         somme=somme-10
    
    return somme

  # a changer

 def compare(self, banque, joueur):
    ''' (Main, Main) -> None
    Compare la main du joueur avec la main de la banque
    et affiche de messages
    '''
 
    self.total(joueur)            
    self.total(banque)
    
    if self.total(banque)>self.total(joueur):
        print("vous avez perdu")

  
    elif self.total(banque)<self.total(joueur):
        print("vous avez gagne")
    
    else:#en cas d'egalite
      l=[]#liste valeur banque
      l2=[]#liste valeur joueur
      
      for i in banque.main:
            l.append(i.valeur)#la liste l contient les valeurs des cartes de banque
            
      for k in joueur.main:
            l2.append(k.valeur)#la liste l2 contient les valeurs des cartes de joueur   

      if "A" in l and("K" in l or "Q" in l or "J" in l or "10" in l) and len(l)==2 and self.total(banque)==21 and not("A" in l2 and("K" in l2 or "Q" in l2 or "J" in l2 or "10" in l2) and len(l2)==2): 
         print("vous avez perdu")#si la banque a un blackjack

      elif "A" in l2 and("K" in l2 or "Q" in l2 or "J" in l2 or "10" in l2) and len(l2)==2 and  self.total(joueur)==21 and not("A" in l and("K" in l or "Q" in l or "J" in l or "10" in l) and len(l)==2):
         print("vous avez gagne")#si le joueur a un blackjack

      else:
         print("egalite")#egalite sans blackjack
         
class Main(object):
    '''represente une main des cartes a jouer'''

    def __init__(self, joueur):
        '''(Main, str)-> none
        initialise le nom du joueur et la liste de cartes avec liste vide'''
        self.joueur=joueur
        self.main=[]

    def ajouteCarte(self, carte):
        '''(Main, Carte) -> None
        ajoute une carte a la main'''
        self.main.append(carte)
        
    def montreMain(self):
        '''(Main)-> None
        affiche le nom du joueur et la main'''
        print(self.joueur,self.main)
                
    def __eq__(self, autre):
        '''retourne True si les main ont les meme cartes
           dans la meme ordre'''
        return self.valeur==autre.valeur and self.couleur==autre.couleur and self.main[0]==autre.main[0]

    def __repr__(self):
        '''retourne une representation de l'objet'''
        return ("la main de ",str(self.joueur),"est ",str(self.main))
        
class Carte:
    '''represente une carte a jouer'''

    def __init__(self, valeur, couleur):
        '''(Carte,str,str)->None        
        initialise la valeur et la couleur de la carte'''
        self.valeur = valeur
        self.couleur = couleur  # pique, coeur, trefle ou carreau

    def __repr__(self):
        '''(Carte)->str
        retourne une representation de l'objet'''
        return 'Carte('+self.valeur+', '+self.couleur+')'

    def __eq__(self, autre):
        '''(Carte,Carte)->bool
        self == autre si la valeur et la couleur sont les memes'''
        return self.valeur == autre.valeur and self.couleur == autre.couleur

class JeuDeCartes:
    '''represente une jeu de 52 cartes'''
    # valeurs et couleurs sont des variables de classe
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    # couleurs est un set de 4 symboles Unicode qui representent les 4 couleurs
    # pique, coeur, trefle ou carreau
    
    def __init__(self):
        'initialise le paquet de 52 cartes'
        self.paquet = []          # paquet vide au debut
        for couleur in JeuDeCartes.couleurs: 
            for valeur in JeuDeCartes.valeurs: # variables de classe
                # ajoute une Carte de valeur et couleur
                
                self.paquet.append(Carte(valeur,couleur))

    def tireCarte(self):
        '''(JeuDeCartes)->Carte
        distribue une carte, la premiere du paquet'''
        return self.paquet.pop()

    def battre(self):
        '''(JeuDeCartes)->None
        pour battre le jeu des cartes'''
        shuffle(self.paquet)

    def __repr__(self):
        '''retourne une representation de l'objet'''
        return 'Paquet('+str(self.paquet)+')'

    def __eq__(self, autre):
        '''retourne True si les paquets ont les meme cartes
           dans la meme ordre'''
        return self.paquet == autre.paquet
    
b = Blackjack()
b.joue()

