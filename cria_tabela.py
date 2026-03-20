from conectar import conexao, meu_cursor

# Criar a tabela "produtos"
meu_cursor.execute("""
    CREATE TABLE IF NOT EXISTS PRODUTO (
        CODIGO SERIAL PRIMARY KEY,
        NOME VARCHAR(100) NOT NULL,
        PRECO NUMERIC(10, 2) NOT NULL
    );
""")

# just in case
conexao.commit()
print("Tabela 'PRODUTO' criada com sucesso!")
conexao.close()