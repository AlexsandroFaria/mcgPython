from conexao.database import DataBase


class ClasseDao:

    def listar_tabela_classe(self):
        con = DataBase()
        sql = "SELECT * FROM tb_classe_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def cadastrar_classe_personagem(self, nome_classe, referencia):
        con = DataBase()
        sql = f"INSERT INTO tb_classe_personagem (nome_classe, referencia) VALUES ('{nome_classe}', '{referencia}')"
        con.executa_query(sql)

    def pesquisar_classe_nome(self, nome):
        con = DataBase()
        sql = f"SELECT * FROM tb_classe_personagem WHERE nome_classe='{nome}'"
        resultado = con.executa_consulta(sql)
        return resultado

    def carregar_classe_id(self, id):
        con = DataBase()
        sql = f"SELECT * FROM tb_classe_personagem WHERE id_classe={id}"
        resultado = con.executa_consulta(sql)
        return resultado

    def consulta_classe_nome(self, nome):
        con = DataBase()
        sql = f"SELECT nome_classe FROM tb_classe_personagem WHERE nome_classe='{nome}'"
        resultado = con.executa_consulta(sql)
        return resultado

    def excluir_classe(self, id):
        con = DataBase()
        sql = f"DELETE FROM tb_classe_personagem WHERE id_classe={id}"
        con.executa_query(sql)

    def popular_combo_classe_nome(self):
        con = DataBase()
        sql = "SELECT nome_classe FROM tb_classe_personagem"
        resultado = con.executa_consulta(sql)
        return resultado
