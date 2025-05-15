################### Getters e Setters ####################
class Personagem:
    def __init__(self, nome, vida, defesa=0):
        self.nome = nome
        self.__vida = vida
        self.__defesa = defesa

    def mostrar_vida(self):
        return self.__vida

    @property
    def vida(self):
        return self.__vida
    
    @property
    def defesa(self):
        return self.__defesa
    
    @defesa.setter
    def defesa(self, valor):
        if valor >= 0 and valor <= 100:
            self.__defesa = valor
        else:
            print("Valor tem que estar entre 0 e 100.")
        




    
p = Personagem("Sky", 100)
print(p.vida)
p.defesa = 50
print(p.defesa)

p.defesa = 110    
print(p.defesa)

p.defesa = -10
print(p.defesa)


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

'''
pontuacao.pontos = -5
print(pontuacao.pontos)

'''


class Jogo:
    def __init__(self, dificuldade):
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

'''
jogo.dificuldade = 5
print(jogo.dificuldade)
'''






