import re
import hashlib
from datetime import datetime

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

def validar_valor(valor_str):
    try:
        valor = float(valor_str)
        return valor >= 0
    except ValueError:
        return False

def formatar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%Y-%m-%d")
        return data.strftime("%d/%m/%Y")
    except:
        return data_str

def cor_texto(texto, cor="verde"):
    cores = {
        "vermelho": "\033[91m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "azul": "\033[94m",
        "fim": "\033[0m"
    }
    return f"{cores.get(cor, '')}{texto}{cores['fim']}"
