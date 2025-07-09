
# 🛠️ Mini ERP em Python com POO e SQLite

Um sistema ERP simples e modular desenvolvido em Python, com persistência de dados via SQLite e programação orientada a objetos (POO). Ideal para estudo e prática de conceitos básicos de sistemas corporativos.

---

## 🚀 Funcionalidades

### Módulos

- 👤 **Usuários**
  - Cadastro de usuários com validação
  - Login com senha criptografada (SHA-256)
  
- 📇 **CRM (Clientes)**
  - Cadastrar, listar, buscar, editar e excluir clientes
  
- 💰 **Finanças**
  - Adicionar receitas e despesas
  - Listar lançamentos financeiros
  - Calcular saldo total

---

## 📂 Estrutura do Projeto

```
mini_erp/
├── main.py          # Programa principal, menu e fluxo
├── database.py      # Conexão e criação das tabelas SQLite
├── usuario.py       # Módulo usuários (cadastro e autenticação)
├── crm.py           # Módulo clientes (CRUD completo)
├── financeiro.py    # Módulo finanças (lançamentos e saldo)
├── utils.py         # Funções auxiliares (hash, validação, formatação)
├── requirements.txt # Dependências do projeto
└── .gitignore       # Arquivos ignorados pelo Git
```

---

## 🛠️ Como Rodar

### Pré-requisitos

- Python 3 instalado (recomendo 3.8+)
- Terminal / prompt de comando

### Passos

1. Clone ou baixe o projeto

2. Instale as dependências (apenas PyInstaller é externa)

```bash
pip install -r requirements.txt
```

3. Execute o programa

```bash
python main.py
```

---

## 🔐 Segurança

- As senhas dos usuários são armazenadas usando **hash SHA-256** para maior segurança.
- Cadastro e autenticação são feitos de forma segura via banco de dados SQLite.

---

## 🎛️ Uso

### 🔐 Tela inicial
- Faça login com um usuário existente
- Ou cadastre um novo usuário

### 📋 Menu principal após login
1. **CRM**
2. **Finanças**
3. **Sair**

### 🗂️ CRM
- ✅ Cadastrar cliente  
- 🔍 Buscar cliente por nome  
- 📄 Listar clientes  
- ✏️ Editar cliente  
- ❌ Excluir cliente  

### 💰 Finanças
- ➕ Adicionar receita ou despesa  
- 📊 Listar lançamentos  
- 💵 Mostrar saldo total  

---

## 💡 Tecnologias usadas

- 🐍 **Python 3**
- 🗃️ **SQLite** (banco de dados leve e integrado)
- 🧱 **POO** (Programação Orientada a Objetos)
- 🔐 **Hashlib** (criptografia de senha)
- 📦 **PyInstaller** (criação de executável `.exe`)

---

## 📦 Gerando um executável `.exe`

Para criar um executável do programa e rodar sem precisar do Python instalado:

```bash
pip install pyinstaller
pyinstaller --onefile --console main.py
```

✅ O arquivo `.exe` será gerado na pasta `dist/main.exe`.

---

## 📝 .gitignore

O projeto ignora:

- Arquivos `.pyc` e `__pycache__/`
- Banco de dados local (`erp.db`)
- Pastas geradas pelo PyInstaller (`dist/`, `build/`)
- Ambientes virtuais (`venv/`, `env/`)
- Arquivos de sistema (`.DS_Store`, `Thumbs.db`)

---

## 🎯 Próximos Passos / Melhorias Futuras

- 🖼️ Interface gráfica com Tkinter  
- 🧾 CRUD completo no módulo financeiro (editar/excluir lançamentos)  
- 📑 Exportação de relatórios em CSV ou PDF  
- ✅ Validações mais robustas (emails, valores etc)  
- ☁️ Backup automático do banco de dados

---

## 👨‍💻 Autor

**Nicolas Cabral** — Projeto feito com ajuda do **ChatGPT** 🤖

---

## 📄 Licença

Projeto livre para uso educacional e pessoal.

💬 Se quiser ajuda para melhorar, empacotar ou evoluir esse sistema, é só pedir! 🚀
