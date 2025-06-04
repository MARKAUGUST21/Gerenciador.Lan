import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Credenciais de exemplo ---
CREDENCIAIS = {"admin": "1234", "funcionario": "4321"}

# --- Função que verifica login ---
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    if CREDENCIAIS.get(usuario) == senha:
        messagebox.showinfo("Sucesso", "Login efetuado com sucesso!")
        root.destroy()
        abrir_painel_admin()
    else:
        messagebox.showerror("Erro", "Login ou senha incorretos!")

# --- Função que cria a janela do painel administrativo ---
def abrir_painel_admin():
    admin = tk.Tk()
    admin.title("Painel Administrativo - Gestão Lan House")
    admin.geometry("900x600")

    # Cria um Notebook (abas)
    notebook = ttk.Notebook(admin)
    notebook.pack(fill='both', expand=True)

    # --- Aba de Ativos ---
    frame_ativos = ttk.Frame(notebook)
    notebook.add(frame_ativos, text="Ativos")

    global tree_ativos, colunas_ativos
    colunas_ativos = ("id", "nome", "especificacoes", "valor", "ult_manutencao", "status", "data_aquisicao", "vida_util",)
    tree_ativos = ttk.Treeview(frame_ativos, columns=colunas_ativos, show='headings')

    for col in colunas_ativos:
        tree_ativos.heading(col, text=col.capitalize())
        tree_ativos.column(col, width=100)

    # Dados de exemplo
    
    tree_ativos.insert("", tk.END, values=("#SEC1", "Câmera de Segurança", "IP, Full HD, 20m, 120°, IP66", "225","10/01/2025", "Novo", "10/01/2025", "5 anos"))

    tree_ativos.insert("", tk.END, values=("#COE1", "Escritório", "quad-core, RAM 8gb, SSD SATA 512 GB", "1550","01/01/2025", "Novo", "01/01/2025", "6 anos"))

    tree_ativos.insert("", tk.END, values=("#COS1", "Servidor", "quad-core, RAM 8gb, SSD M.2 2 TB, 2x HD 1 TB", "2550","01/01/2025", "Novo", "01/01/2025", "5 anos"))
    
    tree_ativos.insert("", tk.END, values=("#SIOP1", "Sistema Operacional", "Windows 11", "200","08/01/2025", "Novo", "08/01/2025", "-"))

    tree_ativos.insert("", tk.END, values=("#CACO1", "Cadeira para computador", "Ergônomica de Escritório", "200","04/01/2025", "Novo", "08/01/2025", "8 anos"))

    tree_ativos.insert("", tk.END, values=("#CLAC1", "Ar-condicionado", "Split Inverter 18.000 BTUs", "2700","05/01/2025", "Novo", "05/01/2025", "8 anos"))

    tree_ativos.insert("", tk.END, values=("#REN1", "Nobreak", "1400 VA, Entrada e Saída Bivolt", "700","02/01/2025", "Novo", "02/01/2025", "5 anos"))

    tree_ativos.insert("", tk.END, values=("#RES1", "Switch", "Gigabit 10/100/1000 Mbps Gerenciável 24 portas", "790","02/01/2025", "Novo", "02/01/2025", "5 anos"))

    tree_ativos.insert("", tk.END, values=("#MECO1", "Mesa para computador", "100x60 cm", "150","04/01/2025", "Novo", "04/01/2025", "8 anos"))

    
    tree_ativos.pack(fill='both', expand=True, padx=10, pady=10)

    # Botões de ação para ativos
    frame_botoes_ativos = ttk.Frame(frame_ativos)
    frame_botoes_ativos.pack(pady=5)

    tk.Button(frame_botoes_ativos, text="Adicionar Ativo", command=adicionar_ativo).grid(row=0, column=0, padx=5)
    tk.Button(frame_botoes_ativos, text="Editar Selecionado", command=editar_ativo).grid(row=0, column=1, padx=5)
    tk.Button(frame_botoes_ativos, text="Remover Selecionado", command=remover_ativo).grid(row=0, column=2, padx=5)

    # --- Aba de Funcionários ---
    frame_funcionarios = ttk.Frame(notebook)
    notebook.add(frame_funcionarios, text="Funcionários")

    global tree_func, colunas_func
    colunas_func = ("id", "nome", "funcao", "especialidade", "salario")
    tree_func = ttk.Treeview(frame_funcionarios, columns=colunas_func, show='headings')

    for col in colunas_func:
        tree_func.heading(col, text=col.capitalize())
        tree_func.column(col, width=150)

    # Adicionar os funcionarios na hora


    tree_func.pack(fill='both', expand=True, padx=10, pady=10)



    # Botões de ação para funcionários
    frame_botoes_func = ttk.Frame(frame_funcionarios)
    frame_botoes_func.pack(pady=5)

    tk.Button(frame_botoes_func, text="Adicionar Funcionário", command=adicionar_funcionario).grid(row=0, column=0, padx=5)
    tk.Button(frame_botoes_func, text="Editar Selecionado", command=editar_funcionario).grid(row=0, column=1, padx=5)
    tk.Button(frame_botoes_func, text="Remover Selecionado", command=remover_funcionario).grid(row=0, column=2, padx=5)

    admin.mainloop()

# --- Funções de Ação: Ativos ---
def adicionar_ativo():
    def salvar():
        valores = [entrys[col].get() for col in colunas_ativos]
        tree_ativos.insert("", tk.END, values=valores)
        janela.destroy()

    janela = tk.Toplevel()
    janela.title("Adicionar Ativo")
    entrys = {}
    for i, col in enumerate(colunas_ativos):
        tk.Label(janela, text=col.capitalize()).grid(row=i, column=0, padx=5, pady=5)
        entrys[col] = tk.Entry(janela)
        entrys[col].grid(row=i, column=1, padx=5, pady=5)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=len(colunas_ativos), column=0, columnspan=2, pady=10)

def editar_ativo():
    item = tree_ativos.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecione um item para editar.")
        return

    valores_atuais = tree_ativos.item(item, 'values')

    def salvar():
        novos_valores = [entrys[col].get() for col in colunas_ativos]
        tree_ativos.item(item, values=novos_valores)
        janela.destroy()

    janela = tk.Toplevel()
    janela.title("Editar Ativo")
    entrys = {}
    for i, col in enumerate(colunas_ativos):
        tk.Label(janela, text=col.capitalize()).grid(row=i, column=0, padx=5, pady=5)
        entrys[col] = tk.Entry(janela)
        entrys[col].insert(0, valores_atuais[i])
        entrys[col].grid(row=i, column=1, padx=5, pady=5)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=len(colunas_ativos), column=0, columnspan=2, pady=10)

def remover_ativo():
    item = tree_ativos.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecione um item para remover.")
        return
    tree_ativos.delete(item)

# --- Funções de Ação: Funcionários ---
def adicionar_funcionario():
    def salvar():
        valores = [entrys[col].get() for col in colunas_func]
        tree_func.insert("", tk.END, values=valores)
        janela.destroy()

    janela = tk.Toplevel()
    janela.title("Adicionar Funcionário")
    entrys = {}
    for i, col in enumerate(colunas_func):
        tk.Label(janela, text=col.capitalize()).grid(row=i, column=0, padx=5, pady=5)
        entrys[col] = tk.Entry(janela)
        entrys[col].grid(row=i, column=1, padx=5, pady=5)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=len(colunas_func), column=0, columnspan=2, pady=10)

def editar_funcionario():
    item = tree_func.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecione um item para editar.")
        return

    valores_atuais = tree_func.item(item, 'values')

    def salvar():
        novos_valores = [entrys[col].get() for col in colunas_func]
        tree_func.item(item, values=novos_valores)
        janela.destroy()

    janela = tk.Toplevel()
    janela.title("Editar Funcionário")
    entrys = {}
    for i, col in enumerate(colunas_func):
        tk.Label(janela, text=col.capitalize()).grid(row=i, column=0, padx=5, pady=5)
        entrys[col] = tk.Entry(janela)
        entrys[col].insert(0, valores_atuais[i])
        entrys[col].grid(row=i, column=1, padx=5, pady=5)

    tk.Button(janela, text="Salvar", command=salvar).grid(row=len(colunas_func), column=0, columnspan=2, pady=10)

def remover_funcionario():
    item = tree_func.selection()
    if not item:
        messagebox.showwarning("Aviso", "Selecione um item para remover.")
        return
    tree_func.delete(item)

# --- Janela de Login ---
root = tk.Tk()
root.title("Login - Gestão Lan House")
root.geometry("700x400")
root.configure(bg="")

# Adiciona cor aos widgets de login
label_usuario = tk.Label(root, text="Usuário:", bg="#e8e8e8")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(root)
entry_usuario.pack(pady=5)

label_senha = tk.Label(root, text="Senha:", bg="#e8e8e8")
label_senha.pack(pady=5)
entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=5)

btn_entrar = tk.Button(root, text="Entrar", command=verificar_login, bg="#4CAF50", fg="white", activebackground="#388E3C")
btn_entrar.pack(pady=10)



root.mainloop()