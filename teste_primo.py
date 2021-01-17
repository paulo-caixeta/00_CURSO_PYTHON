x = int (input("Digite x: "))
i = 2
eh_primo = True
while i < x and eh_primo != False:
	if x % i != 0:
		i = i+1
	else: 
		eh_primo = False
		print ("Não é primo")

if eh_primo == True:
	print ("É PRIMO")