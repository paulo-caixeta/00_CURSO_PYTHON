digitoigual = False

numero = int(input("Digite um número: "))

while numero > 1 and not digitoigual:
	
	d1 = numero % 10
	numero = numero // 10
	d2 = numero % 10	
	
	if d1==d2:
		digitoigual = True

print ("O número possui dígitos sequenciais iguais?")
if digitoigual:
	print ("Sim.")
else:
	print ("Não.")
	
