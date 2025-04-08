import random;
class PersonagemDois:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print("Game Over")

        else:
            print(f"Dano: {dano} Vida restante: {self.vida}")

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        print(f"Personagem atacou e causou {dano} de dano!")
        alvo.tomar_dano(dano)

class Inimigo:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida >= 0:
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"Dano: {dano} Vida restante: {self.vida}")

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou e causou {dano} de dano!")
        alvo.tomar_dano(dano)
  

    
        

