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

        self._recepcionista = None  

    # MÉTODOS DE NEGÓCIO

    def registrar_responsavel(self, recepcionista):
        self._recepcionista = recepcionista

    def cancelar(self, recepcionista):
        self.status = "cancelada"
        self._recepcionista = recepcionista

    def alterar_status(self, novo_status: str):
        self.status = novo_status

    def reagendar(self, nova_data_hora: datetime):
        self.data_hora = nova_data_hora
        self.status = "reagendada"

    # Validações
    
    @property
    def medico(self):
        return self._medico

    @medico.setter
    def medico(self, valor):
        if not isinstance(valor, Medico):
            raise ValueError("O médico informado é inválido.")
        self._medico = valor

    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, valor):
        if not isinstance(valor, Paciente):
            raise ValueError("O paciente informado é inválido.")
        self._paciente = valor

    @property
    def data_hora(self):
        return self._data_hora

    @data_hora.setter
    def data_hora(self, valor):
        if not isinstance(valor, datetime):
            raise ValueError("A data e hora devem ser um objeto datetime.")
        self._data_hora = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        estados_validos = ["agendada", "reagendada", "cancelada", "finalizada"]
        if valor not in estados_validos:
            raise ValueError(f"Status inválido. Use um de: {estados_validos}")
        self._status = valor

    @property
    def recepcionista(self):
        return self._recepcionista

    @recepcionista.setter
    def recepcionista(self, valor):
        if valor is not None and not hasattr(valor, "matricula"):
            raise ValueError("Recepcionista inválido.")
        self._recepcionista = valor

    def __repr__(self):
        resp = self.recepcionista.nome if self.recepcionista else "Nenhum"
        return (
            f"Consulta(id={self.id}, medico={self.medico.nome}, "
            f"paciente={self.paciente.nome}, data_hora={self.data_hora}, "
            f"status='{self.status}', recepcionista='{resp}')"
        )
