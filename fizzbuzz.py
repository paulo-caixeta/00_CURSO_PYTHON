n = int(input("Digite um número inteiro: "))
rDiv3 = n % 3
rDiv5 = n % 5

if (rDiv3 == 0 and rDiv5 == 0):
	print ("FizzBuzz")

else:
	print (n)