from psycopg2 import Error
from conectar import conexao, meu_cursor

# Serve para criar a classe de conexão com o banco de dados e as operações básicas de CRUD (Create, Read, Update, Delete)

class AppBD:
    def __init__(self):
        self.conn = None
        self.cur = None
        self.connect_to_db()

    def connect_to_db(self):
        self.conn = conexao
        self.cur = meu_cursor
        print("Conexão com o banco de dados estabelecida com sucesso!")

    def selecionar_dados(self):
        try:
            self.cur.execute("SELECT * FROM PRODUTO ORDER BY CODIGO;")
            registros = self.cur.fetchall()
            return registros
        except (Exception, Error) as error:
            print("Erro ao selecionar dados:", error)
            return []

    def inserir_dados(self, nome, preco):
        try:
            self.cur.execute("""
                INSERT INTO PRODUTO (NOME, PRECO) VALUES (%s, %s)
                """, (nome, preco))
            self.conn.commit()
            print(f"Produto '{nome}' inserido com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao inserir dados:", error)

    def atualizar_dados(self, codigo, nome, preco):
        try:
            self.cur.execute("""
                UPDATE PRODUTO SET NOME = %s, PRECO = %s WHERE CODIGO = %s
                """, (nome, preco, codigo))
            self.conn.commit()
            print(f"Produto com código {codigo} atualizado com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao atualizar dados:", error)

    def deletar_dados(self, codigo):
        try:
            self.cur.execute("""
                DELETE FROM PRODUTO WHERE CODIGO = %s
                """, (codigo,))
            self.conn.commit()
            print(f"Produto com código {codigo} deletado com sucesso!")
        except (Exception, Error) as error:
            print("Erro ao deletar dados:", error)

if __name__ == "__main__":
    app_bd = AppBD()
    print("AppBD executado diretamente!")