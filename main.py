from Modelos.medico import Medico
from Modelos.paciente import Paciente
from Modelos.consulta import Consulta
from Modelos.pagamento import Pagamento
from Modelos.recepcionista import Recepcionista

from Servicos.agendamento_service import AgendamentoService
from Servicos.pagamento_service import PagamentoService


agendamento_service = AgendamentoService()
pagamento_service = PagamentoService()


def menu():
    while True:
        print("\n------ MENU ------")
        print("1. AGENDAR CONSULTA")
        print("2. PAGAMENTO")
        print("3. CADASTRO")
        print("4. SAIR")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            menu_agendar()

        elif opcao == "2":
            menu_pagamento()

        elif opcao == "3":
            menu_cadastro()

        elif opcao == "4":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.\n")


# -------------------------
# 1) MENU DE AGENDAMENTO
# -------------------------

def menu_agendar():
    print("\n--- AGENDAR CONSULTA ---")

    nome_paciente = input("Nome do paciente: ")
    cpf_paciente = input("CPF: ")
    telefone = input("Telefone: ")
    historico = input("Histórico médico: ")

    paciente = Paciente(nome_paciente, cpf_paciente, telefone, historico)

    nome_medico = input("\nNome do médico: ")
    cpf_medico = input("CPF do médico: ")
    telefone_medico = input("Telefone do médico: ")
    crm = input("CRM: ")
    especialidade = input("Especialidade: ")

    medico = Medico(nome_medico, cpf_medico, telefone_medico, crm, especialidade)


    data = input("Data da consulta (YYYY-MM-DD): ")
    hora = input("Hora da consulta (HH:MM): ")

    consulta = Consulta(data, hora, medico, paciente)

    try:
        agendamento_service.agendar(consulta)
        print("Consulta agendada com sucesso!")

    except ValueError as erro:
        print(f"Erro ao agendar: {erro}")


# -------------------------
# 2) MENU DE PAGAMENTO
# -------------------------

def menu_pagamento():
    print("\n--- PAGAMENTO ---")

    valor = float(input("Valor disponível para pagamento: R$ "))
    metodo = input("Método de pagamento (pix/cartao/dinheiro): ").lower()
    total = float(input("Valor da consulta: R$ "))

    pagamento = Pagamento(valor, metodo)

    try:
        pagamento_service.realizar_pagamento(pagamento, total)
    except ValueError as erro:
        print(f"Erro: {erro}")


# -------------------------
# 3) MENU DE CADASTRO
# -------------------------

def menu_cadastro():
    print("\n--- CADASTRAR USUÁRIO ---")
    print("1. Paciente")
    print("2. Médico")
    print("3. Recepcionista")

    opcao = input("Escolha o tipo de usuário: ")

    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")

    if opcao == "1":
        historico = input("Histórico médico: ")
        pessoa = Paciente(nome, cpf, telefone, historico)

    elif opcao == "2":
        crm = input("CRM: ")
        especialidade = input("Especialidade: ")
        pessoa = Medico(nome, cpf, telefone, crm, especialidade)

    elif opcao == "3":
        matricula = input("Matrícula: ")
        pessoa = Recepcionista(nome, cpf, telefone, matricula)

    else:
        print("Opção inválida!")
        return

    print("\nCadastro concluído!")
    pessoa.exibir_dados()


# -------------------------
# EXECUTAR SISTEMA
# -------------------------

if __name__ == "__main__":
    menu()
