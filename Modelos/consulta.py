from datetime import datetime
from Modelos.pessoa import Pessoa
from enum import Enum



class StatusConsulta(Enum):
    AGENDADA = "agendada"
    REAGENDADA = "reagendada"
    CANCELADA = "cancelada"
    FINALIZADA = "finalizada"

class Consulta:
    _id_counter = 1

    def __init__(self, medico: Pessoa, paciente: Pessoa, data_hora: datetime, motivo: str):
        self.id = Consulta._gerar_id()
        self.medico = medico
        self.paciente = paciente
        self.data_hora = data_hora
        self.motivo = motivo
        self.status = StatusConsulta.AGENDADA
        self.recepcionista = None
    
    @classmethod
    def _gerar_id(cls):
        id_atual = cls._id_counter
        cls._id_counter += 1
        return id_atual

    @property
    def medico(self):
        return self._medico

    @medico.setter
    def medico(self, valor):
        if not isinstance(valor, Pessoa):
            raise ValueError("O médico deve ser uma Pessoa válida.")
        self._medico = valor

    @property
    def paciente(self):
        return self._paciente

    @paciente.setter
    def paciente(self, valor):
        if not isinstance(valor, Pessoa):
            raise ValueError("O paciente deve ser uma Pessoa válida.")
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
    def motivo(self):
        return self._motivo

    @motivo.setter
    def motivo(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("O motivo da consulta não pode ser vazio.")
        self._motivo = valor.strip()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, valor):
        if not isinstance(valor, StatusConsulta):
            raise ValueError("Status inválido.")
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
            f"motivo='{self.motivo}', status='{self.status.value}', "
            f"recepcionista='{resp}')"
        )