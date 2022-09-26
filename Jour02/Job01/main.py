class   Personne:

    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom
    
    def sePresenter(self):
        print("Je m'appel", self._prenom, self._nom)

    def getNom(self):
        return  self._nom
    
    def setNom(self, nom):
        self._nom = nom
    
    def getPrenom(self):
        return self._prenom
    
    def setPrenom(self, prenom):
        self._prenom = prenom

class   Livre:

    def __init__(self, titre, auteur):
        self._titre = titre
        self._auteur = auteur

    def afficher(self):
        print("Le titre du livre est \"", self._titre, "\" écrit par", self._auteur.getPrenom(), self._auteur.getNom())

class Auteur(Personne):

    def __init__(self, nom, prenom):
        Personne.__init__(self, nom, prenom)
        self.oeuvres = []
    
    def listerOeuvres(self):
        for oeuvre in self.oeuvres:
            oeuvre.afficher()
    
    def ecrireUnLivre(self, titre):
        new = Livre(titre, self)
        self.oeuvres.append(new)

marc = Auteur("Zimerman", "Marc")
marc.ecrireUnLivre("J'ai faim")
marc.listerOeuvres()