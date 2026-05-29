import os
import psycopg2

# Carrega variáveis de ambiente do arquivo .env local se ele existir
if os.path.exists('.env'):
    with open('.env') as f:
        for line in f:
            if line.strip() and not line.strip().startswith('#'):
                try:
                    key, value = line.strip().split('=', 1)
                    os.environ[key.strip()] = value.strip().strip('"').strip("'")
                except ValueError:
                    pass

def conectar():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "agenda"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", ""),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            telefone VARCHAR(15),
            email VARCHAR(100)
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Executa a criação da tabela ao importar o módulo
criar_tabela()