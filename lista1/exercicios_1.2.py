class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def dizer_nome(self):
        print(f"Meu nome é {self.nome}!")

p = Personagem("Lucas")
p.dizer_nome()


class Pontuacao:
    def __init__(self, pontos):
        self.pontos = pontos

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
        print(f"Você ganhou {quantidade} pontos!")
        
    def mostrar_pontos(self):
        print(f"Pontuação atual: {self.pontos}")

pontuacao = Pontuacao(0)
pontuacao.adicionar_pontos(50)
pontuacao.mostrar_pontos()

class PersonagemDois:
    def __init__(self, vida):
        self.vida = vida
    
    def tomar_dano(self, dano):
        if dano > 0:
            self.vida -= dano
            print(self.vida)
        if self.vida == 0:
            print("Game Over")

pdois = PersonagemDois(100)
pdois.tomar_dano(10)

