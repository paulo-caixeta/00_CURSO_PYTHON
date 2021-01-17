numero = int(input("Digite o valor de n (n > 0): "))
n1 = numero
d = int(input("Digite o valor de d (0<=d<=9):"))
contd = 0

while numero>0:
    dn = numero % 10
    if dn == d:
        contd = contd + 1
    numero = numero // 10

print("O dígito",d,"ocorre",contd,"vezes em",n1)
