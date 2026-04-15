# LISTAS E TUPLAS

emocoes = ("Raiva", "Felicidade", "Tristeza", "Desespero")
Numeros = [1, 3, 5, 7, 9]

# Loops utilizando as listas

'''
contador = 0
listaTEMP = []


while True:
    if contador % 2 == 0:
        listaTEMP.append(Pessoas[contador])
    elif contador % 2 == 1:
        listaTEMP.append(emocoes[contador])

    contador = contador + 1

    if contador >= len(Pessoas):
        break

# print(listaTEMP, "\n")


for l in Numeros:
    print(l + 1)
'''

Atributos_rpg = {"Forca": 5, "Destreza": 10, "inteligencia": 8}
Players_rpg = {"Julio":{"Forca": 5, "Destreza": 10, "inteligencia": 8},"nikani":{"Forca":1,"Destreza":0,"inteligencia": -2}}
Videos = {"Likes":10000, "Comentarios":{"Positivos":20, "Negativos":2, "Neutros":3}, "Salvos":4, "Enviados":20}




print(Videos["Comentarios"]["Positivos"])

'''

# Funções


Pessoas = ["Joao", "Lucas", "Amanda", "Pedro"]

def Adicionar_Pessoas(pessoa):
    global Pessoas
    
    Pessoas.append(pessoa)
    print(f"{pessoa} Foi adicionado a lista!")
    print(Pessoas, "\n")

# Adicionar_Pessoas("Michael jackson")

def remover_Pessoas(index):
    global Pessoas

    if index >= len(Pessoas) or index < 0:
        print(f"O index selecionado ({index}) é maior que o tamanho da lista! ({len(Pessoas)}), lembre-se que o indice inicia em 0!", "\n")
        return
        
    print(f"{Pessoas[index]} Foi removido(a) da lista!", "\n")
    Pessoas.pop(index)
    print(Pessoas)

# remover_Pessoas(0)

def procurar_Pessoas(nome):
    if nome in Pessoas:
        indice = Pessoas.index(nome)
        print(f"A pessoa {nome} foi encontrada no índice {indice}. \n")
    else:
        print(f"Não foi possivel achar '{nome}'. Certifique-se de que este nome está certo ou se existe.\n")

# procurar_Pessoas("Amanda")





# Menu simples com funções
def menu():
    while True:
        print('''
#selecione 1 :
#1- Buscar pessoa
#2- apagar pessoa
#3- adicionar pessoa
#4- listar a lista
#5- sair
''')
        
        try:
            selecionador = int(input("> "))
        
        except ValueError:
            print("Erro: Por favor, digite apenas o NÚMERO da opção desejada.\n")
            continue

        if selecionador == 1:
            nome = input("Digite o nome da pessoa a procurar. >")
            procurar_Pessoas(nome)
        elif selecionador == 2:
            apagador = int(input("Digite o indice em que a pessoa se encontra. >"))
            remover_Pessoas(apagador)
        elif selecionador == 3:
            adicionador = input("Digite o nome da pessoa a adicionar. >")
            Adicionar_Pessoas(adicionador)
        elif selecionador == 4:
            print(Pessoas)
        elif selecionador == 5:
            break
        else:
            pass

menu()'''