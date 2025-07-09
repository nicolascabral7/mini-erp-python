from database import conectar

class Cliente:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def cadastrar_cliente(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)",
                       (self.nome, self.telefone, self.email))
        conn.commit()
        conn.close()
        print("Cliente cadastrado com sucesso!")

    @staticmethod
    def listar_clientes():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        conn.close()
        return clientes

    @staticmethod
    def buscar_cliente_por_nome(nome):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes WHERE nome LIKE ?", ('%' + nome + '%',))
        resultado = cursor.fetchall()
        conn.close()
        return resultado

    @staticmethod
    def editar_cliente(id_cliente, novo_nome, novo_telefone, novo_email):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE clientes
            SET nome = ?, telefone = ?, email = ?
            WHERE id = ?
        """, (novo_nome, novo_telefone, novo_email, id_cliente))
        conn.commit()
        conn.close()
        print("Cliente editado com sucesso!")

    @staticmethod
    def excluir_cliente(id_cliente):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        conn.commit()
        conn.close()
        print("Cliente excluído com sucesso!")
