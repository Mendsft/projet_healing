import time
import threading
from tabulate import tabulate

# ------------------- class ------------------------
class Patients ():
    def __init__(self,nom,maladie,etat,argent=float,poche=[]):
        self.nom = nom
        self.maladie = maladie
        self.argent = argent 
        self.etat = etat 
        self.poche = poche
        
    def se_deplacer(self,_lieu_depart,_lieu_arrive):
        print(f"{self.nom} : je me trouve à {_lieu_depart} et je vais aller cherche mes medocs à la {_lieu_arrive} ")
        _lieu_depart.salle.remove(self)
        _lieu_arrive.salle.append(self)
        
    def prendre_payer(self,_pharmacie,_grille,):
        print(f"{self} : bonjour, je suis venu chercher mon traitement , j'ai {self.maladie}")
        
        for i in _grille :
            if self.maladie == i.maladie :
                print(i.maladie)
                print(display_traitment())
                print(f"{_pharmacie.salle[0]} : Bonjour, je vois, je vais vous donner votre médoc qui est {i.nom}")
                print(f"{_pharmacie.salle[0]} : ca vous fera {i.prix} € ")
                
                if self.argent < i.prix :
                    print(f"{_pharmacie.salle[0]} : ah désole vous avez pas assez d'argent ... ")
                    self.etat = "mourrant..."
                    
                elif self.argent >= i.prix:
                    print(f"{self} : Voici svp !")
                    # self.poche = i.nom
                    print(f"{_pharmacie.salle[0]} : Merci,passez une bonne journée")
                    self.argent -=i.prix
                    _pharmacie.caisse +=i.prix  

                    self.etat = "entrain de se soigner"
                    self.poche.append(i)

    def __repr__(self):
        return self.nom
    
class Chat():
    def __init__(self,nom) :
        self.nom = nom
    def __repr__(self):
        return self.nom
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
        print(f"{_cabinet.patient_in[0]} : d'accord docteur !")
        print("quelques minutes plus tard ...")
        print(display_diagnostic())
        print(f"{docteur} : je vois que vous avez une : {_patient.maladie}")
        _cabinet.diagnostic = _patient.maladie
        
    def get_payed (self,_patient):
        if _patient.argent < 50 :
            print(f"{docteur}ah désolé vous avez pas assez d'argent ")
            print(f"{_patient} oh .. pouvez-vous me faire une faveur svp ? ")
            
        else:
            print(f"{docteur} : ca vous fera 50 €")
            self.argent += 50
            _patient.argent -=50
    
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
        print(dislay_cabinet())
        _cabinet.diagnostic = ""

    def __repr__(self):
        return self.nom
        
class Lieu ():
    def __init__(self,nom,salle = []):
        self.nom = nom
        self.salle = salle 
        
    def __repr__(self):
        return self.nom
class Cabinet (Lieu):
    def __init__(self, nom,diagnostic =[] ,salle=[],patient_in =[],patient_out = []):
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

ben = Patients("ben","mal indenté","malade",100,[])
optimus = Patients("optimus","unsave","malade",200,[])
sangoku = Patients("sangoku","404","malade",80,[])
darthvader = Patients("darthvader","azmatique","malade",110,[])
semicolon = Patients("semicolon","syntaxError","malade",60,[])
chat = Chat("chat")
docteur = Docteur("docteur","bonne santé","sain", 20000)
pharmacien = Patients("pharmacien","","bonne santé",)


patients = [ben,optimus,sangoku,darthvader,semicolon]

# medoc 
bien_indente = Medoc("bien indenté","mal indenté",60)
save = Medoc("save","unsave",100)
check = Medoc("check","404",35)
ventoline = Medoc("ventoline","azmatique",40)
found = Medoc("found","syntaxError",20)

grille = [bien_indente,save,check,ventoline,found]

# lieu 
salle_attente = Lieu("Salle d'attente",[ben,optimus,sangoku,darthvader,semicolon])
cabinet = Cabinet("cabinet ","",[docteur,chat])
pharmacie = Pharmacie("pharmacie",grille,100,["pharmacienne"])
cimetierre = Lieu("cimetière",["Fossoyeur"])

# # fonction miauler 
# def miauler ():
#     for i in range (100):
#         time.sleep(2)
#         print("*miaouwwww*")

# #chats :
# miauler = threading.Thread(target= miauler)
# miauler.start()
def display_patient():
    print("")
    print("Liste des patients")
    print("")
    
    header = [["nom","maladie","poche","etats","argent"]]
    for i in patients:
        content=[i.nom,i.maladie,i.poche,i.etat,f"{i.argent} €"]
        header.append(content)
    table = tabulate(header,headers='firstrow',tablefmt='grid')
    return table
    
    
def dislay_cabinet():
    print("")
    print("La salle du docteur")
    print("")
    
    header = [["nom","maladie","cabinet","Patient In","Patient ou "]]
    content=[cabinet.nom,cabinet.diagnostic,cabinet.salle,cabinet.patient_in,cabinet.patient_out]
    header.append(content)
    ds_cabinet = tabulate(header,headers='firstrow',tablefmt='grid')
    return ds_cabinet
    
def display_diagnostic ():
    print("")
    print("Liste diagnostic")
    print("")
    
    header = [["Maladie","Traitemnts"]]
    for i in grille :
        content= [i.maladie,i.nom]
        header.append(content)
    ds_diagnos = tabulate (header,headers='firstrow',tablefmt='grid')
    return ds_diagnos

def display_traitment ():
    print("")
    print("Liste des traitements")
    print("")
    header = [["Traitemnts","Prix"]]
    for i in grille :
        content= [i.maladie,f"{i.prix} €"]
        header.append(content)
    ds_diagnos = tabulate (header,headers='firstrow',tablefmt='grid')
    return ds_diagnos


def medecin (_cabinet,_salle,_patient,_grille,_pharmacie):

    print(display_patient())
    while True :
        if len(_salle.salle) != 0 :

            _patient = str(input(f"Entrez le patient que vous voulez faire rentrer dans le cabinet : {_salle.salle} :"))
            for i in patients:
                if _patient  == i.nom :
                    _patient = i

            docteur.recevoir(_cabinet,salle_attente,_patient)
            docteur.diagnostic(_cabinet,_patient)
            docteur.get_payed(_patient)
            docteur.prescrire(_patient,_grille)
            docteur.sortir(_cabinet,_patient,_salle)
            _patient.se_deplacer(_salle,_pharmacie)
            _patient.prendre_payer(_pharmacie,_grille)

        else:
            print(f"il ne reste plus personne, vous avez accueilli tous vos patients , vous avez gagné : {docteur.argent- 20000} € ajd !")
            print(f"voici un recap de la journéee ")
            print(display_patient())
            return False
            

# print(salle_attente.salle)
# print(cabinet.salle)
# docteur.recevoir(cabinet,salle_attente,sangoku)
# print(salle_attente.salle)
# print(cabinet.salle)
# docteur.diagnostic(cabinet,sangoku)
# docteur.get_payed(sangoku)
# docteur.prescrire(sangoku,grille)

# docteur.sortir(cabinet,sangoku,salle_attente)
# sangoku.se_deplacer(salle_attente,pharmacie)
# print(pharmacie.caisse,sangoku.argent)
# print(sangoku.poche)
# sangoku.prendre_payer(pharmacie,grille)
# print(pharmacie.caisse,sangoku.argent)
# print(sangoku.poche)
# print(cimetierre.salle)

medecin(cabinet,salle_attente,patients,grille,pharmacie)




