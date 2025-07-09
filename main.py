from database import criar_tabelas
from usuario import Usuario
from crm import Cliente
from financeiro import Lancamento

def tela_login():
    print("\n--- Login ---")
    email = input("Email: ")
    senha = input("Senha: ")

    usuario = Usuario.autenticar(email, senha)
    if usuario:
        print(f"\nBem-vindo, {usuario[1]}!")
        return True
    else:
        print("Email ou senha inválidos!")
        return False

def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    usuario = Usuario(nome, email, senha)
    usuario.cadastrar()

def menu_crm():
    while True:
        print("\n--- CRM ---")
        print("1. Cadastrar Cliente")
        print("2. Buscar Cliente por Nome")
        print("3. Listar Clientes")
        print("4. Editar Cliente")
        print("5. Excluir Cliente")
        print("6. Voltar")
        op = input("Escolha: ")

        if op == "1":
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            cliente = Cliente(nome, telefone, email)
            cliente.cadastrar_cliente()

        elif op == "2":
            nome = input("Nome para buscar: ")
            resultados = Cliente.buscar_cliente_por_nome(nome)
            for c in resultados:
                print(c)

        elif op == "3":
            clientes = Cliente.listar_clientes()
            for c in clientes:
                print(c)

        elif op == "4":
            id_cliente = int(input("ID do cliente a editar: "))
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo email: ")
            Cliente.editar_cliente(id_cliente, nome, telefone, email)

        elif op == "5":
            id_cliente = int(input("ID do cliente a excluir: "))
            Cliente.excluir_cliente(id_cliente)

        elif op == "6":
            break
