def partida ():
    n = int(input("Escolha quantas peças para jogar: "))
    while n <= 0:
        print ("Jogada não permitida. Escolha um número inteiro positivo")
        n = int(input("Escolha quantas peças para jogar: "))
    m = int(input("Qual a quantidade máxima de peças removidas? "))
    while m >= n or m <= 0:
        m = int(input("Quantidade não permitida. Qual a quantidade máxima de peças removidas? "))
    print("Ok! O total de peças inicial é",n, "e remoção de no máximo",m, "peças por jogada.")
    mi = m
    if n%(m+1) == 0:
        print("Você começa!")
        User = True
    else:
        print("Computador começa!")
        User = False

    while n > 0:
        if User == True:
            mi = usuario_escolhe_jogada (n, m)
            User = False
            n = n - mi
            if n == 0:
                print("Você ganhou!")
                return ("User")
    
        else:
            mi = computador_escolhe_jogada (n, m)
            User = True
            n = n - mi
            if n == 0:
                print("O computador ganhou!")
                return ("PC")
                
def usuario_escolhe_jogada (n, m):
    mi = int(input("Escolha quantas peças remover: "))
    while mi > m or mi <= 0 or mi > n:
        print ("Jogada não permitida. Escolha um número inteiro, positivo e menor ou igual a",m)
        mi = int(input("Tente novamente! Escolha quantas peças remover: "))
    print("Você removeu",mi,"peças")
    return (mi)

def computador_escolhe_jogada (n, m):
    mi = m
    while mi > 1 and (n - mi)%(m+1) != 0:
        mi = mi - 1
    print("O computador removeu",mi,"peças")
    return (mi)

print ("Bem-vindo ao jogo do NIM! Escolha:")
print ("1 - para jogar uma partida isolada")
print ("2 - para jogar um campeonato")
resposta = int(input())
while resposta != 1 and resposta !=2:
    print ("Jogada não permitida. Digite 1 ou 2")
    resposta = int(input())
if resposta == 1:
    partida()
else:
    y = 1
    Vit_PC = 0
    Vit_User = 0
    while y <= 3:
        if partida() == "PC":
            Vit_PC = Vit_PC + 1
        else:
            Vit_User = Vit_User + 1
        y = y + 1
    print("Placar: Você",Vit_User,"X",Vit_PC,"Computador")
