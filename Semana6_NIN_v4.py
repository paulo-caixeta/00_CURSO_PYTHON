def nin ():
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    print ("1 - para jogar uma partida isolada")
    print ("2 - para jogar um campeonato")
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

def partida ():
    n = int(input("Escolha quantas peças para jogar: "))
    m = int(input("Qual a quantidade máxima de peças removidas? "))
    print("Ok! O total de peças inicial é",n, "e remoção de no máximo",m, "peças por jogada.")
    i = 0
    while i < 1:    
        if n%(m+1) == 0:
            print("Você começa!")
            PC = False
            User = True
        else:
            print("Computador começa!")
            PC = True
            User = False
        i = i + 1
    while n > 0:
        if User == True:
            n = usuario_escolhe_jogada (n, m)
            User = False
            PC = True
            if n == 0:
                print("Você ganhou!")
                return ("User")
            else:
                print("Restam",n,"peças")               
        else:
            n = computador_escolhe_jogada (n, m)
            PC = False
            User = True
            if n == 0:
                print("O computador ganhou!")
                return ("PC")
            else:
                print("Restam",n,"peças")
                
def usuario_escolhe_jogada (n, m):
    mu = int(input("Escolha quantas peças remover: "))
    while mu > m:
        print ("Jogada não permitida. Escolha um número inteiro menor que",m,".")
        mu = int(input("Tente novamente! Escolha quantas peças remover: "))
    n = n - mu
    print("Ok! Você removeu",mu,"peças")
    return n

def computador_escolhe_jogada (n, m):
    mpc = m
    while mpc > 1 and (n - mpc)%(m+1) != 0:
        mpc = mpc - 1
    n = n - mpc
    print("O computador removeu",mpc,"peças")
    return n
