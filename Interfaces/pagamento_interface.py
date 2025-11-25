import tkinter as tk
from tkinter import messagebox

from Modelos.pagamento import Pagamento


def abrir_tela_pagamento(janela_principal, pagamentos):

    janela_pagamento = tk.Toplevel(janela_principal)
    janela_pagamento.title("Registrar Pagamento")
    janela_pagamento.geometry("350x300")

    # -------- CAMPOS --------

    tk.Label(janela_pagamento, text="Valor (R$):").pack()
    entry_valor = tk.Entry(janela_pagamento)
    entry_valor.pack()

    tk.Label(janela_pagamento, text="Método (pix / cartao / dinheiro):").pack()
    entry_metodo = tk.Entry(janela_pagamento)
    entry_metodo.pack()

    tk.Label(janela_pagamento, text="Status (opcional):").pack()
    entry_status = tk.Entry(janela_pagamento)
    entry_status.insert(0, "pago")  # valor padrão
    entry_status.pack()

    # -------- FUNÇÃO REGISTRAR PAGAMENTO --------

    def registrar_pagamento():
        try:
            valor = float(entry_valor.get())
        except ValueError:
            messagebox.showerror("Erro", "Valor inválido.")
            return

        metodo = entry_metodo.get().lower().strip()
        status = entry_status.get().lower().strip()

        # validações automáticas da classe Pagamento
        try:
            pagamento = Pagamento(valor, metodo)
            pagamento.status = status
        except ValueError as erro:
            messagebox.showerror("Erro", str(erro))
            return

        pagamentos.append(pagamento)

        messagebox.showinfo("Sucesso", "Pagamento registrado com sucesso!")
        janela_pagamento.destroy()

    tk.Button(
        janela_pagamento,
        text="Registrar",
        bg="lightgreen",
        command=registrar_pagamento
    ).pack(pady=10)