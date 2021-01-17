numero = int(input("Digite um número inteiro: "))
i = 1
soma = 0

while i>=0 and numero >= 1:
	di = numero % 10
	numero = numero // 10
	soma = soma + di
	
print (soma)

