import tkinter as tk
from Interfaces.cadastro_interface import abrir_tela_cadastro

def iniciar_interface():
    janela = tk.Tk()
    janela.title("Sistema da Clínica")
    janela.geometry("400x250")
    janela.resizable(False, False)

    # Bancos locais na interface
    pacientes = {}
    medicos = {}
    recepcionistas = {}

    tk.Label(janela, text="SISTEMA DA CLÍNICA", font=("Arial", 16, "bold")).pack(pady=20)

    # BOTÃO QUE ABRE A TELA DE CADASTRO (CORRETO)
    tk.Button(
        janela,
        text="CADASTRAR",
        font=("Arial", 12),
        bg="#2196F3",
        fg="white",
        width=25,
        command=lambda: abrir_tela_cadastro(janela, pacientes, medicos, recepcionistas)
    ).pack(pady=10)

    janela.mainloop()
