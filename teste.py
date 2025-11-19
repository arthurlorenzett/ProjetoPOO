"""
ARQUIVO DE TESTES AUTOMÁTICOS DO SISTEMA DE CLÍNICA
Testa todas as funções principais sem interação do usuário.
"""

from datetime import datetime

from Modelos.paciente import Paciente
from Modelos.medico import Medico
from Modelos.recepcionista import Recepcionista
from Modelos.consulta import Consulta
from Modelos.pagamento import Pagamento

from Servicos.agendamento_service import AgendamentoService
from Servicos.pagamento_service import PagamentoService


def testar_cadastro():
    print("\n=== TESTE: CADASTRO ===")

    # Paciente
    p = Paciente("Arthur", "09743528962", "999999999", "Falência nos rins")
    assert p.nome == "Arthur"
    assert p.cpf == "09743528962"
    print("✓ Cadastro de paciente OK")

    # Médico
    m = Medico("Rodolfo", "09743528999", "99991111", "123456-SC", "Oftalmo")
    assert m.crm == "123456-SC"
    assert m.especialidade == "Oftalmo"
    print("✓ Cadastro de médico OK")

    # Recepcionista
    r = Recepcionista("Eliane", "12345678915", "11112222", "12345")
    assert r.matricula == "12345"
    print("✓ Cadastro de recepcionista OK")

    return p, m, r


def testar_agendamento(paciente, medico):
    print("\n=== TESTE: AGENDAMENTO ===")

    agendamento = AgendamentoService()

    data_hora = datetime(2025, 11, 24, 7, 30)
    consulta = Consulta(medico, paciente, data_hora)

    # Primeiro agendamento deve funcionar
    agendamento.agendar(consulta)
    assert len(agendamento.listar_consultas()) == 1
    print("✓ Agendamento simples OK")

    # Tentar agendar no mesmo horário deve dar erro
    try:
        consulta2 = Consulta(medico, paciente, data_hora)
        agendamento.agendar(consulta2)
        assert False, "Erro esperado não ocorreu!"
    except ValueError:
        print("✓ Validação de conflito OK")

    return consulta


def testar_pagamento():
    print("\n=== TESTE: PAGAMENTO ===")

    servico_pagamento = PagamentoService()
    pagamento = Pagamento(valor=300, metodo="pix")

    # Pagamento OK
    servico_pagamento.realizar_pagamento(pagamento, 200)
    assert pagamento.status == "pago"
    print("✓ Pagamento OK")

    # Tentar pagar sem saldo deve falhar
    pagamento2 = Pagamento(valor=50, metodo="pix")
    try:
        servico_pagamento.realizar_pagamento(pagamento2, 200)
        assert False, "Erro esperado não ocorreu!"
    except ValueError:
        print("✓ Validação de saldo insuficiente OK")


def testar_exibicao(paciente, medico, recepcionista, consulta):
    print("\n=== TESTE: EXIBIÇÃO ===")
    # Apenas verificar que os métodos não quebram
    paciente.exibir_dados()
    medico.exibir_dados()
    recepcionista.exibir_dados()
    print(consulta)
    print("✓ Exibição funcionando")


# ============================================================
# EXECUTAR TODOS OS TESTES
# ============================================================
if __name__ == "__main__":
    print("\n======================================")
    print("      INICIANDO TESTES DO SISTEMA     ")
    print("======================================")

    p, m, r = testar_cadastro()
    c = testar_agendamento(p, m)
    testar_pagamento()
    testar_exibicao(p, m, r, c)

    print("\n======================================")
    print("  TODOS OS TESTES FORAM EXECUTADOS!   ")
    print("======================================")
