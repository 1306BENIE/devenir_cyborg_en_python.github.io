class EtreVivant:
	def __init__(self, nom):
		self.nom = nom
		print(f"Coucou {self.nom} je suis un etre vivant")



class Humain(EtreVivant):
	def __init__(self, nom):
		EtreVivant.__init__(self, nom)

	def boire(self):
		print(f"Je boire de l'eau {self.nom}")


homme = Humain("BENIE")

homme.boire()