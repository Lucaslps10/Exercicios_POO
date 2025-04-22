class Carro:
    def __init__(self, modelo, ano, cor, preco):
        self.modelo = modelo
        self.ano = ano 
        self.cor = cor
        self.preco = preco

carro1 = Carro("Palio", 2022, "Vermelho", 15000)
print(carro1.modelo)
print(carro1.ano)
print(carro1.cor)
print(carro1.preco)