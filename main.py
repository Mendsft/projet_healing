import time
# ------------------- class ------------------------
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
    
    def __repr__(self):
        return self.nom
    
class Chat():
    def __init__(self,nom) :
        self.nom = nom
    def __repr__(self):
        return self.nom

    def miauler(self):
        pass
class Docteur (Patients):
    def __init__(self, nom, maladie, etat, argent=float, poche=[]):
        super().__init__(nom, maladie, etat, argent, poche)
    
    def recevoir (self,_cabinet,_attente,_patient):
        _cabinet.salle.append(_patient)
        _attente.salle.remove(_patient)
        print(f"bonjour très cher {_patient} ! ")
        
    def diagnostic(self):
        pass
    def prescrire (self):
        pass
    def get_payed (self):
        pass
    
    def __repr__(self):
        return self.nom
        
class Lieu ():
    def __init__(self,nom,salle = []):
        self.nom = nom
        self.salle = salle 
    def __repr__(self):
        return self.nom
class Cabinet (Lieu):
    def __init__(self, nom,diagnostic ,salle=[],patient_in =[],patient_out = []):
        super().__init__(nom, salle)
        self.diagnostic = diagnostic
        self.patient_in = patient_in
        self.patient_out = patient_out
    
class Pharmacie (Lieu):
    def __init__(self, nom,medoc,caisse = float,salle=[]):
        super().__init__(nom, salle)
        self.medoc= medoc
        self.caisse = caisse
    def __repr__(self):
        return self.nom
class Medoc():
    def __init__(self,nom,maladie,prix=float):
        self.nom = nom
        self.maladie = maladie
        self.prix = prix 
    def __repr__(self):
        return self.nom
        
        
        
# ------------------ Instanciation ----------------
# personnage 
ben = Patients("ben","mal indenté","malade",100)
optimus = Patients("optimus","unsave","malade",200)
sangoku = Patients("sangoku","404","malade",80)
darthvader = Patients("darthvader","azamatique","malade",110)
semicolon = Patients("semicolon","syntaxError","malade",60)
chat = Chat("chat")
docteur = Docteur("docteur","bonne santé","sain", 20000)

# medoc 
bien_indente = Medoc("bien indenté","mal indenté",60)
save = Medoc("save","unsave",100)
check = Medoc("check","404",35)
ventoline = Medoc("ventoline","azmatique",40)
found = Medoc("found","syntaxError",20)
# lieu 
salle_attente = Lieu("Salle d'attente",[ben,optimus,sangoku,darthvader,semicolon])
cabinet = Cabinet("cabinet ","",[docteur,chat])


print(salle_attente.salle)
print(cabinet.salle)
docteur.recevoir(cabinet,salle_attente,sangoku)
print(salle_attente.salle)
print(cabinet.salle)