from Modelos.pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, cpf, telefone, historico_medico):
        super().__init__(nome, cpf, telefone)
        self._historico_medico = historico_medico

    @property 
    def historico_medico(self):
        return self._historico_medico
    
    @historico_medico.setter
    def historico_medico(self, novo_historico):
        if not novo_historico:
            raise ValueError("Historico não pode ser vazio")

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Histórico Médico: {self._historico_medico}")