from database import conectar
from utils import gerar_hash

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = gerar_hash(senha)

    def cadastrar(self):
        conn = conectar()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
                           (self.nome, self.email, self.senha))
            conn.commit()
            print("Usuário cadastrado com sucesso!")
        except:
            print("Erro: e-mail já cadastrado.")
        finally:
            conn.close()

    @staticmethod
    def autenticar(email, senha):
        senha_hash = gerar_hash(senha)
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha_hash))
        usuario = cursor.fetchone()
        conn.close()
        return usuario
