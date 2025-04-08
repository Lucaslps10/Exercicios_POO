import random;
class PersonagemDois:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
    
    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado")

        else:
            print(f"{self.nome} tem {self.vida} de vida restante!")

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
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"{self.nome} tem {self.vida} de vida restante!")

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        print(f"{self.nome} atacou e causou {dano} de dano!")
        alvo.tomar_dano(dano)
  
guerreiro = PersonagemDois("Guerreiro", 100)
inimigo = Inimigo("Inimigo", 100)

turno = 1

"""
print("O combate começou!")
while guerreiro.vida > 0 and inimigo.vida > 0:
    print(f"/n--- Turno {turno} ---")
    guerreiro.atacar(inimigo)
    if inimigo.vida <= 0:
        print("PersonagemDois venceu a batalha!")
        break

    inimigo.atacar(guerreiro)
    if guerreiro.vida <= 0:
        print("O inimigo venceu a batalha!")
        break
    
    turno += 1
"""




class Jogador:
    def __init__(self):
        self.energia = 100
        self.pontos = 0

    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        print(f"Aumentou {quantidade} de energia; Energia = {self.energia}")
    def usar_energia(self, quantidade):
        self.energia -= quantidade
        print(f"Energia usada: {quantidade} Restante: {self.energia}")
        if self.energia < 0:
            print("Sem energia suficiente!")

class Pontuacao:
    def __init__(self, pontos):
        self.pontos = pontos

    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
        print(f"Você ganhou {quantidade} pontos!")
        
    def mostrar_pontos(self):
        print(f"Pontuação atual: {self.pontos}")


