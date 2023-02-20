def check_palindrome(v): 
    reverse = v[::-1]  
  
    if (v == reverse): 
        return True
    return False
  
  
var = input(("Entrez une valeur: "))
if(check_palindrome(var)):
    print("L'entrée est un palindrome")
else:
    print("L'entrée n'est pas un palindrome")
	# return .split().join()