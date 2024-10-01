import tkinter as tk
from tkinter import messagebox, simpledialog

class CadastroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Cadastros")
        
        # Definindo o tamanho da janela
        self.root.geometry("400x400")  # Largura x Altura

        # Adicionando um título com fundo púrpura
        self.title_frame = tk.Frame(root, bg="purple")
        self.title_frame.pack(fill=tk.X)

        self.title_label = tk.Label(self.title_frame, text="Cadastro de Usuários", bg="purple", fg="white", font=("Concert One", 16))
        self.title_label.pack(pady=10)

        # Lista para armazenar os cadastros
        self.cadastros = []

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
        self.btn_redefinir_senha.pack(pady=1)
        self.btn_redefinir_senha.bind("<Enter>", self.on_enter)
        self.btn_redefinir_senha.bind("<Leave>", self.on_leave)

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
            # Verifica se o CPF já está cadastrado
            for usuario in self.cadastros:
                if usuario[1] == cpf:
                    messagebox.showwarning("Erro", "CPF já cadastrado no sistema.")
                    return

            # Se tudo estiver ok, cadastra o usuário como uma lista
            self.cadastros.append([nome, cpf, senha, endereco, telefone])  # Usando lista em vez de tupla
            messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")
            self.limpar_campos()
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
            for usuario in self.cadastros:
                if usuario[0] == nome_pesquisa:
                    self.solicitar_senha(usuario)
                    return
            messagebox.showwarning("Usuário não encontrado", "Usuário não encontrado.")
        else:
            messagebox.showwarning("Erro", "Por favor, insira um nome para pesquisa.")

    def solicitar_senha(self, usuario):
        senha_digitada = simpledialog.askstring("Senha", "Digite a senha:", show="*")  # Asterisco para ocultar
        if senha_digitada == usuario[2]:  # Verifica se a senha está correta
            self.exibir_informacoes(usuario)
        else:
            messagebox.showwarning("Erro", "Senha incorreta!")

    def exibir_informacoes(self, usuario):
        info_window = tk.Toplevel(self.root)  # Cria uma nova janela
        info_window.title("Informações do Usuário")

        # Informações do usuário
        tk.Label(info_window, text=f"Nome: {usuario[0]}", font=("Concert One", 12)).pack(pady=5)
        tk.Label(info_window, text=f"CPF: {usuario[1]}", font=("Concert One", 12)).pack(pady=5)
        tk.Label(info_window, text=f"Endereço: {usuario[3]}", font=("Concert One", 12)).pack(pady=5)
        tk.Label(info_window, text=f"Telefone: {usuario[4]}", font=("Concert One", 12)).pack(pady=5)

        # Botão para fechar a janela de informações
        btn_fechar = tk.Button(info_window, text="Fechar", command=info_window.destroy, bg="purple", fg="white", font=("Concert One", 12), borderwidth=0, highlightthickness=0, relief="flat")
        btn_fechar.pack(pady=10)

    def redefinir_senha(self):
        nome_redefinir = simpledialog.askstring("Redefinir Senha", "Digite o nome do usuário:")
        if nome_redefinir:
            for usuario in self.cadastros:
                if usuario[0] == nome_redefinir:
                    # Solicita a senha antiga
                    senha_antiga = simpledialog.askstring("Verificação", "Digite a senha antiga:", show="*")
                    if senha_antiga == usuario[2]:  # Verifica a senha antiga
                        nova_senha = simpledialog.askstring("Nova Senha", "Digite a nova senha:", show="*")
                        if nova_senha:
                            # Atualiza a senha no registro
                            usuario[2] = nova_senha  # Agora que usuario é uma lista, isso funcionará
                            messagebox.showinfo("Sucesso", "Senha redefinida com sucesso!")
                        else:
                            messagebox.showwarning("Erro", "Nova senha não pode ser vazia.")
                    else:
                        messagebox.showwarning("Erro", "Senha antiga incorreta!")
                    return

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroApp(root)
    root.mainloop()
