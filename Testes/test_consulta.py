import unittest
from datetime import datetime

from Modelos.pessoa import Pessoa
from Modelos.medico import Medico
from Modelos.paciente import Paciente
from Modelos.consulta import Consulta, StatusConsulta


class PessoaFake(Pessoa):
    """Classe concreta só para testar Pessoa (pois é abstrata)"""
    pass


class TestModelos(unittest.TestCase):

    # ------------------------
    # PESSOA
    # ------------------------
    def test_pessoa_getters(self):
        p = PessoaFake("Nome", "12345678901", "999")

        self.assertEqual(p.nome, "Nome")
        self.assertEqual(p.cpf, "12345678901")
        self.assertEqual(p.telefone, "999")

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            PessoaFake("", "12345678901", "999999")

    def test_cpf_invalido(self):
        with self.assertRaises(ValueError):
            PessoaFake("Nome", "123", "999999")

    def test_telefone_vazio(self):
        with self.assertRaises(ValueError):
            PessoaFake("Nome", "12345678901", "")
    
    def test_exibir_dados(self):
        p = PessoaFake("Nome", "12345678901", "999")
        p.exibir_dados()

    # ------------------------
    # MEDICO
    # ------------------------

    def test_medico_valido(self):
        medico = Medico("Dr", "12345678901", "999", "123456", "Cardio")

        self.assertEqual(medico.crm, "123456")
        self.assertEqual(medico.especialidade, "Cardio")

    def test_crm_invalido(self):
        with self.assertRaises(ValueError):
            Medico("Dr", "12345678901", "999", "123", "Cardio")

    def test_especialidade_vazia(self):
        medico = Medico("Dr", "12345678901", "999", "123456", "Cardio")

        with self.assertRaises(ValueError):
            medico.especialidade = ""

    # ------------------------
    # PACIENTE
    # ------------------------
    def test_paciente_valido(self):
        paciente = Paciente("Maria", "12345678901", "999", "Histórico")

        self.assertEqual(paciente.historico_medico, "Histórico")

    def test_historico_vazio(self):
        paciente = Paciente("Maria", "12345678901", "999", "ok")

        with self.assertRaises(ValueError):
            paciente.historico_medico = ""
    
    # ------------------------
    # RECEPCIONISTA
    # ------------------------
    def test_recepcionista_valido(self):
        medico = Medico("Dr", "12345678901", "999", "123456", "Cardio")
        paciente = Paciente("Maria", "12345678901", "999", "ok")

        consulta = Consulta(medico, paciente, datetime.now(), "Motivo")
        class R:
            matricula = "123"
            nome = "Atendente"

        consulta.recepcionista = R()

        self.assertEqual(consulta.recepcionista.nome, "Atendente")

    def test_recepcionista_invalido(self):
        medico = Medico("Dr", "12345678901", "999", "123456", "Cardio")
        paciente = Paciente("Maria", "12345678901", "999", "ok")

        consulta = Consulta(medico, paciente, datetime.now(), "Motivo")

        class R:
            pass

        with self.assertRaises(ValueError):
            consulta.recepcionista = R()
    # ------------------------
    # CONSULTA (validações)
    # ------------------------

    def test_medico_invalido(self):
        paciente = Paciente("Maria", "12345678901", "999", "ok")

        with self.assertRaises(ValueError):
            Consulta("invalido", paciente, datetime.now(), "Motivo")

    def test_paciente_invalido(self):
        medico = Medico("Dr", "12345678901", "999", "123456", "Cardio")

        with self.assertRaises(ValueError):
            Consulta(medico, "invalido", datetime.now(), "Motivo")

    def test_data_invalida(self):
        medico = Medico("Dr", "12345678901", "999", "123456", "Cardio")
        paciente = Paciente("Maria", "12345678901", "999", "ok")

        with self.assertRaises(ValueError):
            Consulta(medico, paciente, "data errada", "Motivo")

    def test_status_invalido(self):
        medico = Medico("Dr", "12345678901", "999", "123456", "Cardio")
        paciente = Paciente("Maria", "12345678901", "999", "ok")

        consulta = Consulta(medico, paciente, datetime.now(), "Motivo")

        with self.assertRaises(ValueError):
            consulta.status = "qualquer coisa"

    def test_motivo_vazio(self):
        medico = Medico("Dr", "12345678901", "999", "123456", "Cardio")
        paciente = Paciente("Maria", "12345678901", "999", "ok")

        with self.assertRaises(ValueError):
            Consulta(medico, paciente, datetime.now(), "")

    # ------------------------
    # CONSULTA (validações)
    # ------------------------
    def test_repr(self):
        medico = Medico("Dr", "12345678901", "999", "123456", "Cardio")
        paciente = Paciente("Maria", "12345678901", "999", "ok")

        consulta = Consulta(medico, paciente, datetime.now(), "Motivo")

        texto = repr(consulta)
        self.assertIn("Consulta", texto)
        self.assertIn("Dr", texto)

if __name__ == "__main__":
    unittest.main()