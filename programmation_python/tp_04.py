# nom, prenom, aime la programmation, langage de programmation
# Traitement de donnees
# BENIE SYLVESTRE aime la Programmation et son langage prefere est python


userInfos = []

user_first_name = input("Nom > ")
userInfos.append(user_first_name)

user_last_name = input("Prenom(s) > ")
userInfos.append(user_last_name)

like_programmation = input("Aimez-vous la programmation (O / N) ? >")
if (like_programmation=="O"):
	like_programmation = True
	language=  input("Quel est votre langage de programmation ? >")
	
	
	userInfos.append(language)
else:
	like_programmation = False

# userInfos.append(like_programmation)

if (like_programmation == True):
	print(f"{userInfos[0]} {userInfos[1]} aime la programmation et son langage preferé est {userInfos[2]}")

else:
	print(f"{userInfos[0]} {userInfos[1]} n'aime pas la programmation")




