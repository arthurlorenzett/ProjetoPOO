class AgendamentoService:

    def __init__(self):
        self.consultas = []

    def agendar(self, consulta):
        for c in self.consultas:
            if c.medico == consulta.medico and c.data_hora == consulta.data_hora: #
                raise ValueError("Já existe uma consulta marcada para este médico neste horário.")
        
        self.consultas.append(consulta)

    def listar_consultas(self):
        return self.consultas
