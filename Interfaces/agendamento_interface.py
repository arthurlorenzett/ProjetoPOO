import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from Modelos.consulta import Consulta

def abrir_tela_agendamento(janela_principal, agendamento_service, pacientes, medicos, consultas_agendadas, recepcionistas):

    janela_agendamento = tk.Toplevel(janela_principal)
    janela_agendamento.title("Agendar Consulta")
    janela_agendamento.geometry("350x400")

    # Campos
    tk.Label(janela_agendamento, text="CPF do recepcionista:").pack()
    entry_cpf_recepc = tk.Entry(janela_agendamento)
    entry_cpf_recepc.pack()

    tk.Label(janela_agendamento, text="CPF do paciente:").pack()
    entry_cpf_paciente = tk.Entry(janela_agendamento)
    entry_cpf_paciente.pack()

    tk.Label(janela_agendamento, text="CPF do médico:").pack()
    entry_cpf_medico = tk.Entry(janela_agendamento)
    entry_cpf_medico.pack()

    tk.Label(janela_agendamento, text="Data (AAAA-MM-DD):").pack()
    entry_data = tk.Entry(janela_agendamento)
    entry_data.pack()

    tk.Label(janela_agendamento, text="Hora (HH:MM):").pack()
    entry_hora = tk.Entry(janela_agendamento)
    entry_hora.pack()

    # Função agendar
    def agendar():
        cpf_recepc = entry_cpf_recepc.get()
        cpf_paciente = entry_cpf_paciente.get()
        cpf_medico = entry_cpf_medico.get()
        data_txt = entry_data.get()
        hora_txt = entry_hora.get()

        # validações
        if cpf_recepc not in recepcionistas:
            messagebox.showerror("Erro", "Recepcionista não encontrada.")
            return

        if cpf_paciente not in pacientes:
            messagebox.showerror("Erro", "Paciente não encontrado.")
            return
        
        if cpf_medico not in medicos:
            messagebox.showerror("Erro", "Médico não encontrado.")
            return

        try:
            data_hora = datetime.strptime(f"{data_txt} {hora_txt}", "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Erro", "Formato inválido de data ou hora.")
            return

        consulta = Consulta(
            medico=medicos[cpf_medico],
            paciente=pacientes[cpf_paciente],
            data_hora=data_hora
        )

        # REGISTRA RESPONSÁVEL
        consulta.registrar_responsavel(recepcionistas[cpf_recepc])

        try:
            agendamento_service.agendar(consulta)
            consultas_agendadas.append(consulta)
            messagebox.showinfo("Sucesso", "Consulta agendada com sucesso!")
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))

    tk.Button(janela_agendamento, text="Agendar", bg="lightgreen", command=agendar).pack(pady=10)
