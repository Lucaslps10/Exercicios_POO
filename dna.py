class Dna:
    def __init__(self, teste_generico, paternidade, maternidade, valor):
        self.teste_generico = teste_generico
        self.paternidade = paternidade
        self.maternidade = maternidade
        self.valor = valor

dna1 = Dna("Identifica alterações genéticas", "Verifica se há vínculo genético", "Verifica se há vínculo genético", "Valor")
print(dna1.teste_generico)
print(dna1.paternidade)
print(dna1.maternidade)
print(dna1.valor)