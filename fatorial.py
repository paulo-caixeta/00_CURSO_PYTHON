# Recebe  o valor de um número natural n e imprime n!

n = int(input("Digite um número inteiro 'n': "))
n_fatorial = 1
i = 0
pi = 1
while i < n:
	pi = (n - i)
	i = i + 1
	n_fatorial = n_fatorial * pi

print (n_fatorial)
