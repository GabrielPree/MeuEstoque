import psycopg2

# Configurações de conexão com o banco de dados PostgreSQL
# Certifique-se de ajustar os parâmetros de conexão conforme necessário para o seu ambiente
conexao = psycopg2.connect(
    host="localhost",
    database="produtos_db",
    user="admin",
    password="admin123"
)

meu_cursor = conexao.cursor()