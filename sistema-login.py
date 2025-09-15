import time

# Senha fixa
senha_correta = "1234"
tentativas_restantes = 3
tempo_limite = 30  # segundos

# Marca o início da sessão
inicio = time.time()
acesso_concedido = False

while tentativas_restantes > 0 and (time.time() - inicio) < tempo_limite:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        acesso_concedido = True
        break
    else:
        tentativas_restantes -= 1
        print(f"Senha incorreta. Tentativas restantes: {tentativas_restantes}")

# Verifica resultado final
tempo_total = time.time() - inicio

if acesso_concedido:
    print("✅ Acesso concedido com sucesso!")
elif tentativas_restantes == 0:
    print("❌ Acesso negado: número de tentativas excedido.")
elif tempo_total >= tempo_limite:
    print("⏰ Acesso negado: tempo limite excedido.")
