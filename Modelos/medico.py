from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, cpf, telefone, crm, especialidade):
        super().__init__(nome, cpf, telefone)
        self._crm = crm
        self_especialidade = especialidade
    
    @property
    def especialidade(self):
        return self._crm

    @especialidade.setter
    def especialidade(self, valor):
        if not valor:
            raise ValueError("CRM não pode ser vazio.")
        if len(valor) < 6:
            raise ValueError("CRM inválido.")
        self._crm = valor
    
    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, valor):
        if not valor:
            raise ValueError("Especialidade não pode ser vazia")
    
    def exibir_dados(self):
        return super().exibir_dados()
        print(f"CRM: {self.crm}")
        print(f"Especialidade: {self.especialidade}")