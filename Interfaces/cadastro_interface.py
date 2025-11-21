import tkinter as tk
from tkinter import ttk, messagebox

from Modelos.paciente import Paciente
from Modelos.medico import Medico
from Modelos.recepcionista import Recepcionista


def abrir_tela_cadastro(janela_principal, pacientes, medicos, recepcionistas):
    cadastro = tk.Toplevel(janela_principal)
    cadastro.title("Cadastro de Usuários")
    cadastro.geometry("420x420")
    cadastro.resizable(False, False)

    tk.Label(cadastro, text="CADASTRAR USUÁRIO", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(cadastro, text="Selecione o tipo:", font=("Arial", 11)).pack()
    tipo_var = tk.StringVar(value="Paciente")

    tipos = ["Paciente", "Médico", "Recepcionista"]
    box_tipo = ttk.Combobox(cadastro, textvariable=tipo_var, values=tipos, state="readonly")
    box_tipo.pack(pady=5)

    frame = tk.Frame(cadastro)
    frame.pack(pady=10)

    # CAMPOS BÁSICOS
    tk.Label(frame, text="Nome:").grid(row=0, column=0, sticky="w")
    entry_nome = tk.Entry(frame, width=30)
    entry_nome.grid(row=0, column=1)

    tk.Label(frame, text="CPF:").grid(row=1, column=0, sticky="w")
    entry_cpf = tk.Entry(frame, width=30)
    entry_cpf.grid(row=1, column=1)

    tk.Label(frame, text="Telefone:").grid(row=2, column=0, sticky="w")
    entry_telefone = tk.Entry(frame, width=30)
    entry_telefone.grid(row=2, column=1)

    # CAMPO EXTRA – muda conforme o tipo selecionado
    label_extra = tk.Label(frame, text="Histórico médico:")
    entry_extra = tk.Entry(frame, width=30)
    label_extra.grid(row=3, column=0, sticky="w")
    entry_extra.grid(row=3, column=1)

    def atualizar_campo_extra(*args):
        tipo = tipo_var.get()
        if tipo == "Paciente":
            label_extra.config(text="Histórico médico:")
        elif tipo == "Médico":
            label_extra.config(text="CRM / Especialidade:")
        else:
            label_extra.config(text="Matrícula:")

    tipo_var.trace("w", atualizar_campo_extra)

    # BOTÃO SALVAR
    def salvar():
        nome = entry_nome.get().strip()
        cpf = entry_cpf.get().strip()
        telefone = entry_telefone.get().strip()
        extra = entry_extra.get().strip()
        tipo = tipo_var.get()

        if not nome or not cpf or not telefone or not extra:
            messagebox.showerror("Erro", "Preencha todos os campos.")
            return

        # CADASTRO
        if tipo == "Paciente":
            novo = Paciente(nome, cpf, telefone, extra)
            pacientes[cpf] = novo

        elif tipo == "Médico":
            try:
                crm, especialidade = extra.split("/")
            except:
                messagebox.showerror("Erro", "Formato inválido! Use: CRM/Especialidade")
                return
            novo = Medico(nome, cpf, telefone, crm.strip(), especialidade.strip())
            medicos[cpf] = novo

        elif tipo == "Recepcionista":
            novo = Recepcionista(nome, cpf, telefone, extra)
            recepcionistas[cpf] = novo

        messagebox.showinfo("Sucesso", f"{tipo} cadastrado(a) com sucesso!")
        cadastro.destroy()

    tk.Button(cadastro, text="Cadastrar", font=("Arial", 12), bg="#4CAF50", fg="white",
              width=20, command=salvar).pack(pady=20)
