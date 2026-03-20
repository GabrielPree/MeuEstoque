import tkinter as tk
from tkinter import ttk, messagebox
from AppBD import AppBD

class MeuEstoque:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Meu Estoque - Gestão de Produtos")
        self.root.geometry("900x800")
        self.root.resizable(True, True)

        # Configurar estilo
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # Cores do tema escuro - Cinza
        self.cor_primaria = "#1e1e1e"
        self.cor_secundaria = "#2d2d2d"
        self.cor_terciaria = "#3c3c3c"
        self.cor_entrada = "#3c3c3c"
        self.cor_texto = "#ffffff"
        self.cor_texto_secundario = "#cccccc"
        self.cor_borda = "#4a4a4a"

        # Cores para o Treeview
        self.tree_bg1 = "#e0e0e0"
        self.tree_bg2 = "#d0d0d0"
        self.tree_fg = "#1e1e1e"
        self.tree_heading_bg = "#3c3c3c"
        self.tree_heading_fg = "#ffffff"
        self.tree_select_bg = "#1565c0"
        self.tree_select_fg = "#ffffff"

        # Cores para botões
        self.cor_sucesso = "#2e7d32"
        self.cor_sucesso_hover = "#1b5e20"
        self.cor_azul = "#1565c0"
        self.cor_azul_hover = "#0d47a1"
        self.cor_vermelho = "#c62828"
        self.cor_vermelho_hover = "#b71c1c"
        self.cor_cinza = "#546e7a"
        self.cor_cinza_hover = "#37474f"

        # Configurar cores da janela principal
        self.root.configure(bg=self.cor_primaria)

        # Configurar estilo dos ttk widgets
        self.style.configure('TLabel', background=self.cor_primaria, foreground=self.cor_texto)
        self.style.configure('TFrame', background=self.cor_primaria)
        self.style.configure('TLabelframe', background=self.cor_primaria, foreground=self.cor_texto)
        self.style.configure('TLabelframe.Label', background=self.cor_primaria, foreground=self.cor_texto)

        # Frame principal com padding
        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Título da aplicação
        titulo = tk.Label(
            main_frame, 
            text="📦 GESTÃO DE PRODUTOS", 
            font=("Arial", 18, "bold"),
            bg=self.cor_primaria,
            fg=self.cor_texto
        )
        titulo.pack(pady=(0, 20))

        # Frame para entrada de dados
        entrada_frame = ttk.LabelFrame(main_frame, text="Dados do Produto", padding="15")
        entrada_frame.pack(fill=tk.X, pady=(0, 15))

        # Configurar grid para entrada de dados
        for i in range(3):
            entrada_frame.columnconfigure(i, weight=1)

        # Campos de entrada
        tk.Label(
            entrada_frame, 
            text="Código:", 
            font=("Arial", 10),
            bg=self.cor_primaria,
            fg=self.cor_texto
        ).grid(row=0, column=0, sticky='w', padx=5, pady=5)

        self.txtCodigo = tk.Entry(
            entrada_frame, 
            font=("Arial", 10),
            relief=tk.SUNKEN,
            bg=self.cor_entrada,
            fg=self.cor_texto,
            insertbackground=self.cor_texto,
            highlightthickness=1,
            highlightcolor=self.cor_borda,
            highlightbackground=self.cor_borda
        )
        self.txtCodigo.grid(row=0, column=1, sticky='ew', padx=5, pady=5)
        self.txtCodigo.bind('<Key>', lambda e: 'break')  # Impede digitação

        tk.Label(
            entrada_frame, 
            text="Nome:", 
            font=("Arial", 10),
            bg=self.cor_primaria,
            fg=self.cor_texto
        ).grid(row=1, column=0, sticky='w', padx=5, pady=5)

        self.txtNome = tk.Entry(
            entrada_frame, 
            font=("Arial", 10),
            relief=tk.FLAT,
            bg=self.cor_entrada,
            fg=self.cor_texto,
            insertbackground=self.cor_texto,
            highlightthickness=1,
            highlightcolor=self.cor_borda,
            highlightbackground=self.cor_borda
        )
        self.txtNome.grid(row=1, column=1, sticky='ew', padx=5, pady=5)
        self.txtNome.bind('<Return>', lambda e: self.txtPreco.focus())

        tk.Label(
            entrada_frame, 
            text="Preço (R$):", 
            font=("Arial", 10),
            bg=self.cor_primaria,
            fg=self.cor_texto
        ).grid(row=2, column=0, sticky='w', padx=5, pady=5)

        self.txtPreco = tk.Entry(
            entrada_frame, 
            font=("Arial", 10),
            relief=tk.FLAT,
            bg=self.cor_entrada,
            fg=self.cor_texto,
            insertbackground=self.cor_texto,
            highlightthickness=1,
            highlightcolor=self.cor_borda,
            highlightbackground=self.cor_borda
        )
        self.txtPreco.grid(row=2, column=1, sticky='ew', padx=5, pady=5)
        self.txtPreco.bind('<Return>', lambda e: self.cadastrar_produto())

        # Frame para botões
        botoes_frame = ttk.Frame(main_frame)
        botoes_frame.pack(fill=tk.X, pady=(0, 15))

        # Configurar grid para botões
        for i in range(4):
            botoes_frame.columnconfigure(i, weight=1)

        # Botões com estilização
        self.btnCadastrar = tk.Button(
            botoes_frame,
            text="➕ CADASTRAR",
            font=("Arial", 10, "bold"),
            bg=self.cor_sucesso,
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            activebackground=self.cor_sucesso_hover,
            activeforeground="white",
            command=self.cadastrar_produto
        )
        self.btnCadastrar.grid(row=0, column=0, padx=5, sticky='ew')

        self.btnAtualizar = tk.Button(
            botoes_frame,
            text="✏️ ATUALIZAR",
            font=("Arial", 10, "bold"),
            bg=self.cor_azul,
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            activebackground=self.cor_azul_hover,
            activeforeground="white",
            command=self.atualizar_produto
        )
        self.btnAtualizar.grid(row=0, column=1, padx=5, sticky='ew')

        self.btnExcluir = tk.Button(
            botoes_frame,
            text="❌ EXCLUIR",
            font=("Arial", 10, "bold"),
            bg=self.cor_vermelho,
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            activebackground=self.cor_vermelho_hover,
            activeforeground="white",
            command=self.excluir_produto
        )
        self.btnExcluir.grid(row=0, column=2, padx=5, sticky='ew')

        self.btnLimpar = tk.Button(
            botoes_frame,
            text="🧹 LIMPAR",
            font=("Arial", 10, "bold"),
            bg=self.cor_cinza,
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            activebackground=self.cor_cinza_hover,
            activeforeground="white",
            command=self.limpar_tela
        )
        self.btnLimpar.grid(row=0, column=3, padx=5, sticky='ew')

        # Frame para a tabela
        tabela_container = ttk.Frame(main_frame)
        tabela_container.pack(fill=tk.BOTH, expand=True)

        # Barra de pesquisa
        pesquisa_frame = ttk.LabelFrame(tabela_container, text="🔍 Pesquisar Produtos", padding="10")
        pesquisa_frame.pack(fill=tk.X, pady=(0, 10))

        # Configurar grid para pesquisa
        pesquisa_frame.columnconfigure(1, weight=1)

        tk.Label(
            pesquisa_frame, 
            text="Buscar:", 
            font=("Arial", 10),
            bg=self.cor_primaria,
            fg=self.cor_texto
        ).grid(row=0, column=0, sticky='w', padx=5)

        self.txtPesquisa = tk.Entry(
            pesquisa_frame, 
            font=("Arial", 10),
            relief=tk.FLAT,
            bg=self.cor_entrada,
            fg=self.cor_texto,
            insertbackground=self.cor_texto,
            highlightthickness=1,
            highlightcolor=self.cor_borda,
            highlightbackground=self.cor_borda
        )
        self.txtPesquisa.grid(row=0, column=1, sticky='ew', padx=5)

        # Bind para pesquisa em tempo real
        self.txtPesquisa.bind('<KeyRelease>', self.filtrar_produtos)

        btnLimparPesquisa = tk.Button(
            pesquisa_frame,
            text="🧹 Limpar",
            font=("Arial", 9),
            bg=self.cor_cinza,
            fg="white",
            relief=tk.FLAT,
            cursor="hand2",
            activebackground=self.cor_cinza_hover,
            activeforeground="white",
            command=self.limpar_pesquisa
        )
        btnLimparPesquisa.grid(row=0, column=2, padx=5)

        # Frame para o Treeview
        treeview_frame = ttk.LabelFrame(tabela_container, text="Produtos Cadastrados", padding="10")
        treeview_frame.pack(fill=tk.BOTH, expand=True)

        # Scrollbar para a tabela
        scrollbar = tk.Scrollbar(treeview_frame, bg=self.cor_secundaria, troughcolor=self.cor_primaria)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Treeview
        self.tree = ttk.Treeview(
            treeview_frame,
            columns=("CODIGO", "NOME", "PREÇO"),
            show="headings",
            yscrollcommand=scrollbar.set,
            selectmode='browse',
            height=15
        )
        scrollbar.config(command=self.tree.yview)

        # Configurar cores do Treeview
        style = ttk.Style()
        style.configure("Treeview",
                       background=self.tree_bg1,
                       foreground=self.tree_fg,
                       fieldbackground=self.tree_bg1,
                       borderwidth=0)
        style.map('Treeview',
                  background=[('selected', self.tree_select_bg)],
                  foreground=[('selected', self.tree_select_fg)])

        style.configure("Treeview.Heading",
                       background=self.tree_heading_bg,
                       foreground=self.tree_heading_fg,
                       relief="flat",
                       font=('Arial', 10, 'bold'))
        style.map("Treeview.Heading",
                  background=[('active', self.cor_azul)])

        # Ordenação das colunas
        self.tree.heading("CODIGO", text="Código", command=lambda: self.ordenar_coluna("CODIGO", False))
        self.tree.heading("NOME", text="Nome do Produto", command=lambda: self.ordenar_coluna("NOME", False))
        self.tree.heading("PREÇO", text="Preço (R$)", command=lambda: self.ordenar_coluna("PREÇO", False))

        self.tree.column("CODIGO", width=80, anchor='center')
        self.tree.column("NOME", width=300, anchor='w')
        self.tree.column("PREÇO", width=120, anchor='e')

        self.tree.pack(fill=tk.BOTH, expand=True)

        # Definir tags para linhas alternadas
        self.tree.tag_configure('linha1', background=self.tree_bg1, foreground=self.tree_fg)
        self.tree.tag_configure('linha2', background=self.tree_bg2, foreground=self.tree_fg)

        self.tree.bind('<<TreeviewSelect>>', self.apresentarRegistrosSelecionados)

        # Status bar
        self.status_bar = tk.Label(
            root,
            text="Sistema de Gestão de Produtos v1.0",
            bd=1,
            relief=tk.FLAT,
            anchor=tk.W,
            bg=self.cor_terciaria,
            fg=self.cor_texto,
            font=("Arial", 9)
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Carregar dados iniciais
        self.carregar_dados_iniciais()

#-----------------------------------------------------------------------------------------------------------------------
#                           Métodos para operações CRUD e funcionalidades adicionais
#-----------------------------------------------------------------------------------------------------------------------

    def filtrar_produtos(self, event=None):
        termo = self.txtPesquisa.get().lower().strip()

        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            registros = self.db.selecionar_dados()

            if termo:
                # Filtrar registros que contêm o termo no código ou nome
                registros_filtrados = []
                for registro in registros:
                    if (termo in str(registro[0]).lower() or  # Código
                        termo in registro[1].lower()):        # Nome
                        registros_filtrados.append(registro)

                # Inserir dados filtrados
                for i, registro in enumerate(registros_filtrados):
                    tag = 'linha1' if i % 2 == 0 else 'linha2'
                    registro_formatado = list(registro)
                    registro_formatado[2] = f"R$ {float(registro[2]):.2f}"
                    self.tree.insert("", tk.END, values=registro_formatado, tags=(tag,))
                
                self.atualizar_status(f"📊 Encontrados {len(registros_filtrados)} produtos")
            else:
                # Mostrar todos os produtos
                for i, registro in enumerate(registros):
                    tag = 'linha1' if i % 2 == 0 else 'linha2'
                    registro_formatado = list(registro)
                    registro_formatado[2] = f"R$ {float(registro[2]):.2f}"
                    self.tree.insert("", tk.END, values=registro_formatado, tags=(tag,))

                self.atualizar_status(f"📊 Total de {len(registros)} produtos")

        except Exception as e:
            self.atualizar_status(f"❌ Erro ao filtrar: {str(e)}", "erro")

    def limpar_pesquisa(self):
        self.txtPesquisa.delete(0, tk.END)
        self.carregar_dados_iniciais()

    def ordenar_coluna(self, col, reverse):
        dados = []
 
        for child in self.tree.get_children(''):
            valores = self.tree.item(child, 'values')
            
            if col == "CODIGO":
                # Ordenar por código (inteiro)
                try:
                    dados.append((int(valores[0]), child))
                except:
                    dados.append((valores[0], child))

            elif col == "PREÇO":
                # Ordenar por preço (float) - remover R$
                try:
                    preco = float(valores[2].replace('R$', '').strip())
                    dados.append((preco, child))
                except:
                    dados.append((0, child))

            else:  # NOME
                # Ordenar por nome (string)
                dados.append((valores[1].lower(), child))

        # Ordenar os dados
        dados.sort(key=lambda x: x[0], reverse=reverse)

        # Reorganizar na treeview
        for index, (_, child) in enumerate(dados):
            self.tree.move(child, '', index)

        # Atualizar comando da coluna para alternar ordenação
        self.tree.heading(col, command=lambda: self.ordenar_coluna(col, not reverse))

    def atualizar_status(self, mensagem, tipo="info"):
        cores = {
            "info": self.cor_terciaria,
            "sucesso": self.cor_sucesso,
            "erro": self.cor_vermelho
        }
        self.status_bar.config(text=mensagem, bg=cores.get(tipo, self.cor_terciaria))
        self.root.after(3000, lambda: self.status_bar.config(text="Meu Estoque - Gestão de Produtos v1.0", bg=self.cor_terciaria))

    def validar_preco(self, preco):
        try:
            preco_limpo = preco.replace('R$', '').replace(' ', '').replace(',', '.')
            return float(preco_limpo)
        except ValueError:
            return None

    def cadastrar_produto(self):
        nome = self.txtNome.get().strip()
        preco = self.txtPreco.get().strip()

        if not nome or not preco:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
            return

        preco_valido = self.validar_preco(preco)
        if preco_valido is None:
            messagebox.showwarning("Aviso", "Por favor, insira um preço válido!")
            return

        try:
            self.db.inserir_dados(nome, preco_valido)
            self.atualizar_status(f"✅ Produto '{nome}' cadastrado com sucesso!", "sucesso")
            self.carregar_dados_iniciais()
            self.limpar_tela()
        except Exception as e:
            self.atualizar_status(f"❌ Erro ao cadastrar: {str(e)}", "erro")

    def atualizar_produto(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get().strip()
        preco = self.txtPreco.get().strip()

        if not codigo or not nome or not preco:
            messagebox.showwarning("Aviso", "Selecione um produto e preencha todos os campos!")
            return

        preco_valido = self.validar_preco(preco)
        if preco_valido is None:
            messagebox.showwarning("Aviso", "Por favor, insira um preço válido!")
            return

        try:
            self.db.atualizar_dados(codigo, nome, preco_valido)
            self.atualizar_status(f"✅ Produto atualizado com sucesso!", "sucesso")
            self.carregar_dados_iniciais()
            self.limpar_tela()
        except Exception as e:
            self.atualizar_status(f"❌ Erro ao atualizar: {str(e)}", "erro")

    def excluir_produto(self):
        codigo = self.txtCodigo.get()

        if not codigo:
            messagebox.showwarning("Aviso", "Selecione um produto para excluir!")
            return

        if messagebox.askyesno("Confirmar exclusão", "Tem certeza que deseja excluir este produto?"):
            try:
                self.db.deletar_dados(codigo)
                self.atualizar_status(f"✅ Produto excluído com sucesso!", "sucesso")
                self.carregar_dados_iniciais()
                self.limpar_tela()
            except Exception as e:
                self.atualizar_status(f"❌ Erro ao excluir: {str(e)}", "erro")

    def limpar_tela(self):
        self.txtCodigo.delete(0, tk.END)
        self.txtNome.delete(0, tk.END)
        self.txtPreco.delete(0, tk.END)
        self.txtNome.focus()

    def apresentarRegistrosSelecionados(self, event):
        selecao = self.tree.selection()
        if selecao:
            item = selecao[0]
            valores = self.tree.item(item, "values")
            
            self.txtCodigo.delete(0, tk.END)
            self.txtCodigo.insert(tk.END, valores[0])
            
            self.txtNome.delete(0, tk.END)
            self.txtNome.insert(tk.END, valores[1])
            
            preco_limpo = valores[2].replace('R$', '').strip()
            self.txtPreco.delete(0, tk.END)
            self.txtPreco.insert(tk.END, preco_limpo)

    def carregar_dados_iniciais(self):
        # Limpar tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Limpar campo de pesquisa
        self.txtPesquisa.delete(0, tk.END)

        try:
            registros = self.db.selecionar_dados()

            # Inserir dados com cores alternadas
            for i, registro in enumerate(registros):
                tag = 'linha1' if i % 2 == 0 else 'linha2'
                registro_formatado = list(registro)
                registro_formatado[2] = f"R$ {float(registro[2]):.2f}"
                self.tree.insert("", tk.END, values=registro_formatado, tags=(tag,))

            self.atualizar_status(f"📊 Total de {len(registros)} produtos carregados")

        except Exception as e:
            self.atualizar_status(f"❌ Erro ao carregar dados: {str(e)}", "erro")

# Criando interface gráfica
if __name__ == "__main__":
    root = tk.Tk()
    app_bd = AppBD()
    app_gui = MeuEstoque(root, app_bd)
    root.mainloop()