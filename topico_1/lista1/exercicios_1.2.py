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
    def __init__(self):
        self.vida = 100
    
    def tomar_dano(self, dano):
        self.vida -= dano
        if dano > 0 and self.vida > 0:
            print(f"Dano: {dano} Vida restante: {self.vida}")
        else:
            print("Game Over")

pdois = PersonagemDois()
pdois.tomar_dano(10)
pdois.tomar_dano(5)
pdois.tomar_dano(10)
pdois.tomar_dano(10)
pdois.tomar_dano(65)

class Jogador:
    def __init__(self):
        self.energia = 50

    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        print(f"Aumentou {quantidade} de energia; Energia = {self.energia}")
    def usar_energia(self, quantidade):
        self.energia -= quantidade
        print(f"Energia usada: {quantidade} Restante: {self.energia}")
        if self.energia < 0:
            print("Sem energia suficiente!")

jogador = Jogador()
jogador.usar_energia(60)
jogador.recuperar_energia(20)


class Inimigo:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        

    def atacar(self, alvo):
        print(f"{self.nome} atacou!")
        alvo.tomar_dano(10)

guerreiro = PersonagemDois()
inimigo = Inimigo("Morte", 100)
inimigo.atacar(guerreiro)


        