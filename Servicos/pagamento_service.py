class Pagamento:

    def __init__(self, valor, metodo, status):
        self.valor = valor
        self.metodo = metodo
        self.status = status

    @property
    def pagamento(self):
        print(f"Valor pago {self.valor}")

    @pagamento.setter
    def pagamento (self, preco):
        if self.valor < preco:
            raise ValueError("Pagamento não realizado, falta dinheiro amigo!.")
        print("Realizando Pagamento...")
        self.valor = preco

    @property
    def metodo(self):
        print(f"Método de pagamento utilizado {self.metodo}")

    @metodo.setter
    def metodo(self):
        pass

    @property
    def status(self):
        print(f"Status do pagamento: {self.status}")

    @status.setter
    def status(self):
        pass