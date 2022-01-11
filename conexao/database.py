import sqlite3
from sqlite3 import Error


class DataBase:

    def conexao_banco(self):
        try:
            self.conn = sqlite3.connect('mastercontrolguide.db')
            self.cur = self.conn.cursor()
        except Error as sqlerro:
            print(f"Erro ao conectar no Banco: {sqlerro}")
        return self.conn

    def close_connection(self):
        try:
            self.conn.close()
        except Error as sqlerro:
            print(f"Erro ao conectar no Banco: {sqlerro}")

    def executa_consulta(self, sql):
        self.conexao_banco()
        self.cur.execute(sql)
        resultado = self.cur.fetchall()
        self.close_connection()
        return resultado

    def executa_query(self, sql):
        self.conexao_banco()
        self.cur.execute(sql)
        self.conn.commit()
        self.close_connection()
