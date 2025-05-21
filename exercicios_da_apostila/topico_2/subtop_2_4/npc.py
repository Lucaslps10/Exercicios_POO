################## HERANÇA ########################
from exercicios_da_apostila.topico_2.subtop_2_1.personagem import Personagem 


class NPC(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def atacar(self, alvo):
        print(f"{self.nome} não pode atacar {alvo.nome}!")

npc = NPC("Cell", 100)
p = Personagem("Jales", 100)
npc.atacar(p)
print(npc.mostrar_vida())
    
