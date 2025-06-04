import tkinter as tk
from tkinter import ttk, messagebox
from controller.ativo_controller import AtivoController
from models import *
from datetime import datetime
from utils.relatorio import gerar_relatorio_pdf

class MainView:
    def __init__(self, root):
        self.controller = AtivoController()
        self.root = root
        self.root.title("Gerenciador de Ativos")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(tuple(range(8)), weight=1)

        # Botão para abrir a janela de adicionar ativos
        tk.Button(root, text="Adicionar Ativo", command=self.abrir_janela_adicionar).grid(row=1, column=2, columnspan=1, pady=2)
        # Botão para editar ativos
        tk.Button(root, text="Editar Ativo", command=self.editar_ativo).grid(row=1, column=3, columnspan=1, pady=2)
        # Botão para deletar ativos
        tk.Button(root, text="Deletar Ativo", command=self.deletar_ativo).grid(row=1, column=4, columnspan=1, pady=2)
        # Botão para gerar relatório
        tk.Button(root, text="Gerar Relatório", command=self.gerar_relatorio).grid(row=1, column=5, columnspan=1, pady=2)

        # Notebook com abas por tipo de ativo
        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=0, column=0, columnspan=8, sticky="nsew", padx=10, pady=10)

        self.ativos = {
            "Computador": Computador, 
            "Monitor": Monitor,
            "Periférico": Perifericos,
            "Switch": Switch,
            "Cabo de Rede": Cabo_de_rede,
            "Nobreak": Nobreak,
            "Patch Panel": Patch_panel,
            "Roteador": Roteador,
            "Estabilizador": Estabilizador,
            "Ar-condicionado": Ar_condicionado,
            "Licença de Jogo": Licenca_jogo,
            "Jogo Adicional": Jogo_adicional,
            "Sistema Operacional": Sistema_operacional,
            "Antivírus": Antivirus,
            "Programa de Edição": Programa_edicao,
            "Painel LED": Painel_led,
            "Contato": Contato,
            "Divulgação": Divulgacao,
            "Identidade Digital": Identidade_digital,
            "Mesa para Computador": Mesa_computador,
            "Mesa para Computador Administração": Mesa_administracao,
            "Cadeira para Computador": Cadeira_computador,
            "Balcão para Recepção": Balcao_recepcao,
            "Piso Vinílico": Piso_vinilico,
            "Decoração": Decoracao,
            "Câmera de Segurança": Camera,
            "Sistema de Alarme": Alarme,
            "Software de Gerenciamento": Software_gerenciamento,
            "Banco de Dados": Banco_de_dados,
            "Website": Website,
            }
        self.tabela = {
            Computador: "Computador",
            Monitor: "Computador",
            Perifericos: "Computador",
            Switch: "Rede",
            Cabo_de_rede: "Rede",
            Nobreak: "Rede",
            Patch_panel: "Rede",
            Roteador: "Rede",
            Estabilizador: "Rede",
            Ar_condicionado: "Climatização",
            Licenca_jogo: "Licença",
            Jogo_adicional: "Licença",
            Sistema_operacional: "Licença",
            Antivirus: "Licença",
            Programa_edicao: "Licença",
            Painel_led: "Iluminação",
            Contato: "Marca",
            Divulgacao: "Marca",
            Identidade_digital: "Marca",
            Mesa_computador: "Mobília",
            Mesa_administracao: "Mobília",
            Cadeira_computador: "Mobília",
            Balcao_recepcao: "Mobília",
            Piso_vinilico: "Mobília",
            Decoracao: "Mobília",
            Camera: "Segurança",
            Alarme: "Segurança",
            Software_gerenciamento: "Software",
            Banco_de_dados: "Software",
            Website: "Software",
            }
        
        self.tipos_ativos = ["Computador", "Rede", "Segurança", "Climatização", "Iluminação", "Mobília", "Licença", "Software", "Marca"]
        self.tabelas = {}
        colunas = ("ID", "Tipo", "Nome", "Especificações", "Valor", "Estado", "Data de Aquisição", "Vida Útil (em anos)", "Ativo/Inativo")

        for tipo in self.tipos_ativos:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=tipo)
            # Tabela Treeview
            tree = ttk.Treeview(frame, columns=colunas, show='headings')
            for col in colunas:
                tree.heading(col, text=col)
                tree.column(col, width=100)
            tree.pack(fill='both', expand=True)

            self.tabelas[tipo] = tree
        self.iniciar_tabelas()

    def abrir_janela_adicionar(self):
        # Nova janela
        janela = tk.Toplevel(self.root)
        janela.title("Adicionar Ativo")
        janela.geometry("300x400")

        # Seletor de ativo (droplist)
        tk.Label(janela, text="Ativo").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ativo_var = tk.StringVar(value=list(self.ativos.keys())[0])
        ativo_combo = ttk.Combobox(janela, textvariable=ativo_var, values=list(self.ativos.keys()), state="readonly")
        ativo_combo.grid(row=0, column=1, padx=5, pady=5)

        # Campos padrão
        tk.Label(janela, text="ID").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        tk.Label(janela, text="Nome").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        tk.Label(janela, text="Especificações").grid(row=4, column=0, padx=5, pady=5, sticky="w")
        tk.Label(janela, text="Valor").grid(row=5, column=0, padx=5, pady=5, sticky="w")
        tk.Label(janela, text="Data de Aquisição").grid(row=6, column=0, padx=5, pady=5, sticky="w")
        tk.Label(janela, text="Estado").grid(row=7, column=0, padx=5, pady=5, sticky="w")
        tk.Label(janela, text="Vida Útil (em anos)").grid(row=8, column=0, padx=5, pady=5, sticky="w")
        
        tk.Label(janela, text="Ativo/Inativo").grid(row=9, column=0, padx=5, pady=5, sticky="w")
        status_var = tk.StringVar(value="Ativo")
        status_combo = ttk.Combobox(janela, textvariable=status_var, values=("Ativo", "Inativo"), state="readonly")
        status_combo.grid(row=9, column=1, padx=5, pady=5)

        id_entry = tk.Entry(janela)
        nome_entry = tk.Entry(janela)
        espec_entry = tk.Entry(janela)
        valor_entry = tk.Entry(janela)
        dataq_entry = tk.Entry(janela)
        estado_entry = tk.Entry(janela)
        vida_entry = tk.Entry(janela)

        id_entry.grid(row=2, column=1, padx=5, pady=5)
        nome_entry.grid(row=3, column=1, padx=5, pady=5)
        espec_entry.grid(row=4, column=1, padx=5, pady=5)
        valor_entry.grid(row=5, column=1, padx=5, pady=5)
        dataq_entry.grid(row=6, column=1, padx=5, pady=5)
        estado_entry.grid(row=7, column=1, padx=5, pady=5)
        vida_entry.grid(row=8, column=1, padx=5, pady=5)

        # Campo "Tipo" (apenas para Computador, Monitor, Periférico)
        tipo_label = tk.Label(janela, text="Tipo")
        tipo_var = tk.StringVar(value="Escritório")
        tipo_combo = ttk.Combobox(janela, textvariable=tipo_var, values=("Escritório", "Gamer", "Servidor"), state="readonly")

        def atualizar_tipo_field(*args):
            if ativo_var.get() in ("Computador", "Monitor", "Periférico"):
                tipo_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
                tipo_combo.grid(row=1, column=1, padx=5, pady=5)
            else:
                tipo_label.grid_remove()
                tipo_combo.grid_remove()

        ativo_var.trace_add("write", atualizar_tipo_field)
        atualizar_tipo_field()  # Chama uma vez para o valor inicial

        # Botão de confirmação
        def confirmar():
            try:
                id = id_entry.get()
                nome = nome_entry.get()
                espec = espec_entry.get()
                valor = float(valor_entry.get())
                data_str = dataq_entry.get()
                estado = estado_entry.get()
                vida = int(vida_entry.get())
                status = status_var.get()
                ativo_escolhido = ativo_var.get()
                ClasseSelecionada = self.ativos[ativo_escolhido]
                data_obj = datetime.strptime(data_str, "%d/%m/%Y")
                data_formatada = data_obj.strftime("%d/%m/%Y")
                if ativo_escolhido in ("Computador", "Monitor", "Periférico"):
                    tipo = tipo_var.get()
                    ativo = ClasseSelecionada(tipo, id, nome, espec, valor, data_formatada, estado, vida, status)
                else:
                    ativo = ClasseSelecionada(id, nome, espec, valor, data_formatada, estado, vida, status)
                self.controller.adicionar_ativo(ativo)
                tabela = self.tabela[ClasseSelecionada]
                self.atualizar_tabela(tabela)

                janela.destroy()  # Fecha a janelinha

            except ValueError:
                messagebox.showerror("Erro", "Valor e vida útil devem ser um número inteiro.")

        tk.Button(janela, text="Adicionar", command=confirmar).grid(row=10, column=0, columnspan=2, pady=10)

    def editar_ativo(self):
        tabela = self.notebook.tab(self.notebook.select(), "text")
        tree = self.tabelas[tabela]
        item_selecionado = tree.selection()

        if not item_selecionado:
            messagebox.showwarning("Aviso", "Selecione um ativo para editar.")
            return

        valores = tree.item(item_selecionado, "values")

        # Abre janela de edição
        self.abrir_janela_edicao(tabela, valores)

    def abrir_janela_edicao(self, tabela, valores):
        janela = tk.Toplevel(self.root)
        janela.title("Editar Ativo")
        janela.geometry("300x400")

        labels = ["ID", "Tipo", "Nome", "Especificações", "Valor", "Estado", "Data de Aquisição", "Vida Útil (em anos)", "Ativo/Inativo"]
        entradas = {}

        for i, label in enumerate(labels):
            tk.Label(janela, text=label).grid(row=i, column=0, padx=5, pady=5)
            if label == "Ativo/Inativo":
                status_var = tk.StringVar(value=valores[i])
                status_combo = ttk.Combobox(janela, textvariable=status_var, values=("Ativo", "Inativo"), state="readonly")
                status_combo.grid(row=i, column=1, padx=5, pady=5)
                entradas[label] = status_var
            else: 
                entrada = tk.Entry(janela)
                entrada.grid(row=i, column=1, padx=5, pady=5)
                if label == "Valor":
                    valor_limpo = valores[i].replace("R$", "").replace(".", "").replace(",", ".").strip()
                    entrada.insert(0, valor_limpo)
                elif label == "ID" or label == "Tipo":
                    entrada.insert(0, valores[i])
                    entrada.config(state="disabled")
                else:
                    entrada.insert(0, valores[i])
                entradas[label] = entrada

        def salvar():
            novos_valores = {label: entrada.get() for label, entrada in entradas.items()}
            self.controller.editar_ativo(tabela, novos_valores)
            self.atualizar_tabela(tabela)
            janela.destroy()

        tk.Button(janela, text="Salvar", command=salvar).grid(row=len(labels), column=0, columnspan=2, pady=10)

    def atualizar_tabela(self, tabela):
        tree = self.tabelas[tabela]
        tree.delete(*tree.get_children())
        ativos = self.controller.listar_ativos(tabela)

        for ativo in ativos:
            id, tipo, nome, especificacoes, valor, estado, data_aquisicao, vida_util, status = ativo
            valor_formatado = f"R$ {float(valor):,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.')
            tree.insert("", tk.END, values=(id, tipo, nome, especificacoes, valor_formatado, estado, data_aquisicao, vida_util, status))

    def iniciar_tabelas(self):
        for tipo in self.tipos_ativos:
            tabela = self.tabelas[tipo]
            ativos = self.controller.listar_ativos(tipo)
            for ativo in ativos:
                id, tipo, nome, especificacoes, valor, estado, data_aquisicao, vida_util, status = ativo
                valor_formatado = f"R$ {float(valor):,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.')
                tabela.insert("", tk.END, values=(id, tipo, nome, especificacoes, valor_formatado, estado, data_aquisicao, vida_util, status))

    def deletar_ativo(self):
        tabela = self.notebook.tab(self.notebook.select(), "text")
        tree = self.tabelas[tabela]
        item_selecionado = tree.selection()

        if not item_selecionado:
            messagebox.showwarning("Aviso", "Selecione um ativo para deletar.")
            return

        id_ativo = tree.item(item_selecionado, "values")[0]
        resposta = messagebox.askyesno("Confirmação", f"Você tem certeza que deseja deletar o ativo com ID {id_ativo}?")
        if not resposta:
            return
        self.controller.deletar_ativo(tabela, id_ativo)
        self.atualizar_tabela(tabela)

    def gerar_relatorio(self):
        tabela = self.notebook.tab(self.notebook.select(), "text")
        ativos = self.controller.listar_ativos(tabela)
        if ativos:
            gerar_relatorio_pdf(tabela, ativos)
        else:
            messagebox.showinfo("Informação", "Não há dados para gerar o relatório.")