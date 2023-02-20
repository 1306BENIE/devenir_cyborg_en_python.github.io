import random

def alea():
	aleatoire = ["work", "house", "pack"]
	for i in range(1, len(aleatoire)+1):
		benie = random.choices(aleatoire, k=1)
	print(f"Le mot trouvé aleatoire est {benie}")


alea()
		