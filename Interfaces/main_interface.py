import tkinter as tk

from Interfaces.cadastro_interface import abrir_tela_cadastro
from Interfaces.agendamento_interface import abrir_tela_agendamento
from Interfaces.cancelamento_interface import abrir_tela_cancelamento
from Interfaces.exibir_dados_interface import abrir_tela_exibir_dados
from Interfaces.pagamento_interface import abrir_tela_pagamento

# Serviços
from Servicos.agendamento_service import AgendamentoService


def iniciar_interface():
    janela = tk.Tk()
    janela.title("Sistema da Clínica")
    janela.geometry("400x350")
    janela.resizable(False, False)

    # "Bancos de dados" locais
    pacientes = {}
    medicos = {}
    recepcionistas = {}
    consultas = []
    pagamentos = []

    # Serviço de agendamento
    agendamento_service = AgendamentoService()

    tk.Label(
        janela,
        text="SISTEMA DA CLÍNICA",
        font=("Arial", 16, "bold")
    ).pack(pady=20)

    # ----------- BOTÃO: CADASTRO -----------
    tk.Button(
        janela,
        text="Cadastrar Usuário",
        font=("Arial", 12),
        bg="#2196F3",
        fg="white",
        width=25,
        command=lambda: abrir_tela_cadastro(
            janela,
            pacientes,
            medicos,
            recepcionistas
        )
    ).pack(pady=10)

    # ----------- BOTÃO: AGENDAMENTO -----------
    tk.Button(
        janela,
        text="Agendar Consulta",
        font=("Arial", 12),
        bg="#4CAF50",
        fg="white",
        width=25,
        command=lambda: abrir_tela_agendamento(
            janela,
            agendamento_service,
            pacientes,
            medicos,
            consultas,
            recepcionistas
        )
    ).pack(pady=10)

    # ----------- BOTÃO: CANCELAMENTO -----------
    tk.Button(
        janela,
        text="Cancelar Consulta",
        font=("Arial", 12),
        bg="#F44336",
        fg="white",
        width=25,
        command=lambda: abrir_tela_cancelamento(
            janela,
            consultas
        )
    ).pack(pady=10)

    # ----------- BOTÃO: EXIBIR DADOS -----------
    tk.Button(
    janela,
    text="Exibir Dados",
    font=("Arial", 12),
    bg="#9C27B0",
    fg="white",
    width=25,
    command=lambda: abrir_tela_exibir_dados(
        janela,
        pacientes,
        medicos,
        recepcionistas,
        consultas
    )
    ).pack(pady=10)

    # ----------- BOTÃO: PAGAMENTO -----------
    tk.Button(
    janela,
    text="Pagamento",
    font=("Arial", 12),
    bg="#FF9800",
    fg="white",
    width=25,
    command=lambda: abrir_tela_pagamento(
        janela,
        pagamentos
    )
).pack(pady=10)



    janela.mainloop()
