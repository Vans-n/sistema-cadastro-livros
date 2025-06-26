import json
import os

class Livro:
    def __init__(self, titulo, autor, ano_edicao, editora, data_cadastro):
        self.titulo = titulo
        self.autor = autor
        self.ano_edicao = ano_edicao
        self.editora = editora
        self.data_cadastro = data_cadastro

    def exibir(self):
        print(f"Título: {self.titulo}")
        print(f"Autor(a): {self.autor}")
        print(f"Ano da Edição: {self.ano_edicao}")
        print(f"Editora: {self.editora}")
        print(f"Data de Cadastro: {self.data_cadastro}")

    def para_dict(self):
        return {
            "titulo": self.titulo,
            "autor": self.autor,
            "ano_edicao": self.ano_edicao,
            "editora": self.editora,
            "data_cadastro": self.data_cadastro
        }

    @staticmethod
    def de_dict(dados):
        return Livro(
            dados["titulo"],
            dados["autor"],
            dados["ano_edicao"],
            dados["editora"],
            dados["data_cadastro"]
        )

class SistemaBiblioteca:
    def __init__(self):
        self.biblioteca = []
        self.arquivo = "biblioteca.json"
        self.carregar_dados()

    def salvar_dados(self):
        with open(self.arquivo, "w") as f:
            json.dump([livro.para_dict() for livro in self.biblioteca], f, indent=4)

    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                dados = json.load(f)
                self.biblioteca = [Livro.de_dict(item) for item in dados]

    def cadastrar_livro(self):
        print("\nCadastro de Livro 📙")
        titulo = input("Título: ")
        autor = input("Autor(a): ")
        ano = input("Ano da Edição: ")
        editora = input("Editora: ")
        data = input("Data de Cadastro (dd/mm/aaaa): ")
        livro = Livro(titulo, autor, ano, editora, data)
        self.biblioteca.append(livro)
        self.salvar_dados()
        print("Livro cadastrado com sucesso!\n")

    def buscar_livro(self):
        print("\nBuscar Livro 🔎")
        busca = input("Digite o nome do livro: ")
        for livro in self.biblioteca:
            if livro.titulo.lower() == busca.lower():
                print("\nLivro encontrado:\n")
                livro.exibir()

                opcao = input("\nDeseja editar as informações? (s/n): ")
                if opcao.lower() == 's':
                    self.editar_livro(livro)
                    self.salvar_dados()
                return
        print("Livro não encontrado.\n")

    def editar_livro(self, livro):
        print("\n Edição de Livro ✏")
        novo_titulo = input(f"Novo título (ou Enter para manter '{livro.titulo}'): ")
        novo_autor = input(f"Novo autor (ou Enter para manter '{livro.autor}'): ")
        novo_ano = input(f"Novo ano da edição (ou Enter para manter '{livro.ano_edicao}'): ")
        nova_editora = input(f"Nova editora (ou Enter para manter '{livro.editora}'): ")
        nova_data = input(f"Nova data de cadastro (ou Enter para manter '{livro.data_cadastro}'): ")

        if novo_titulo: livro.titulo = novo_titulo
        if novo_autor: livro.autor = novo_autor
        if novo_ano: livro.ano_edicao = novo_ano
        if nova_editora: livro.editora = nova_editora
        if nova_data: livro.data_cadastro = nova_data

        print("Informações atualizadas com sucesso!\n")

def menu():
    sistema = SistemaBiblioteca()
    while True:
        print("1. Cadastrar Livro")
        print("2. Buscar Livro")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            sistema.cadastrar_livro()
        elif opcao == '2':
            sistema.buscar_livro()
        elif opcao == '3':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!\n")

menu()
