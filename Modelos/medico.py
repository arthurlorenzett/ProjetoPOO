from pessoa import Pessoa

class Medico(Pessoa):
    def __init__(self, nome, cpf, telefone, crm, especialidade):
        super().__init__(nome, cpf, telefone)
        self._crm = crm
        self_especialidade = especialidade
    
    @property
    def crm(self):
        return self._crm

    @crm.setter
    def crm(self, novo_crm):
        if not novo_crm:
            raise ValueError("CRM não pode ser vazio.")
        if len(novo_crm) < 6:
            raise ValueError("CRM inválido.")
        self._crm = novo_crm
    
    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, nova_especialidade):
        if not nova_especialidade:
            raise ValueError("Especialidade não pode ser vazia")
    
    def exibir_dados(self):
        return super().exibir_dados()
        print(f"CRM: {self.crm}")
        print(f"Especialidade: {self.especialidade}")