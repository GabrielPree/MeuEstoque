from faker import Faker
from conectar import conexao, meu_cursor

# Antes de rodar este script, certifique-se de que a tabela "PRODUTO" já foi criada usando o script cria_tabela.py
# Este script serve para gerar dados de teste e inserir na tabela "PRODUTO"

# configurando gerador
fake = Faker('pt_BR')

# Mude o range para gerar mais ou menos produtos

for _ in range(5):
    nome = fake.word().capitalize()
    preco = round(fake.random_number(digits=5) / 100, 2)  # Gerar um preço aleatório
    print (f"Gerando produto: {nome} - R${preco}")
    meu_cursor.execute("""
        INSERT INTO PRODUTO (NOME, PRECO) VALUES (%s, %s)
        """, (nome, preco))
                    
    conexao.commit()
print("Dados inseridos com sucesso!")
meu_cursor.close()
conexao.close()