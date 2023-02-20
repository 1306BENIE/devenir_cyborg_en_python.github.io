print("""
	||======================================||
			BENIE SYLVESTRE				
											
		    REALISER PAR B613-CODEUR		
											
		TRAVAIL - RIGUEUR - EFFICACITE		
											
	||======================================||
	""")
print("====================== START PROGRAM =========================\n")
# Creation d'une classe
# creation d'une methode 
# communication entre les methode

class User():
	"""docstring for ClassName"""
	def add(self):
		print("L'utilisateur a été ajouté")
		
	
	def update(self):
		print("L'utilisateur a été modifié")

	def delate(self):
		print("L'utilisateur a été supprimé")
	def action(self):
		print("Une opération en cours .....")
		self.add()
		print("Opération terminé ")


User = User()

User.action()

print("\n====================== END PROGRAM =========================")