import tkinter as tk
from tkinter import messagebox
import subprocess
import ctypes



class UIMenu:
    def __init__(self, master):
        self.master = master
        
        master.title("Scraping de Produtos")
        master.iconbitmap("./assets/icon_auto.ico")
        master.geometry("300x190")
        
        
        self.label = tk.Label(master, text="Escolha uma opção: ")
        self.label.pack(pady=10)
         
        self.button1 = tk.Button(master, text="Categoria Em Destaque", command=lambda: self.executar_script(1),padx=10, pady=5, width=20, wraplength=150)
        self.button1.pack()

        self.button2 = tk.Button(master, text="Categoria Todos Os Produtos", command=lambda: self.executar_script(2),padx=10, pady=5, width=20, wraplength=150)
        self.button2.pack()

        self.button3 = tk.Button(master, text="Categoria Original", command=lambda: self.executar_script(3),padx=10, pady=5, width=20, wraplength=150)
        self.button3.pack()
        
        self.definir_icone_barra_tarefas()
        
    def executar_script(self, opcao):
        try:
            subprocess.run(["pythonw","app.py",str(opcao)], shell=False, check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Erro",f"Ocorreu um erro ao executar o script Python:\n{e}")
        else: 
            self.master.iconify()
    
        
    def definir_icone_barra_tarefas(self):
        try:
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Scraping de Produtos")
            self.master.wm_withdraw()
            self.master.after(10, lambda: self.master.wm_deiconify())
        except Exception as e:
            print(f"Erro ao definir ícone na barra de tarefas: {e}")
        
#Cria a janela principal
root = tk.Tk()
app = UIMenu(root)
root.mainloop()
        