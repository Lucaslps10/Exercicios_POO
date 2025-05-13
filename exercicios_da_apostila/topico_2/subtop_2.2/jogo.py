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
            print("Só há três níveis de dificuldade: 1, 2 e 3;")
        
jogo = Jogo(2)
print(jogo.dificuldade)

jogo.dificuldade = 3
print(jogo.dificuldade)


jogo.dificuldade = 5
print(jogo.dificuldade)
