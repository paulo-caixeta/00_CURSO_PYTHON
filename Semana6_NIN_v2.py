def nin ():
    print ("Vamos jogar?")
    resposta = str(input("Digite S/N:"))
    if resposta == "S":
        partida()
    else:
        print ("OK!")
        
def partida ():
    #freguês escolhe quantas peças em jogo (n)
    n = int(input("Escolha quantas peças para jogar: "))
    #freguês escolhe de quantas em quantas peças serão as jogadas (m)
    m = int(input("Qual a quantidade máxima de peças removidas? "))
    print("Ok! O total de peças inicial é",n, "e remoção de no máximo",m, "peças por jogada.")
    mu = m
    mpc = m
    ni = n
    i = 0

    while i < 1:    
#Testa condição para início da partida pelo PC ou Usuário        
        if n%(m+1) == 0:
            print("Você começa!")
            PC = False
            User = True
            
        else:
            print("Computador começa!")
            PC = True
            User = False

        i = i + 1

    while ni != 0:
        if User == True and PC == False:
            ni = usuario_escolhe_jogada (mu, m, ni)
                
        else:
            ni = computador_escolhe_jogada (mpc, m, ni)
            
    print("ACABOU")
            
def usuario_escolhe_jogada (mu, m, ni):
    mu = int(input("Escolha quantas peças remover: "))
    while mu > m:
        print ("Jogada não permitida. Escolha um número inteiro menor que",m,".")
        mu = int(input("Tente novamente! Escolha quantas peças remover: "))
    ni = ni - mu
    print("Ok! Você removeu",mu,"peças.")
    if ni == 0:
        print("Você ganhou!")
    else:
        print("Restam",ni,"peças")
    User = False
    PC = True

def computador_escolhe_jogada (mpc, m, ni):
    while mpc > 1 and (ni - mpc)%(m+1) != 0:
        mpc = mpc - 1
    
    ni = ni - mpc
    print("O computador removeu",mpc,"peças")
    if ni == 0:
        print("O computador ganhou!")
    else:
        print("Restam",ni,"peças")
    PC = False
    User = True

