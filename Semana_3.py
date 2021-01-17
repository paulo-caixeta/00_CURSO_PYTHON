# escreva o seu programa
n = int(input("Digite o valor de n: "))
xp = 0
xi = 0

while n>=0:
    if n%2 == 0:
        xp = xp + 1
        n= n - 1
    else:
        xi = xi +1
        n = n - 1

print("Pares =",xp,"Impares=",xi)
