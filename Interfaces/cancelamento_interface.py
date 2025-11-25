import tkinter as tk
from tkinter import messagebox


def abrir_tela_cancelamento(janela_principal, consultas_agendadas):

    janela_cancelar = tk.Toplevel(janela_principal)
    janela_cancelar.title("Cancelar Consulta")
    janela_cancelar.geometry("300x300")

    tk.Label(janela_cancelar, text="CPF do paciente:").pack()
    entry_cpf = tk.Entry(janela_cancelar)
    entry_cpf.pack()

    lista_box = tk.Listbox(janela_cancelar, width=40)
    lista_box.pack(pady=10)

    consultas_filtradas = []

    def buscar():
        lista_box.delete(0, tk.END)
        cpf = entry_cpf.get()

        consultas_filtradas.clear()

        for c in consultas_agendadas:
            if c.paciente.cpf == cpf and c.status != "cancelada":
                consultas_filtradas.append(c)
                lista_box.insert(tk.END, f"ID {c.id} - {c.data_hora}")

        if not consultas_filtradas:
            messagebox.showinfo("Aviso", "Nenhuma consulta encontrada.")

    def cancelar():
        index = lista_box.curselection()
        if not index:
            messagebox.showerror("Erro", "Selecione uma consulta.")
            return

        consulta = consultas_filtradas[index[0]]
        consulta.alterar_status("cancelada")
        messagebox.showinfo("Sucesso", "Consulta cancelada.")
        buscar()

    tk.Button(janela_cancelar, text="Buscar consultas", command=buscar).pack()
    tk.Button(janela_cancelar, text="Cancelar consulta", bg="tomato", command=cancelar).pack(pady=5)
