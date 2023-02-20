class personne:
	def __init__(self, nom, prenom, age):
		self.nom = nom
		self.prenom = prenom
		self.age = age

	def __str__(self):
		return f"je suis {self.nom} {self.prenom} j'ai {self.age} ans"
p1 = personne("BENIE", "SYLVESTRE", 23)

print(p1)