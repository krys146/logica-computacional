
# Lista de desenhos da forca (7 etapas: 0 a 6 erros)
desenhos = [
    """
     _______
    |/      
    |       
    |       
    |       
    |       
    |___    
    """,
    """
     _______
    |/      |
    |      (_)
    |       
    |       
    |       
    |___    
    """,
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |       
    |___    
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|
    |       |
    |       
    |___    
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |       
    |___    
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / 
    |___    
    """,
    """
     _______
    |/      |
    |      (_)
    |      \\|/
    |       |
    |      / \\
    |___    
    """
]

# Palavra secreta
palavra = "python"
letras_descobertas = ["_" for _ in palavra]
tentativas = 6
erros = 0

print("🎯 Bem-vindo ao Jogo da Forca!")

while tentativas > 0 and "_" in letras_descobertas:
    print(desenhos[erros])
    print("Palavra:", " ".join(letras_descobertas))
    letra = input("Digite uma letra: ").lower()

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra
        print("✅ Letra correta!")
    else:
        erros += 1
        tentativas -= 1
        print("❌ Letra incorreta! Tentativas restantes:", tentativas)

# Resultado final
if "_" not in letras_descobertas:
    print("🎉 Parabéns! Você venceu!")
else:
    print(desenhos[6])
    print("💀 Você perdeu! A palavra era:", palavra)

