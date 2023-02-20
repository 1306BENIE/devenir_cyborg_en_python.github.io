
def fonction(a):
	if(a<0 or a>15):
		return -1

	return (a*fonction(a-1))


print(fonction(15))