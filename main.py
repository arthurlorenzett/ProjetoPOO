from datetime import datetime

from Modelos.medico import Medico
from Modelos.paciente import Paciente
from Modelos.consulta import Consulta
from Modelos.pagamento import Pagamento
from Modelos.recepcionista import Recepcionista

from Servicos.agendamento_service import AgendamentoService
from Servicos.pagamento_service import PagamentoService


# -----------------------------
# INSTÂNCIAS DOS SERVIÇOS
# -----------------------------
agendamento_service = AgendamentoService()
pagamento_service = PagamentoService()

# -----------------------------
# "BANCO DE DADOS"
# -----------------------------
pacientes = {}
medicos = {}
recepcionistas = {}
consultas_agendadas = []  


# -----------------------------
# MENU PRINCIPAL
# -----------------------------
def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1. Agendar consulta")
        print("2. Pagamento")
        print("3. Cadastro")
        print("4. Exibir todos os dados")
        print("5. Sair")
        print("=============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_agendar()

        elif opcao == "2":
            menu_pagamento()

        elif opcao == "3":
            menu_cadastro()

        elif opcao == "4":
            menu_exibir_todos()

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida.\n")

# ----------------------------------------
# ESCOLHER RECEPCIONISTA
# ----------------------------------------
def escolher_recepcionista():
    if not recepcionistas:
        print("Nenhum recepcionista cadastrado!")
        return None

    print("\n--- RECEPCIONISTAS DISPONÍVEIS ---")
    for r in recepcionistas.values():
        print(f"- {r._nome} | CPF: {r._cpf} | Matrícula: {r._matricula}")

    cpf = input("Digite o cpf do recepcionista: ")

    if cpf not in recepcionistas:
        print("Recepcionista não encontrado!")
        return None

    return recepcionistas[cpf] 
# ----------------------------------------
# 1) AGENDAMENTO DE CONSULTA
# ----------------------------------------
def menu_agendar():
    print("\n--- AGENDAR CONSULTA ---")
    recepcionista = escolher_recepcionista()
    if recepcionista is None:
        return
    print(f"\nRecepcionista selecionado: {recepcionista._nome}")

    cpf_paciente = input("CPF do paciente: ")
    if cpf_paciente not in pacientes:
        print("Paciente não encontrado! Cadastre antes.")
        return
    paciente = pacientes[cpf_paciente]

    cpf_medico = input("CPF do médico: ")
    if cpf_medico not in medicos:
        print("Médico não encontrado! Cadastre antes.")
        return
    medico = medicos[cpf_medico]

    data = input("Data da consulta (AAAA-MM-DD): ")
    hora = input("Hora da consulta (HH:MM): ")

    try:
        data_hora = datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Data ou hora inválida!")
        return

    consulta = Consulta(medico, paciente, data_hora)

    try:
        agendamento_service.agendar(consulta)   # valida conflito
        consultas_agendadas.append(consulta)    # guarda também no main
        print("\nConsulta agendada com sucesso!")
        print(consulta)

    except ValueError as erro:
        print(f"Erro ao agendar: {erro}")


# ----------------------------------------
# 2) PAGAMENTO
# ----------------------------------------
def menu_pagamento():
    print("\n--- PAGAMENTO ---")

    valor = float(input("Valor disponível: R$ "))
    metodo = input("Método (pix/cartao/dinheiro): ")
    total = float(input("Valor da consulta: R$ "))

    pagamento = Pagamento(valor, metodo)

    try:
        pagamento_service.realizar_pagamento(pagamento, total)
    except ValueError as erro:
        print(f"Erro: {erro}")


# ----------------------------------------
# 3) CADASTRO
# ----------------------------------------
def menu_cadastro():
    print("\n--- CADASTRO ---")
    print("1. Paciente")
    print("2. Médico")
    print("3. Recepcionista")

    opcao = input("Escolha: ")

    nome = input("Nome: ")
    cpf = input("CPF: ")
    telefone = input("Telefone: ")

    # Paciente
    if opcao == "1":
        historico = input("Histórico médico: ")
        pessoa = Paciente(nome, cpf, telefone, historico)
        pacientes[cpf] = pessoa
        print("Paciente cadastrado!")

    # Médico
    elif opcao == "2":
        crm = input("CRM: ")
        especialidade = input("Especialidade: ")
        pessoa = Medico(nome, cpf, telefone, crm, especialidade)
        medicos[cpf] = pessoa
        print("Médico cadastrado!")

    # Recepcionista
    elif opcao == "3":
        matricula = input("Matrícula: ")
        pessoa = Recepcionista(nome, cpf, telefone, matricula)
        recepcionistas[cpf] = pessoa
        print("Recepcionista cadastrado!")

    else:
        print("Opção inválida!")
        return

    pessoa.exibir_dados()


# ----------------------------------------
# 4) EXIBIR TODOS OS DADOS
# ----------------------------------------
def menu_exibir_todos():
    print("\n====================")
    print(" PACIENTES CADASTRADOS")
    print("====================")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
    else:
        for p in pacientes.values():
            p.exibir_dados()
            print("--------------------")

    print("\n====================")
    print(" MÉDICOS CADASTRADOS")
    print("====================")
    if not medicos:
        print("Nenhum médico cadastrado.")
    else:
        for m in medicos.values():
            m.exibir_dados()
            print("--------------------")

    print("\n====================")
    print(" RECEPCIONISTAS CADASTRADOS")
    print("====================")
    if not recepcionistas:
        print("Nenhum recepcionista cadastrado.")
    else:
        for r in recepcionistas.values():
            r.exibir_dados()
            print("--------------------")

    print("\n====================")
    print(" CONSULTAS AGENDADAS")
    print("====================")
    if not consultas_agendadas:
        print("Nenhuma consulta agendada.")
    else:
        for c in consultas_agendadas:
            print(c)
            print("--------------------")


    


# ----------------------------------------
# EXECUÇÃO
# ----------------------------------------
if __name__ == "__main__":
    menu()
