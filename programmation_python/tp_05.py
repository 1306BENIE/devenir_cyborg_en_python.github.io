print("""
	||======================================||
			BENIE SYLVESTRE				
											
		    REALISER PAR B613-CODEUR		
											
		TRAVAIL - RIGUEUR - EFFICACITE		
											
	||======================================||
	""")
print("====================== START PROGRAM =========================\n")

# nom, prenom, aime la programmation, langage de programmation
# Traitement de donnees
# BENIE SYLVESTRE aime la Programmation et son langage prefere est python'()
def programmation():
	infoUtilisateur = []

	nom = input("Votre nom > ")
	infoUtilisateur.append(nom)

	prenom = input("Votre prenom(s) >")
	infoUtilisateur.append(prenom)

	AimeProgrammation = input("Aimez-vous la programmation (Y / N) ?")

	if (AimeProgrammation == "Y"):
		AimeProgrammation = True

		langage = input("Quel est votre langage de programmation ?")
		infoUtilisateur.append(langage)

	else:
		AimeProgrammation = False

	if (AimeProgrammation == True):
		print(f"{infoUtilisateur[0]} {infoUtilisateur[1]} aime la programmation et son langage prefere est {infoUtilisateur[2]}")

	else:
		print(f"{infoUtilisateur[0]} {infoUtilisateur[1]} n'aime pas la programmation")

programmation()

print("\n====================== END PROGRAM =========================")






































