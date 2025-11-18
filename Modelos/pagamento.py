class Pagamento:
    def __init__(self, valor, metodo, status="pendente"):
        self._valor = valor
        self._metodo = metodo
        self._status = status

    # ----- PROPRIEDADES -----

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("O valor não pode ser negativo.")
        self._valor = novo_valor

    @property
    def metodo(self):
        return self._metodo

    @metodo.setter
    def metodo(self, novo_metodo):
        if novo_metodo not in ["pix", "cartao", "dinheiro"]:
            raise ValueError("Método de pagamento inválido.")
        self._metodo = novo_metodo

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        if novo_status not in ["pendente", "pago", "cancelado"]:
            raise ValueError("Status inválido.")
        self._status = novo_status
