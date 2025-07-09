from database import conectar
from datetime import datetime

class Lancamento:
    def __init__(self, tipo, descricao, valor, data=None):
        self.tipo = tipo
        self.descricao = descricao
        self.valor = valor
        self.data = data if data else datetime.now().strftime("%Y-%m-%d")

    def adicionar_lancamento(self):
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO lancamentos (tipo, descricao, valor, data) VALUES (?, ?, ?, ?)",
                       (self.tipo, self.descricao, self.valor, self.data))
        conn.commit()
        conn.close()
        print("Lançamento adicionado com sucesso!")

    @staticmethod
    def listar_lancamentos():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lancamentos")
        lancamentos = cursor.fetchall()
        conn.close()
        return lancamentos

    @staticmethod
    def saldo_total():
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT tipo, valor FROM lancamentos")
        dados = cursor.fetchall()
        conn.close()

        saldo = 0
        for tipo, valor in dados:
            if tipo.lower() == "receita":
                saldo += valor
            elif tipo.lower() == "despesa":
                saldo -= valor
        return saldo
