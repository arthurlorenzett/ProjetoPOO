import tkinter as tk
from tkinter import messagebox, scrolledtext


def abrir_tela_exibir_dados(janela_principal, pacientes, medicos, recepcionistas, consultas, pagamentos):
    janela = tk.Toplevel(janela_principal)
    janela.title("Exibir Dados")
    janela.geometry("500x500")

    tk.Label(janela, text="Escolha o que deseja exibir:", font=("Arial", 12, "bold")).pack(pady=10)

    opcao_var = tk.StringVar()
    opcao_var.set("Pacientes")

    opcoes = ["Pacientes", "Médicos", "Recepcionistas", "Consultas", "Pagamentos"]

    menu = tk.OptionMenu(janela, opcao_var, *opcoes)
    menu.pack(pady=10)

    # Área de texto rolável
    caixa_texto = scrolledtext.ScrolledText(janela, width=60, height=20)
    caixa_texto.pack(pady=10)
    caixa_texto.config(state="disabled")  # impede edição

    def exibir():
        caixa_texto.config(state="normal")
        caixa_texto.delete("1.0", tk.END)
        escolha = opcao_var.get()

        if escolha == "Pacientes":
            if not pacientes:
                caixa_texto.insert(tk.END, "Nenhum paciente cadastrado.")
            else:
                for p in pacientes.values():
                    caixa_texto.insert(tk.END, f"Nome: {p.nome}\n")
                    caixa_texto.insert(tk.END, f"CPF: {p.cpf}\n")
                    caixa_texto.insert(tk.END, f"Telefone: {p.telefone}\n")
                    caixa_texto.insert(tk.END, f"Histórico médico: {p.historico_medico}\n")
                    caixa_texto.insert(tk.END, "-"*40 + "\n")

        elif escolha == "Médicos":
            if not medicos:
                caixa_texto.insert(tk.END, "Nenhum médico cadastrado.")
            else:
                for m in medicos.values():
                    caixa_texto.insert(tk.END, f"Nome: {m.nome}\n")
                    caixa_texto.insert(tk.END, f"CPF: {m.cpf}\n")
                    caixa_texto.insert(tk.END, f"Telefone: {m.telefone}\n")
                    caixa_texto.insert(tk.END, f"CRM: {m.crm}\n")
                    caixa_texto.insert(tk.END, f"Especialidade: {m.especialidade}\n")
                    caixa_texto.insert(tk.END, "-"*40 + "\n")

        elif escolha == "Recepcionistas":
            if not recepcionistas:
                caixa_texto.insert(tk.END, "Nenhum recepcionista cadastrado.")
            else:
                for r in recepcionistas.values():
                    caixa_texto.insert(tk.END, f"Nome: {r.nome}\n")
                    caixa_texto.insert(tk.END, f"CPF: {r.cpf}\n")
                    caixa_texto.insert(tk.END, f"Telefone: {r.telefone}\n")
                    caixa_texto.insert(tk.END, f"Matrícula: {r.matricula}\n")
                    caixa_texto.insert(tk.END, "-"*40 + "\n")

        elif escolha == "Consultas":
            if not consultas:
                caixa_texto.insert(tk.END, "Nenhuma consulta agendada.")
            else:
                for c in consultas:
                    caixa_texto.insert(tk.END, f"ID: {c.id}\n")
                    caixa_texto.insert(tk.END, f"Médico: {c.medico.nome}\n")
                    caixa_texto.insert(tk.END, f"Paciente: {c.paciente.nome}\n")
                    caixa_texto.insert(tk.END, f"Motivo: {c.motivo}\n")
                    caixa_texto.insert(tk.END, f"Data e hora: {c.data_hora}\n")
                    caixa_texto.insert(tk.END, f"Status: {c.status}\n")
                    resp = c.recepcionista.nome if c.recepcionista else "Nenhum"
                    caixa_texto.insert(tk.END, f"Responsável: {resp}\n")
                    caixa_texto.insert(tk.END, "-"*40 + "\n")
        elif escolha == "Pagamentos":
            if not pagamentos:
                caixa_texto.insert(tk.END, "Nenhum pagamento registrado.")
            else:
                for pg in pagamentos:
                    caixa_texto.insert(tk.END, f"Valor: R$ {pg.valor:.2f}\n")
                    caixa_texto.insert(tk.END, f"Método: {pg.metodo}\n")
                    caixa_texto.insert(tk.END, f"Status: {pg.status}\n")
                    caixa_texto.insert(tk.END, "-"*40 + "\n")
        caixa_texto.config(state="disabled")  # bloquear novamente      
    tk.Button(janela, text="Exibir", width=20, bg="#1976D2", fg="white", command=exibir).pack()
