import time
# ------------------- class ------------------------
class Patients ():
    def __init__(self,nom,maladie,etat,argent=float,poche=[]):
        self.nom = nom
        self.maladie = maladie
        self.argent = argent 
        self.etat = etat 
        self.poche = poche

class Docteur (Patients):
    def __init__(self, nom, maladie, etat, argent=float, poche=[]):
        super().__init__(nom, maladie, etat, argent, poche)
        
        
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
        
        
# ------------------ Instanciation ----------------
    
ben = Patients("ben","mal indenté","malade",100)
optimus = Patients("optimus","unsave","malade",200)
sangoku = Patients("sangoku","404","malade",80)
darthvader = Patients("darthvader","azamatique","malade",110)
semicolon = Patients("semicolon","syntaxError","malade",60)
docteur = Docteur("docteur","bonne santé","sain", 20000)