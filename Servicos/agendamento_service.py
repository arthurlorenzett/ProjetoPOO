class Agendamento:

    def __init__(self):
        self._consultas = []

    def adicionar_consulta(self, consulta):

        for c in self._consultas:
            if (c.medico == consulta.medico and
                c.data == consulta.data and
                c.hora == consulta.hora):
                raise ValueError("Já existe uma consulta marcada para este médico neste horário.")

        self._consultas.append(consulta)

    def listar_consultas(self):
        return self._consultas
