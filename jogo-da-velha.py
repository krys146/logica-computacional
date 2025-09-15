# Função para criar o tabuleiro
def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

# Função para exibir o tabuleiro com loops aninhados
def mostrar_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    for linha in tabuleiro:
        for celula in linha:
            print(f"[{celula}]", end=" ")
        print()

# Função para verificar vitória
def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas e colunas
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)) or \
           all(tabuleiro[j][i] == jogador for j in range(3)):
            return True
    # Verifica diagonais
    if all(tabuleiro[i][i] == jogador for i in range(3)) or \
       all(tabuleiro[i][2 - i] == jogador for i in range(3)):
        return True
    return False

# Função para verificar empate
def verificar_empate(tabuleiro):
    return all(celula != " " for linha in tabuleiro for celula in linha)

# Função principal do jogo
def jogar
