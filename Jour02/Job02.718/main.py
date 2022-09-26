class   Personne:

    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    def getNom(self):
        return  self._nom
    
    def setNom(self, nom):
        self._nom = nom
    
    def getPrenom(self):
        return self._prenom
    
    def setPrenom(self, prenom):
        self._prenom = prenom

    def sePresenter(self):
        print("Je m'appel", self._prenom, self._nom)

class   Livre:

    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur
    
    def getTitre(self):
        return self._titre

    def getAuteur(self):
        return self._auteur
    
    def setAuteur(self, auteur):
        self._auteur = auteur
    
    def setTitre(self, titre):
        self._titre = titre

    def afficher(self):
        print("Le titre du livre est \"", self._titre, "\" écrit par", self._auteur.getPrenom(), self._auteur.getNom())

class   Client(Personne):

    def __init__(self, nom, prenom):
        Personne.__init__(self, nom, prenom)
        self._collection = []

    def getCollection(self):
        return self._collection
    
    def showCollection(self):
        print("Collection de", self.getNom(), ":")
        for livre in self.getCollection():
            print(livre.getTitre())
    
    def addToCollection(self, livre):
        for l in self._collection:
            if l.getTitre() == livre.getTitre():
                print("Ce livre fait déjà partie de cette collection")
                return False
        self._collection.append(livre)
        return True
    
    def rmvFromCollection(self, livre):
        for l in self._collection:
            if l.getTitre() == livre.getTitre():
                self._collection.remove(livre)

class   Bibliotheque:

    def __init__(self, nom):
        self._nom = nom
        self._catalogue = {"Livres": [], "Quantités": []}

    def getNom(self):
        return self._nom
    
    def getLivres(self):
        return self._catalogue.get("Livres")

    def getQuantites(self):
        return self._catalogue.get("Quantités")
    
    def setNom(self, nom):
        self._nom = nom
    
    def addToCatalogue(self, livre, quantite):
        for l in self.getLivres():
            if  l.getTitre() == livre.getTitre():
                i = self.getLivres().index(l)
                self.getQuantites()[i] += quantite
                return
        self.getLivres().append(livre)
        self.getQuantites().append(quantite)

    def rmvFromCatalogue(self, livre):
        i = self.getLivres().index(livre)
        if i != ValueError():
            self.getLivres().pop(i)
            self.getQuantites().pop(i)

    def acheterUnLivre(self, auteur, titre, quantite):
        livre = auteur.chercherOeuvre(titre)
        if livre != False:
            self.addToCatalogue(livre, quantite)
        else:
            print("Livre introuvable")

    def inventaire(self):
        for livre, quantite in zip(self.getLivres(), self.getQuantites()):
            print(livre.getTitre(), ":", quantite)

    def louer(self, client, titre):
        i = False
        for l in self.getLivres():
            if l.getTitre() == titre:
                i = self.getLivres().index(l)
                if client.addToCollection(self.getLivres()[i]):
                    self.getQuantites()[i] -= 1
                    if self.getQuantites()[i] == 0:
                        self.rmvFromCatalogue(self.getLivres()[i])
                    return
        print("Nous ne possedons pas se livre")

    def rendreLivres(self, client):
        while client.getCollection():
            livre = client.getCollection().pop()
            self.addToCatalogue(livre, 1)
            client.rmvFromCollection(livre)

class Auteur(Personne):

    def __init__(self, nom, prenom):
        Personne.__init__(self, nom, prenom)
        self._oeuvres = []
    
    def listerOeuvres(self):
        for oeuvre in self._oeuvres:
            oeuvre.afficher()
    
    def ecrireUnLivre(self, titre):
        new = Livre(titre, self)
        self._oeuvres.append(new)

    def chercherOeuvre(self, titre):
        for oeuvre in self._oeuvres:
            if oeuvre.getTitre() == titre:
                return oeuvre
        return False

marc = Auteur("Zimerman", "Marc")
frank = Auteur("Garcia", "Frank")
biblio = Bibliotheque("La grande page")
bob = Client("Ferrari", "Bob")

marc.ecrireUnLivre("J'ai faim")
marc.ecrireUnLivre("Nicolo le clodo")
frank.ecrireUnLivre("Le thon")
frank.ecrireUnLivre("J'adore les kinders buenos")

marc.listerOeuvres()
frank.listerOeuvres()
print("==========")
biblio.acheterUnLivre(marc, "Thon mayo", 6)
biblio.acheterUnLivre(marc, "Nicolo le clodo", 8)
biblio.acheterUnLivre(frank, "Le thon", 3)
biblio.acheterUnLivre(frank, "J'adore les kinders buenos", 1)
biblio.inventaire()
print("==========")
biblio.louer(bob, "Nicolo le clodo")
biblio.louer(bob, "J'adore les kinders buenos")
bob.showCollection()
print("==========")
biblio.inventaire()
print("==========")
biblio.rendreLivres(bob)
biblio.inventaire()