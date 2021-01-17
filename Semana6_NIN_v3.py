def nin ():
    print ("Vamos jogar?")
    resposta = str(input("Digite S/N:"))
    if resposta == "S":
        partida()
    else:
        print ("OK!")


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
               
        else:
            n = computador_escolhe_jogada (n, m)
            PC = False
            User = True           

    print("ACABOU")
            
def usuario_escolhe_jogada (n, m):
    mu = int(input("Escolha quantas peças remover: "))
    while mu > m:
        print ("Jogada não permitida. Escolha um número inteiro menor que",m,".")
        mu = int(input("Tente novamente! Escolha quantas peças remover: "))
    n = n - mu
    print("Ok! Você removeu",mu,"peças.")

    if n == 0:
        print("Você ganhou!")
    else:
        print("Restam",n,"peças")

    return n

def computador_escolhe_jogada (n, m):
    mpc = m
    while mpc > 1 and (n - mpc)%(m+1) != 0:
        mpc = mpc - 1
    
    n = n - mpc
    print("O computador removeu",mpc,"peças")
    if n == 0:
        print("O computador ganhou!")
    else:
        print("Restam",n,"peças")

    return n
