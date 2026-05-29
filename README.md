# 📞 Python Tkinter & PostgreSQL Contact Manager (Agenda)

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL Badge">
  <img src="https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge" alt="Tkinter Badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License">
</div>

---

Uma aplicação desktop moderna de **gerenciamento de contatos (Agenda)** construída em **Python**, utilizando a biblioteca gráfica **Tkinter** para a interface de usuário e o banco de dados relacional **PostgreSQL** para persistência robusta dos dados.

Este projeto demonstra a estruturação de um fluxo CRUD completo integrado de ponta a ponta, com separação de responsabilidades (Interface vs. Acesso a Dados) e tratamento de segurança para proteção de dados sensíveis.

---

## 🎯 Destaques Arquiteturais & Boas Práticas

Para ir além de um script acadêmico simples, o projeto foi estruturado seguindo conceitos fundamentais de desenvolvimento profissional:

- **Programação Orientada a Objetos (POO):** Toda a interface do usuário e comportamento da aplicação são encapsulados na classe `AgendaApp`, facilitando a manutenção e extensão do código.
- **Separação de Responsabilidades (De-coupling):** A lógica de conexão e estruturação de tabelas do banco de dados fica em `database.py`, enquanto a lógica de renderização de tela e validação de dados fica em `main.py`.
- **Segurança da Informação (Zero Leak):** Configuração segura de conexões via variáveis de ambiente com arquivo `.env`, garantindo que credenciais locais de banco de dados nunca sejam expostas em repositórios públicos.
- **Resiliência de Inicialização:** A aplicação detecta e cria a tabela `contatos` automaticamente na primeira inicialização do banco, garantindo que o programa rode sem necessidade de scripts SQL manuais de setup.

---

## 🚀 Funcionalidades

- **Cadastro Completo (Create):** Criação de contatos contendo Nome (campo obrigatório com validação), Telefone e E-mail.
- **Visualização Dinâmica (Read):** Exibição de todos os contatos em uma tabela interativa (`Treeview`), com atualização automática.
- **Edição Direta (Update):** Permite selecionar qualquer contato na tabela e atualizar suas informações instantaneamente no banco de dados.
- **Remoção Segura (Delete):** Exclusão permanente de contatos da base de dados PostgreSQL através da interface.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3](https://www.python.org/)
- **Interface Gráfica:** [Tkinter](https://docs.python.org/3/library/tkinter.html) (Biblioteca Nativa)
- **Banco de Dados:** [PostgreSQL 14+](https://www.postgresql.org/)
- **Driver de Conexão:** `psycopg2`
- **Ambiente Isolado:** Virtual Environment (`venv`)

---

## 🔧 Configuração e Execução Local

### 1. Pré-requisitos
Certifique-se de possuir o **Python 3** e o **PostgreSQL** instalados e rodando na sua máquina.

### 2. Configurar as Variáveis de Ambiente
Renomeie o arquivo `.env.example` para `.env` no diretório raiz do projeto e ajuste as credenciais com as suas configurações locais do PostgreSQL:
```env
DB_NAME=agenda
DB_USER=seu_usuario_postgres
DB_PASSWORD=sua_senha_postgres
DB_HOST=localhost
DB_PORT=5432
```

### 3. Instalar e Executar (Usando Ambiente Virtual)

```bash
# Entrar no diretório do projeto
cd agenda

# Criar ambiente virtual
python3 -m venv .venv

# Ativar ambiente virtual
source .venv/bin/activate  # No Linux/WSL
# .venv\Scripts\activate   # No Windows (Prompt comum)

# Instalar dependências necessárias
pip install psycopg2-binary

# Executar a aplicação
python main.py
```
