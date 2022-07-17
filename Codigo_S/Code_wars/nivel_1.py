"""DESAFIO CODE WARS - GRUPO 10
ANDRESSA DA CONCEIÇÃO SANTANA RIBEIRO
IARA VARJÃO BARBOSA
PEDRO AUGUSTO SANTIAGO JUNIOR
RAFAEL BOMBARDA ODA
VINICIUS AUGUSTO CARNEIRO
"""

# import sleep para definir um tempo (no caso 1 segundo) entre a geração de um mapa e outro
from time import sleep

# definição do itens que compõe o jogo
PAREDE = '#'
CAMINHO_LIVRE = ' '
CAMINHO_PERCORRIDO = "2"
ROBO = "4"
SAIDA = "S"

# definição de movimento com base no eixo X e Y
ESQUERDA = [0, -1]
DIREITA  = [0, 1]
CIMA     = [-1, 0]
BAIXO    = [1, 0]

# desenho do mapa e onde se inicia o ROBO
LABIRINTO = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'], 
    ['#', '#', '#', '#', '#', '#', ' ', ' ', '4', ' ', ' ', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'], 
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#'], 
    ['#', '#', '#', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'], 
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', ' ', '#'], 
    ['#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#'], 
    ['#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#'], 
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'S', '#']
]

# imprime o labirinto
def print_labirinto():
    print("")
    for linha in LABIRINTO:
        print("".join(linha))
    print("")

# definição de movimento que será feito pelo ROBO
def movimento(posicao: tuple, direcao: list):
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    return [posicao[0] + direcao[0], posicao[1] + direcao[1]]

# definição de volta de movimento quando o ROBO encontrar uma parede
def voltar(posicao: tuple, direcao: list):
    LABIRINTO[posicao[0]][posicao[1]] = CAMINHO_PERCORRIDO
    LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] = ROBO
    return [posicao[0] - direcao[0], posicao[1] - direcao[1]]   

# finalização caso encontre a SAIDA, se não, continua o jogo
def verifica_movimento(posicao: tuple, direcao: list) -> bool:
    if LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == SAIDA:
        raise print("SUCESSO")

    return (LABIRINTO[posicao[0] + direcao[0]][posicao[1] + direcao[1]] == CAMINHO_LIVRE)

def main():
    POSICAO_INICIAL = [3, 8]

    LABIRINTO[POSICAO_INICIAL[0]][POSICAO_INICIAL[1]] = ROBO

    print_labirinto()

    retorno = []

    POSICAO_ATUAL = POSICAO_INICIAL

    while True: # enquanto não encontrar a saída, o ROBO continua seu caminho.
        # Primeiro movimento será para cima.
        if verifica_movimento(POSICAO_ATUAL, CIMA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, CIMA)
            retorno.append(CIMA) #guarda os movimentos
            print_labirinto()
            sleep(1)

        # Se encontrar uma barreira, irá mudar para direita
        elif verifica_movimento(POSICAO_ATUAL, DIREITA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, DIREITA)
            retorno.append(DIREITA)
            print_labirinto()
            sleep(1)

        # Se encontrar uma barreira, irá mudar para baixo
        elif verifica_movimento(POSICAO_ATUAL, BAIXO):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, BAIXO)
            retorno.append(BAIXO)
            print_labirinto()
            sleep(1)

        # Se encontrar uma barreira, irá mudar para esquerda
        elif verifica_movimento(POSICAO_ATUAL, ESQUERDA):
            POSICAO_ATUAL = movimento(POSICAO_ATUAL, ESQUERDA)
            retorno.append(ESQUERDA)
            print_labirinto()
            sleep(1)

        else:
            #caso encontre uma barreira, irá buscar o seu último movimento e voltar
            voltar_casa = retorno[len(retorno)-1]
            POSICAO_ATUAL = voltar(POSICAO_ATUAL, voltar_casa)            

if __name__ == "__main__":
    main()