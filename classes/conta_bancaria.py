class ContaBancaria:
    def __init__(self, usuario, senha, saldo):
        self.usuario = usuario
        self.senha = senha
        self.saldo = saldo

conta1 = ContaBancaria("lucas123", "12345", 500.00)
print(conta1.usuario)
print(conta1.senha)
print(conta1.saldo)        