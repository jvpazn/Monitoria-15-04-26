# ==========================================
# LISTAS E TUPLAS
# ==========================================

# 'Pessoas' é uma LISTA (usa colchetes []). Listas podem ser alteradas depois (adicionar, remover).
Pessoas = ["Joao", "Lucas", "Amanda", "Pedro"]

# 'emocoes' é uma TUPLA (usa parênteses ()). Tuplas são imutáveis (não podem ser alteradas).
emocoes = ("Raiva", "Felicidade", "Tristeza", "Desespero")

print(Pessoas) # Apenas mostra a lista original na tela


# ==========================================
# Loops utilizando as listas
# ==========================================

contador = 0 # Variável para controlar em qual posição (índice) estamos
listaTEMP = [] # Lista vazia que vai guardar a mistura das pessoas com as emoções

while True: # Inicia um loop infinito (vai rodar até achar um 'break')
    
    if contador % 2 == 0:
        # Se o contador for PAR (resto da divisão por 2 é zero), adiciona uma pessoa
        listaTEMP.append(Pessoas[contador])
        
    elif contador % 2 == 1:
        # Se o contador for ÍMPAR, adiciona uma emoção
        listaTEMP.append(emocoes[contador])

    contador = contador + 1 # Aumenta o contador para ir pro próximo item na próxima rodada

    # Verifica se o contador já chegou no tamanho total da lista 'Pessoas'
    if contador >= len(Pessoas):
        break # Se sim, quebra o loop infinito e continua o programa

print(listaTEMP, "\n") # Imprime a lista misturada e pula uma linha (\n)


# for l in Numeros:
    # print(l + 1)


# ==========================================
# DICIONÁRIOS
# ==========================================

# Cria um dicionário guardando atributos. Funciona no esquema "Chave": Valor.
Atributos_rpg = {"Forca": 5, "Destreza": 10, "inteligencia": 8}

# O método .update() adiciona uma nova chave e valor ao dicionário existente
Atributos_rpg.update({"Carisma" : 20})

print(Atributos_rpg)


# Dicionários aninhados: Um dicionário inteiro guardado dentro do valor de outro dicionário
Players_rpg = {"Julio":{"Forca": 5, "Destreza": 10, "inteligencia": 8},"nikani":{"Forca":1,"Destreza":0,"inteligencia": -2}}
Videos = {"Likes":10000, "Comentarios":{"Positivos":20, "Negativos":2, "Neutros":3}, "Salvos":4, "Enviados":20}

# Entra em 'Videos', abre a gaveta 'Comentarios', e pega apenas o valor de 'Positivos'
print(Videos["Comentarios"]["Positivos"])



# ==========================================
# FUNÇÕES CUSTOMIZADAS
# ==========================================

def Adicionar_Pessoas(pessoa):
    global Pessoas # Avisa o Python que vamos modificar a lista 'Pessoas' criada lá no topo do código
    
    Pessoas.append(pessoa) # Adiciona o novo nome no final da lista
    print(f"{pessoa} Foi adicionado a lista!")
    print(Pessoas, "\n")

# Adicionar_Pessoas("Michael jackson")


def remover_Pessoas(index):
    global Pessoas

    # Trava de segurança: checa se o número passado é maior que a lista ou se é negativo
    if index >= len(Pessoas) or index < 0:
        print(f"O index selecionado ({index}) é maior que o tamanho da lista! ({len(Pessoas)}), lembre-se que o indice inicia em 0!", "\n")
        return # O return vazio faz a função parar aqui mesmo, evitando que o programa quebre
        
    print(f"{Pessoas[index]} Foi removido(a) da lista!", "\n")
    Pessoas.pop(index) # O .pop() arranca o item que estiver na posição exata do 'index'
    print(Pessoas)

# remover_Pessoas(0)


def procurar_Pessoas(nome):
    # O 'in' pergunta se o texto exato do nome existe dentro da lista
    if nome in Pessoas:
        indice = Pessoas.index(nome) # O .index() descobre qual é a posição numérica daquele nome
        print(f"A pessoa {nome} foi encontrada no índice {indice}. \n")
    else:
        print(f"Não foi possivel achar '{nome}'. Certifique-se de que este nome está certo ou se existe.\n")

# procurar_Pessoas("Amanda")



# ==========================================
# MENU INTERATIVO
# ==========================================

def menu():
    while True: # Mantém o menu rodando para sempre, até o usuário escolher a opção 5 (sair)
        print('''
#selecione 1 :
#1- Buscar pessoa
#2- apagar pessoa
#3- adicionar pessoa
#4- listar a lista
#5- sair
''')
        
        # O 'try' tenta executar o código abaixo. Serve para não quebrar o programa se o usuário digitar letras.
        try:
            selecionador = int(input("> ")) # Pede o input e tenta converter para número inteiro (int)
        
        except ValueError: # Se der "erro de valor" (ex: digitou "A"), ele cai aqui
            print("Erro: Por favor, digite apenas o NÚMERO da opção desejada.\n")
            continue # O 'continue' ignora o resto do código abaixo e reinicia o loop 'while'

        # Estrutura de decisão (roteador) do menu
        if selecionador == 1:
            nome = input("Digite o nome da pessoa a procurar. >")
            procurar_Pessoas(nome) # Chama a função de busca
            
        elif selecionador == 2:
            apagador = int(input("Digite o indice em que a pessoa se encontra. >"))
            remover_Pessoas(apagador) # Chama a função de apagar
            
        elif selecionador == 3:
            adicionador = input("Digite o nome da pessoa a adicionar. >")
            Adicionar_Pessoas(adicionador) # Chama a função de adicionar
            
        elif selecionador == 4:
            print(Pessoas) # Apenas mostra a lista atual
            
        elif selecionador == 5:
            break # Quebra o loop infinito do menu, fechando o programa
            
        else:
            pass # Se digitar um número como 6 ou 7, o 'pass' não faz nada e o loop recomeça

menu()
