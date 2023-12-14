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
        _cabinet.patient_in.append(_patient)
        print(f"bonjour très cher {_patient} ! ")
        
    def diagnostic(self,_cabinet,_patient):
        print(f"{docteur} : je vais vous diagnostiquer ! ")
        print(f"{_cabinet.patient_in} : d'accord docteur !")
        print("quelques minutes plus tard ...")
        print(f"{docteur} : je vois que vous avez une : {_patient.maladie}")
        
    def get_payed (self,_patient):
        if _patient.argent < 50 :
            print(f"{docteur}ah désolé vous avez pas assez d'argent ")
            print(f"{_patient} oh .. pouvez-vous me faire une faveur svp ? ")
            
        else:
            print(f"{docteur} : ca vous fera 50 €")
            self.argent += 50
            print(self.argent)
    
    def prescrire (self,_patient,_grille):
        for i in _grille:
            if _patient.maladie == i.maladie :
                print(f"{docteur} : je vais vous prescrire pour votre traitement   : {i.nom}")
                _patient.etat = "en traitement"
                
    def sortir(self,_cabinet,_patient,_attente):
        print(f"{docteur} : Bon je pense que nous en avons fini, je vous souhaite bon rétablissement et oubliez pas de prendre votre traitement à la pharmacie ! ")
        _cabinet.salle.remove(_patient)
        _cabinet.patient_out.append(_patient)
        _cabinet.patient_in.remove(_patient)
        _attente.salle.append(_patient)

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

grille = [bien_indente,save,check,ventoline,found]

print(salle_attente.salle)
print(cabinet.salle)
docteur.recevoir(cabinet,salle_attente,sangoku)
print(salle_attente.salle)
print(cabinet.salle)
docteur.diagnostic(cabinet,sangoku)
docteur.get_payed(sangoku)
docteur.prescrire(sangoku,grille)

docteur.sortir(cabinet,sangoku,salle_attente)
print(salle_attente.salle)


