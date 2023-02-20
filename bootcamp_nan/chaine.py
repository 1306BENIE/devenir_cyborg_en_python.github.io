def chaine_caractere():
	mot = "morphologie"
	n = input("Saisir > ")
	liste = [] 


	for i in range(0, len(mot)):
		
		if (mot[i] in n):
			liste.append(i)
			print(liste)
			break

	

chaine_caractere()