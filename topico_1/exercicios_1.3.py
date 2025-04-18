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
        print(f"{self.nome} atacou e causou {dano} de dano!")
        alvo.tomar_dano(dano)

class Inimigo:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nome} foi derrotado!")
            return True
        else:
            print(f"{self.nome} tem {self.vida} de vida restante!")
            return False

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
        self.pontuacao = Pontuacao()

    def atacar(self, inimigo):
        if self.energia < 10:
            print("Energia insuficiente para atacar, descanse primeito...")
            self.descansar()
            return 
        dano = random.randint(5, 20)
        print(f"Jogador atacou {inimigo.nome} e causou {dano} de dano!")

        self.energia -= 10
        print(f"Energia restante: {self.energia}")

        derrotado = inimigo.tomar_dano(dano)
        if derrotado:
            self.pontuacao.adicionar_pontos(10)
        
    def descansar(self):
        if self.energia + 20 > 100:
            recuperado = 100 - self.energia
        else:
            recuperado = 20
        self.energia += recuperado
        print(f"Jogador descansou e recuperou {recuperado} de energia. Energia atual: {self.energia}")

class Pontuacao:
    def __init__(self):
        self.pontos = 0

    def adicionar_pontos(self, valor):
        self.pontos += valor
        print(f"Você tem {self.pontos} pontos!")
        
jogador = Jogador()
inimigos = [Inimigo("Bárbaro", 100), Inimigo("Giagante", 100), Inimigo("Bruxa", 100)]

"""
for inimigo in inimigos:
    print(f"\nLutando contra {inimigo.nome}")
    while inimigo.vida > 0:
        jogador.atacar(inimigo)

print(f"\nJogo encerrado. Pontuação final: {jogador.pontuacao.pontos}")
"""




