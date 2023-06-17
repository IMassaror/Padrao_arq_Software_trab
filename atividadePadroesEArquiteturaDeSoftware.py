class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def ano_publicacao(self):
        return self._ano_publicacao

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, status):
        self._disponivel = status


class Usuario:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email
        self._livros_emprestados = []

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    def emprestar_livro(self, livro):
        if livro.disponivel:
            livro.disponivel = False
            self._livros_emprestados.append(livro)
            print(f"Livro '{livro.titulo}' emprestado para {self._nome}.")
        else:
            print(f"Livro '{livro.titulo}' não está disponível.")

    def devolver_livro(self, livro):
        if livro in self._livros_emprestados:
            self._livros_emprestados.remove(livro)
            livro.disponivel = True
            print(f"Livro '{livro.titulo}' devolvido por {self._nome}.")
        else:
            print(f"Livro '{livro.titulo}' não foi emprestado por {self._nome}.")


class Biblioteca:
    def __init__(self):
        self._livros = []
        self._usuarios = []

    def adicionar_livro(self, livro):
        if livro.disponivel:
            self._livros.append(livro)
            print(f"Livro '{livro.titulo}' adicionado à biblioteca.")
        else:
            print(f"Livro '{livro.titulo}' não está disponível.")

    def remover_livro(self, livro):
        if livro in self._livros:
            self._livros.remove(livro)
            print(f"Livro '{livro.titulo}' removido da biblioteca.")
        else:
            print(f"Livro '{livro.titulo}' não está na biblioteca.")

    def buscar_livro(self, titulo):
        for livro in self._livros:
            if livro.titulo == titulo:
                return livro
        return None

    def adicionar_usuario(self, usuario):
        self._usuarios.append(usuario)
        print(f"Usuário '{usuario.nome}' adicionado à biblioteca.")

    def remover_usuario(self, usuario):
        if usuario in self._usuarios:
            self._usuarios.remove(usuario)
            print(f"Usuário '{usuario.nome}' removido da biblioteca.")
        else:
            print(f"Usuário '{usuario.nome}' não está registrado na biblioteca.")

    def buscar_usuario(self, nome):
        for usuario in self._usuarios:
            if usuario.nome == nome:
                return usuario
        return None


# Exemplo de uso do código:

# Criação de alguns livros
livro1 = Livro("Python para Iniciantes", "John Smith", 2018)
livro2 = Livro("Python Avançado", "Jane Doe", 2020)

# Criação de usuários
usuario1 = Usuario("Alice", "alice@example.com")
usuario2 = Usuario("Bob", "bob@example.com")

# Criação da biblioteca
biblioteca = Biblioteca()

# Adicionar livros à biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Adicionar usuários à biblioteca
biblioteca.adicionar_usuario(usuario1)
biblioteca.adicionar_usuario(usuario2)

# Empréstimo de livro
usuario1.emprestar_livro(livro1)

# Tentativa de empréstimo de livro indisponível
usuario2.emprestar_livro(livro1)

# Devolução de livro
usuario1.devolver_livro(livro1)

# Remoção de livro
biblioteca.remover_livro(livro2)

# Remoção de usuário
biblioteca.remover_usuario(usuario2)

# Busca de livro e usuário
livro_encontrado = biblioteca.buscar_livro("Python para Iniciantes")
usuario_encontrado = biblioteca.buscar_usuario("Alice")

# Exemplo de uso dos métodos de acesso
if livro_encontrado:
    print(livro_encontrado.titulo)
if usuario_encontrado:
    print(usuario_encontrado.nome)

