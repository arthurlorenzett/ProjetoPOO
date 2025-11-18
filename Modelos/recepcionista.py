from Modelos.pessoa import Pessoa
from Modelos.consulta import Consulta

class Recepcionista(Pessoa):
    def __init__(self, nome, cpf, telefone, matricula):
        super().__init__(nome, cpf, telefone)
        self._matricula = matricula
        self._consultas = []

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Matrícula: {self._matricula}")

    def agendar_consulta(self, consulta: Consulta):
        self._consultas.append(consulta)

    def cancelar_consulta(self, consulta_id: int):
        for c in self._consultas:
            if c.id == consulta_id:
                c.alterar_status("cancelada")
                return True
        return False

    def listar_consultas(self):
        return self._consultas

    def __repr__(self):
        return (
            f"Recepcionista(nome='{self._nome}', "
            f"matricula='{self._matricula}')"
        )