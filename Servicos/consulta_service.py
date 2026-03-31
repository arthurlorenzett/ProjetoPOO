from datetime import datetime
from Modelos.consulta import Consulta, StatusConsulta


class ConsultaService:

    def cancelar(self, consulta: Consulta, recepcionista):
        consulta.status = StatusConsulta.CANCELADA
        consulta.recepcionista = recepcionista

    def reagendar(self, consulta: Consulta, nova_data: datetime):
        if nova_data <= consulta.data_hora:
            raise ValueError("A nova data deve ser futura.")
        
        consulta.data_hora = nova_data
        consulta.status = StatusConsulta.REAGENDADA

    def finalizar(self, consulta: Consulta):
        consulta.status = StatusConsulta.FINALIZADA