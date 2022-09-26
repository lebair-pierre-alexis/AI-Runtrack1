class   Personne:

    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom
    
    def sePresenter(self):
        print("Je m'appel", self.__prenom, self.__nom)
    
    def get_nom(self):
        return  self.__nom
    
    def set_nom(self, nom):
        self.__nom = nom
    
    def get_prenom(self):
        return self.__prenom
    
    def set_prenom(self, prenom):
        self.__prenom = prenom

marcus = Personne("Philibert", "Marcus")
jean = Personne("Gatier", "Jean")
antoine = Personne("Santonin", "Antoine")

marcus.sePresenter()
jean.sePresenter()
antoine.sePresenter()

jean.set_nom("Michel")
antoine.set_prenom("Maxime")
print(jean.get_nom())
print(antoine.get_prenom())