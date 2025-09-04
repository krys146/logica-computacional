# Lista de preços dos itens
lista_de_compras = [5.99, 2.50, 3.75, 10.90, 1.99]

# Variável para armazenar o total
total = 0

# Loop para somar os preços
for preco in lista_de_compras:
    total += preco

# Exibe o total da compra
print(f"O total da compra é: R${total:.2f}")



nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Bem-vindo ao mundo do Python.")



a = 5
b = 3
print("A soma de a + b é:", a + b)



compras = [10.50, 5.25, 3.99]
total = 0
for item in compras:
    total += item
print(f"Total da compra: R${total:.2f}")


# Lista de mensagens não lidas
mensagens_nao_lidas = ["Oi!", "Você está disponível?", "Não esqueça da reunião às 15h", "Tudo certo por aí?"]

# Enquanto houver mensagens não lidas
while len(mensagens_nao_lidas) > 0:
    # Lê a primeira mensagem
    mensagem = mensagens_nao_lidas.pop(0)mensagens_nao_lidas = ["Oi!", "Você está disponível?", "Não esqueça da reunião às 15h", "Tudo certo por aí?"]

while len(mensagens_nao_lidas) > 0:
    mensagem = mensagens_nao_lidas.pop(0)
    print(f"Lendo mensagem: {mensagem}")
    print("Respondendo mensagem...\n")

print("Todas as mensagens foram lidas e respondidas.")

# Meta de economia
meta = 100
# Valor economizado por semana
economia_semanal = 10
# Total acumulado
total = 0
# Contador de semanas
semanas = 0

# Loop enquanto o total for menor que a meta
while total < meta:
    total += economia_semanal
    semanas += 1

# Exibe o resultado
print(f"Você precisará de {semanas} semanas para economizar R${meta}.")


    print(f"Lendo mensagem: {mensagem}")
    print("Respondendo mensagem...\n")

print("Todas as mensagens foram lidas e respondidas.")

meta = 100
economia_semanal = 10
total = 0
semanas = 0

while total < meta:
    total += economia_semanal
    semanas += 1

print(f"Você precisará de {semanas} semanas para economizar R${meta}.")



# Lista de alunos presentes
lista_presenca = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

# Nome a ser procurado
aluno_procurado = "Carlos"

# Verifica se o aluno está na lista
encontrado = False
for aluno in lista_presenca:
    if aluno == aluno_procurado:
        encontrado = True
        break

# Exibe o resultado
if encontrado:
    print(f"{aluno_procurado} está presente na sala.")
else:
    print(f"{aluno_procurado} não está na lista de presença.")


lista_presenca = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
aluno_procurado = "Carlos"
encontrado = False

for aluno in lista_presenca:
    if aluno == aluno_procurado:
        encontrado = True
        break

if encontrado:
    print(f"{aluno_procurado} está presente na sala.")
else:
    print(f"{aluno_procurado} não está na lista de presença.")



# lacos-repeticao.py

# Exercício 1: Soma de preços com loop for
lista_de_compras = [5.99, 2.50, 3.75, 10.90, 1.99]
total = 0
for preco in lista_de_compras:
    total += preco
print(f"Total da compra: R${total:.2f}")

# Exercício 2: Leitura de mensagens com loop while
mensagens_nao_lidas = ["Oi!", "Você está disponível?", "Não esqueça da reunião às 15h", "Tudo certo por aí?"]
while len(mensagens_nao_lidas) > 0:
    mensagem = mensagens_nao_lidas.pop(0)
    print(f"Lendo mensagem: {mensagem}")
    print("Respondendo mensagem...\n")
print("Todas as mensagens foram lidas e respondidas.")

# Exercício 3: Economizar para uma meta com loop while
meta = 100
economia_semanal = 10
saldo = 0
semanas = 0
while saldo < meta:
    saldo += economia_semanal
    semanas += 1
print(f"Você precisará de {semanas} semanas para economizar R${meta}.")

# Exercício 4: Verificar presença com loop for e if
lista_presenca = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]
aluno_procurado = "Carlos"
encontrado = False
for aluno in lista_presenca:
    if aluno == aluno_procurado:
        encontrado = True
        break
if encontrado:
    print(f"{aluno_procurado} está presente na sala.")
else:
    print(f"{aluno_procurado} não está na lista de presença.")

