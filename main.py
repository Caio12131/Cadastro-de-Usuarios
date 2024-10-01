import tkinter as tk
from tkinter import messagebox, simpledialog
import sqlite3

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Cadastros")
        
        # Definindo o tamanho da janela
        self.root.geometry("400x400")  # Largura x Altura

        # Conectando ao banco de dados SQLite
        self.conn = sqlite3.connect("cadastro_usuarios.db")
        self.create_table()

        # Adicionando um título com fundo púrpura
        self.title_frame = tk.Frame(root, bg="purple")
        self.title_frame.pack(fill=tk.X)

        self.title_label = tk.Label(self.title_frame, text="Cadastro de Usuários", bg="purple", fg="white", font=("Concert One", 16))
        self.title_label.pack(pady=10)

        # Criando um frame para os campos de entrada
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        # Labels e Entradas
        self.label_nome = tk.Label(self.input_frame, text="Nome:", font=("Concert One", 12))
        self.label_nome.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.entry_nome = tk.Entry(self.input_frame, font=("Concert One", 12))
        self.entry_nome.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        self.label_cpf = tk.Label(self.input_frame, text="CPF:", font=("Concert One", 12))
        self.label_cpf.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.entry_cpf = tk.Entry(self.input_frame, font=("Concert One", 12))
        self.entry_cpf.grid(row=1, column=1, padx=10, pady=5, sticky='ew')

        self.label_senha = tk.Label(self.input_frame, text="Senha:", font=("Concert One", 12))
        self.label_senha.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.entry_senha = tk.Entry(self.input_frame, show="*", font=("Concert One", 12))
        self.entry_senha.grid(row=2, column=1, padx=10, pady=5, sticky='ew')

        self.label_endereco = tk.Label(self.input_frame, text="Endereço:", font=("Concert One", 12))
        self.label_endereco.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.entry_endereco = tk.Entry(self.input_frame, font=("Concert One", 12))
        self.entry_endereco.grid(row=3, column=1, padx=10, pady=5, sticky='ew')

        self.label_telefone = tk.Label(self.input_frame, text="Telefone:", font=("Concert One", 12))
        self.label_telefone.grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.entry_telefone = tk.Entry(self.input_frame, font=("Concert One", 12))
        self.entry_telefone.grid(row=4, column=1, padx=10, pady=5, sticky='ew')

        # Botão para cadastrar
        self.btn_cadastrar = tk.Button(root, text="Cadastrar", command=self.cadastrar, bg="purple", fg="white", font=("Concert One", 12), borderwidth=0, highlightthickness=0, relief="flat")
        self.btn_cadastrar.pack(pady=5)
        self.btn_cadastrar.bind("<Enter>", self.on_enter)
        self.btn_cadastrar.bind("<Leave>", self.on_leave)

        # Campo de pesquisa
        self.label_pesquisa = tk.Label(root, text="Pesquisar Nome:", font=("Concert One", 12))
        self.label_pesquisa.pack(pady=5)
        self.entry_pesquisa = tk.Entry(root, show="*", font=("Concert One", 12))  # Asterisco para ocultar a senha
        self.entry_pesquisa.pack(pady=5)

        # Botão para pesquisar
        self.btn_pesquisar = tk.Button(root, text="Pesquisar", command=self.pesquisar, bg="purple", fg="white", font=("Concert One", 12), borderwidth=0, highlightthickness=0, relief="flat")
        self.btn_pesquisar.pack(pady=5)
        self.btn_pesquisar.bind("<Enter>", self.on_enter)
        self.btn_pesquisar.bind("<Leave>", self.on_leave)

        # Botão para redefinir senha
        self.btn_redefinir_senha = tk.Button(root, text="Redefinir Senha", command=self.redefinir_senha, bg="purple", fg="white", font=("Concert One", 12), borderwidth=0, highlightthickness=0, relief="flat")
        self.btn_redefinir_senha.pack(pady=5)
        self.btn_redefinir_senha.bind("<Enter>", self.on_enter)
        self.btn_redefinir_senha.bind("<Leave>", self.on_leave)

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                endereco TEXT,
                telefone TEXT
            )
        ''')
        self.conn.commit()

    def on_enter(self, event):
        event.widget['bg'] = 'darkviolet'  # Mudando a cor de fundo ao passar o mouse

    def on_leave(self, event):
        event.widget['bg'] = 'purple'  # Retornando à cor original ao sair

    def cadastrar(self):
        nome = self.entry_nome.get().strip()
        cpf = self.entry_cpf.get().strip()
        senha = self.entry_senha.get().strip()
        endereco = self.entry_endereco.get().strip()
        telefone = self.entry_telefone.get().strip()

        if nome and cpf and senha and endereco and telefone:
            try:
                # Se tudo estiver ok, cadastra o usuário no banco de dados
                cursor = self.conn.cursor()
                cursor.execute('INSERT INTO usuarios (nome, cpf, senha, endereco, telefone) VALUES (?, ?, ?, ?, ?)',
                               (nome, cpf, senha, endereco, telefone))
                self.conn.commit()
                messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")
                self.limpar_campos()
            except sqlite3.IntegrityError:
                messagebox.showwarning("Erro", "CPF já cadastrado no sistema.")
        else:
            messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_cpf.delete(0, tk.END)
        self.entry_senha.delete(0, tk.END)
        self.entry_endereco.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)
        self.entry_pesquisa.delete(0, tk.END)

    def pesquisar(self):
        nome_pesquisa = self.entry_pesquisa.get().strip()
        if nome_pesquisa:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE nome = ?', (nome_pesquisa,))
            usuario = cursor.fetchone()
            if usuario:
                self.solicitar_senha(usuario)
            else:
                messagebox.showwarning("Usuário não encontrado", "Usuário não encontrado.")
        else:
            messagebox.showwarning("Erro", "Por favor, insira um nome para pesquisa.")

    def solicitar_senha(self, usuario):
        senha_digitada = simpledialog.askstring("Senha", "Digite a senha:", show="*")  # Asterisco para ocultar
        if senha_digitada == usuario[3]:  # Verifica se a senha está correta
            self.exibir_informacoes(usuario)
        else:
            messagebox.showwarning("Erro", "Senha incorreta!")

    def exibir_informacoes(self, usuario):
        info_window = tk.Toplevel(self.root)  # Cria uma nova janela
        info_window.title("Informações do Usuário")

        # Informações do usuário
        tk.Label(info_window, text=f"Nome: {usuario[1]}", font=("Concert One", 12)).pack(pady=5)
        tk.Label(info_window, text=f"CPF: {usuario[2]}", font=("Concert One", 12)).pack(pady=5)
        tk.Label(info_window, text=f"Endereço: {usuario[4]}", font=("Concert One", 12)).pack(pady=5)
        tk.Label(info_window, text=f"Telefone: {usuario[5]}", font=("Concert One", 12)).pack(pady=5)

    def redefinir_senha(self):
        nome_pesquisa = self.entry_pesquisa.get().strip()
        if nome_pesquisa:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE nome = ?', (nome_pesquisa,))
            usuario = cursor.fetchone()
            if usuario:
                senha_antiga = simpledialog.askstring("Senha Antiga", "Digite a senha antiga:", show="*")
                if senha_antiga == usuario[3]:  # Verifica a senha antiga
                    nova_senha = simpledialog.askstring("Nova Senha", "Digite a nova senha:", show="*")
                    if nova_senha:
                        # Atualiza a senha no registro
                        cursor.execute('UPDATE usuarios SET senha = ? WHERE id = ?', (nova_senha, usuario[0]))
                        self.conn.commit()
                        messagebox.showinfo("Sucesso", "Senha redefinida com sucesso!")
                    else:
                        messagebox.showwarning("Erro", "Nova senha não pode ser vazia.")
                else:
                    messagebox.showwarning("Erro", "Senha antiga incorreta!")
            else:
                messagebox.showwarning("Erro", "Usuário não encontrado.")
        else:
            messagebox.showwarning("Erro", "Por favor, insira um nome para redefinir a senha.")

    def __del__(self):
        self.conn.close()  # Fecha a conexão com o banco de dados ao finalizar

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()
