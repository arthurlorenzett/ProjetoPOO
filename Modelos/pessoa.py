from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, cpf, telefone):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone

    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        if novo_nome.strip():  
            self._nome = novo_nome
        else:
            raise ValueError("O nome não pode ser vazio.")

    
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        
        novo_cpf = novo_cpf.strip()

        if not novo_cpf:
            raise ValueError("O CPF não pode ser vazio.")

        if not novo_cpf.isdigit() or len(novo_cpf) != 11:
            raise ValueError("O CPF deve conter 11 dígitos.")

        self._cpf = novo_cpf

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if novo_telefone.strip():
            self._telefone = novo_telefone
        else:
            raise ValueError("O telefone não pode ser vazio.")
    
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}")
