class Pontuacao:
    def __init__(self, pontos):
        self.__pontos = pontos

    def adicionar_pontos(self, valor):
        self.__pontos += valor
        
    def mostrar_pontos(self):
        return self.__pontos
    
    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, valor):
        if valor < 0:
            raise ValueError("A pontuação não pode ser negativa.") # O raise é usado para gerar uma excessão
        self.__pontos = valor

pontuacao = Pontuacao(10)
print(pontuacao.pontos)

#Gerando uma exception message
'''
pontuacao.pontos = -5
print(pontuacao.pontos)

'''