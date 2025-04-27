#################### Encapsulamento (Public, Private) ############################

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida

    def mostrar_vida(self):
        return self.__vida

p1 = Personagem("Lucas", 100)
print(p1.mostrar_vida())


class Pontuacao:
    def __init__(self, pontos):
        self.__pontos = pontos

    def adicionar_pontos(self, valor):
        if valor > 0:
            self.__pontos += valor
        
    def mostrar_pontos(self):
        return self.__pontos
    
pontuacao = Pontuacao(0)
pontuacao.adicionar_pontos(10)
print(pontuacao.mostrar_pontos())


