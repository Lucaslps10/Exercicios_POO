################### Getters e Setters ####################
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida

    def mostrar_vida(self):
        return self.__vida

    @property
    def vida(self):
        return self.__vida
    
p = Personagem("Sky", 100)
print(p.vida)

class Pontuacao:
    def __init__(self, pontos = 0):
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

"""
pontuacao.pontos = -5
print(pontuacao.pontos)

"""


class Jogo:
    def __init__(self, dificuldade = 0):
        self.__dificuldade = dificuldade

    @property
    def dificuldade(self):
        return self.__dificuldade
    
    @dificuldade.setter
    def dificuldade(self, valor):
        if valor in [1, 2, 3]:
            self.__dificuldade = valor

        else:
            raise ValueError("Só há três níveis de dificuldade: 1, 2, 3;")
        
jogo = Jogo(2)
print(jogo.dificuldade)

jogo.dificuldade = 3
print(jogo.dificuldade)

"""
jogo.dificuldade = 5
print(jogo.dificuldade)
"""






