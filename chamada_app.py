import tkinter as tk
from tkinter import messagebox
from chamada_db import criar_banco, salvar_presenca

class ListaChamadaApp:
    def __init__(self, master):
        self.master = master
        master.title("Lista de Chamada - Agosto 2025")
        master.configure(bg="green")
    
        self.alunos = [
            "Ana", "Augusto", "Carla", "Diego", "Fernanda",
            "Gustavo", "Helena", "Igor", "Joao", "Larissa"
        ]

        #dia da semana + datas de agosto 2025
        self.dias_semana = {
            "Segunda (04/08)": "2025-08-04",
            "Terça (05/08)"  : "2025-08-05",
            "Quarta (06/08)" : "2025-08-06",
            "Quinta (07/08)" : "2025-08-07",
            "Sexta (08/08)"  : "2025-08-08"
        }

        self.check_vars = {}

        tk.Label(master, text="Lista de Chamada - Agosto 2025", 
                    font=("Arial", 14, "bold"), bg="green", fg="white").pack(pady=10)

        frame_tabela = tk.Frame(master, bg="green")
        frame_tabela.pack()

        # Cabeçalho
        tk.Label(frame_tabela, text="Aluno", font=("Arial", 12, "bold"),
                    bg="green", fg="white", width=16).grid(row=0, column=0)
        for j, dia in enumerate(self.dias_semana.keys(), start=1):
            tk.Label(frame_tabela, text=dia, font=("Arial", 11, "bold"),
                        bg="green", fg="white", width=14).grid(row=0, column=j)

        # Alunos + Checkboxes
        for i, aluno in enumerate(self.alunos, start=1):
            tk.Label(frame_tabela, text=aluno, font=("Arial", 10),
                     bg="green", fg="black", width=16).grid(row=i, column=0, padx=5, pady=5)
            self.check_vars[aluno] = {}
            for j, (dia, data_iso) in enumerate(self.dias_semana.items(), start=1):
                var = tk.IntVar()
                chk = tk.Checkbutton(frame_tabela, variable=var, bg="green")
                chk.grid(row=i, column=j, padx=5, pady=5)
                self.check_vars[aluno][data_iso] = var  # Armazenamos a data real (YYYY-MM-DD)

        btn_salvar = tk.Button(master, text="Salvar Presenças",
                                bg="white", fg="green", font=("Arial", 11, "bold"), command=self.salvar)
        btn_salvar.pack(pady=15)

    def salvar(self):
        presencas = {aluno: {data: var.get() for data, var in dias.items()}
                        for aluno, dias in self.check_vars.items()}
        salvar_presenca(presencas)
        messagebox.showinfo("Sucesso", "Presenças salvas no banco de dados!")

# Execução
if __name__ == "__main__":
    criar_banco()
    root = tk.Tk()
    app = ListaChamadaApp(root)
    root.mainloop()
