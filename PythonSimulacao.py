'''
Missão 1: A Tupla Intocável
A primeira regra da livraria é que as categorias não podem mudar.

    O que fazer: Crie uma variável chamada categorias_livraria e atribua a ela uma tupla contendo pelo menos 3 categorias de livros (ex: "Ficção", "Terror", "Romance").

    Dica: Lembre-se de qual pontuação (parênteses ou colchetes) o Python usa para tuplas, igual você fez com as emocoes.

Missão 2: O Dicionário do Livro
Você precisa estruturar os dados de um livro, assim como fez com os atributos de RPG.

    O que fazer: Crie um dicionário chamado livro1 com as seguintes chaves e seus respectivos valores: "codigo", "titulo", "autor", "ano", "preco", "quantidade".

Missão 3: O Banco de Dados
Agora precisamos de um lugar para guardar vários livros, que possa crescer ou diminuir.

    O que fazer: Crie uma lista vazia chamada banco_de_dados. Em seguida, use o comando correto para adicionar o livro1 (que você criou na Missão 2) dentro dessa lista.

Missão 4: A Função de Adicionar
Vamos automatizar a Missão 3 criando uma ferramenta reutilizável.

    O que fazer: Crie uma função chamada cadastrar_livro(novo_livro). Dentro dela, adicione o novo_livro à lista banco_de_dados e imprima uma mensagem de sucesso na tela. (Semelhante à sua função Adicionar_Pessoas).

Missão 5: O Loop de Estoque
Vamos usar um loop para ver o que temos guardado.

    O que fazer: Crie um loop for que percorra a sua lista banco_de_dados e imprima na tela apenas o "titulo" de cada livro armazenado.
'''

bibliotecarios = ["neza", "Albina", "Amanda", "Joao"]

Categorias_Livraria = ("Sci-fi", "Romance", "Terror")

Livraria = {"Livro1" : {"Titulo":"Oggy e as baratas tontas", "Genero": Categorias_Livraria[2], "Preco":66.6, "Autor": "Cara maluco que odeia a humanidade"}, "Livro2":{"Titulo":"Vingança do primeiro ano", "Genero": Categorias_Livraria[1], "Preco": 5, "PublicoAlvo":["Criancas","Adultos","Idosos"]}}

def AdicionarLivraria(Titulo, Genero, preco):
    
    length = len(Livraria) + 1

    NovoLivro = {f"Livro{length}": {"Titulo": Titulo, "Genero": Genero, "Preco":preco}}
    
    Livraria.update(NovoLivro)

AdicionarLivraria("Homem lampada", Categorias_Livraria[0], 99)

del Livraria["Livro1"]["Autor"]

Banco_de_dados = []

Banco_de_dados.append(Livraria["Livro1"])
Banco_de_dados.append(Livraria["Livro2"])
print(Banco_de_dados)

Contador = 1
for i in Livraria:
    print(Livraria[f"Livro{Contador}"]["Titulo"])
    Contador = Contador + 1

