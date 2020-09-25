computador = 0
usuario = 0

def main():
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    opt = int(input(""))

    if opt == 1:    
        partida()
    else:
        campeonato()

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    global computador
    global usuario
    tabuleiro = n
    proximo = bool()
    jogada = 0
    x = 0

    if n % (m + 1) == 0:
        print("Você começa!")
        jogada = usuario_escolhe_jogada(n, m)
        tabuleiro -= jogada
        proximo = True
        print(" ")
        print("O usuário tirou", jogada, "peças.")
        if tabuleiro == 1:
            print("Agora resta apenas uma peça no", tabuleiro,".")
        elif tabuleiro == 0:
            print("Fim do jogo! Você ganhou!")
            usuario +=1
        else:    
            print("Agora restam", tabuleiro, "peças no tabuleiro.")
            print(" ")
    else:
        print("Computador começa!")
        jogada = computador_escolhe_jogada(n, m)
        tabuleiro -= jogada
        proximo = False
        if tabuleiro == 1:
            print("Agora resta apenas uma peça no", tabuleiro,".")
        elif tabuleiro == 0:
            print("Fim do jogo! O computador ganhou!")
            computador += 1
        else:    
            print("Agora restam", tabuleiro, "peças no tabuleiro.")
            print(" ")
            
    while tabuleiro > 0:
        if proximo == True:
            jogada = computador_escolhe_jogada(tabuleiro, m)
            tabuleiro -= jogada
            proximo = False
            print(" ")
            print("O computador tirou", jogada, "peças.")
            if tabuleiro == 1:
                print("Agora resta apenas uma peça no", tabuleiro,".")
            elif tabuleiro == 0:
                print("Fim do jogo! O computador ganhou!")
                computador += 1
            else:    
                print("Agora restam", tabuleiro, "peças no tabuleiro.")
            print(" ")
        else:
            jogada = usuario_escolhe_jogada(tabuleiro, m)
            tabuleiro -= jogada
            proximo = True
            print(" ")
            print("O usuário tirou", jogada, "peças.")
            if tabuleiro == 1:
                print("Agora resta apenas uma peça no", tabuleiro,".")
            elif tabuleiro == 0:
                print("Fim do jogo! Você ganhou!")
                usuario +=1
            else:    
                print("Agora restam", tabuleiro, "peças no tabuleiro.")
            print(" ")

def campeonato():
    i = 1
    print("Voce escolheu um campeonato!")
    while i <= 3:
        print("")
        print("**** Rodada",i ," ****")
        print("")
        partida()
        i += 1     

    print(" ")
    print("**** Final do campeonato! ****")
    print(" ")
    print("Placar: Você", usuario, "X", computador, "Computador")
    print(" ")

def computador_escolhe_jogada(n, m):
    jogada = 1
    while jogada != m:
        if (n - jogada) % (m+1) == 0:
            return jogada
        else:
            jogada += 1
    return jogada
    
def usuario_escolhe_jogada(n, m):
    x = False
    while not x:
        jogada = int(input('Quantas peças você vai tirar? '))
        if jogada < 1 or jogada > m:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
        else:
            x = True
    return jogada
main()  