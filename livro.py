class Livro:
    def __init__(self, titulo, autor, data_publicacao, numero_edicao):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao
        self.numero_edicao = numero_edicao

livro1 =  Livro("As aventuras de Tarzan", "Joao Pedro", "20 de janeiro, 2004", "Edicao 2")
print(livro1.titulo)
print(livro1.autor)
print(livro1.data_publicacao)
print(livro1.numero_edicao)