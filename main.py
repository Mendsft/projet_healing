import time
# -------------------class ------------------------
class Patients ():
    def __init__(self,nom,maladie,etat,argent=float,poche=[]):
        self.nom = nom
        self.maladie = maladie
        self.argent = argent 
        self.etat = etat 
        self.poche = poche
        
    def se_deplacer(self):
        pass
    def prendre(self):
        pass
    def payer(self):
        pass
class Lieu ():
    def __init__(self,nom,salle = []):
        self.nom = nom
        self.salle = salle 
        

    