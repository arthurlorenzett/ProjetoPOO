class Pessoa:
    def __init__(self, nome, cpf, telefone):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone

    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if valor.strip():  
            self._nome = valor
        else:
            raise ValueError("O nome não pode ser vazio.")

    
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        
        valor = valor.strip()

        if not valor:
            raise ValueError("O CPF não pode ser vazio.")

        if not valor.isdigit() or len(valor) != 11:
            raise ValueError("O CPF deve conter 11 dígitos.")

        self._cpf = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        if valor.strip():
            self._telefone = valor
        else:
            raise ValueError("O telefone não pode ser vazio.")
