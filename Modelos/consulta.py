from datetime import datetime
from Modelos.medico import Medico
from Modelos.paciente import Paciente


class Consulta:
    _id_counter = 1

    def __init__(self, medico: Medico, paciente: Paciente, data_hora: datetime, status: str = "agendada"):
        self.id = Consulta._id_counter
        Consulta._id_counter += 1

        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora
        self.status = status

        self.recepcionista = None  

    def registrar_responsavel(self, recepcionista):
        self.recepcionista = recepcionista

    def cancelar(self, recepcionista):
        self.status = "cancelada"
        self.recepcionista = recepcionista

    def alterar_status(self, novo_status: str):
        self.status = novo_status

    def reagendar(self, nova_data_hora: datetime):
        self.data_hora = nova_data_hora
        self.status = "reagendada"

    def __repr__(self):
        resp = self.recepcionista.nome if self.recepcionista else "Nenhum"
        return (
            f"Consulta(id={self.id}, medico={self.medico.nome}, "
            f"paciente={self.paciente.nome}, data_hora={self.data_hora}, "
            f"status='{self.status}', recepcionista='{resp}')"
        )