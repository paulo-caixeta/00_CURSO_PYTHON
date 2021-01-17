def partida ():
    print ("Vamos jogar?")
    #freguês escolhe quantas peças em jogo (n)
    n = int(input("Escolha quantas peças para jogar: "))
    #freguês escolhe de quantas em quantas peças serão as jogadas (m)
    m = int(input("Qual a quantidade máxima de peças removidas? "))
    print("Ok! Total de peças inicial =",n, "e remoção de no máximo",m, "peças por jogada.")
    mu = m
    mpc = m
    ni = int(n)

    if n%(m+1) == 0:
        print("Você começa!")
        PC = False
        User = True
        
    else:
        print("Computador começa!")
        PC = True
        User = False

    while ni != 0:
        if User == True:
            ni = usuario_escolhe_jogada (mu, m, ni)
            
        else:
            ni = computador_escolhe_jogada (mpc, m, ni)
            
    print("ACABOU")
            
def usuario_escolhe_jogada (mu, m, ni):
    mu = int(input("Escolha quantas peças remover: "))
    ni = ni - mu
    print("Restam",ni,"peças")
    User = False
    PC = True

def computador_escolhe_jogada (mpc, m, ni):
    while mpc > 1 and (ni - mpc)%(m+1) != 0:
        mpc = mpc - 1
    
    ni = ni - mpc
    print("O computador removeu",mpc,"peças")
    print("Restam",ni,"peças")
    PC = False
    User = True

