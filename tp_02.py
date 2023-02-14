print("""
	||======================================||
			BENIE SYLVESTRE				
											
		    REALISER PAR B613-CODEUR		
											
		TRAVAIL - RIGUEUR - EFFICACITE		
											
	||======================================||
	""")
print("====================== START PROGRAM =========================")
def verification(password = 1306, try_chance = 3):

	check_password = int(input(" Entrez votre mot de passe > "))
	while(check_password != password):
		try_chance -= 1
		print("Vérification du mot de passe.....")
		print(f"Mot de passe incorrect, il vous reste {try_chance} chance(s)")
		if (try_chance == 0):
		 	print("Votre code est bloqué veuillé vous rendre à l'agence")
		 	break
		check_password = int(input(" Entrez votre mot de passe > ")) 

	if (check_password==password):
		print("Vos identifiant ont été confirmé avec succès")
verification()

print("====================== END PROGRAM =========================")