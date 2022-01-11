from conexao.database import DataBase


class NivelPersonagemDao:

    def carregar_combo_personagem(self):
        con = DataBase()
        sql = "SELECT nome_personagem FROM tb_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def consultar_nivel_personagem(self, nome):
        con = DataBase()
        sql = f"SELECT nivel FROM tb_personagem WHERE nome_personagem='{nome}'"
        resultado = con.executa_consulta(sql)
        return resultado

    def inserir_personagem_nivel(self, nome, nivel_personagem, nivel_facil, nivel_medio, nivel_dificil, nivel_mortal):
        con = DataBase()
        sql = f"INSERT INTO tb_nivel_personagem (nome, nivel_personagem, nivel_facil, nivel_medio, nivel_dificil," \
              f"nivel_mortal) Values ('{nome}', {nivel_personagem}, {nivel_facil}, {nivel_medio}, {nivel_dificil}," \
              f"{nivel_mortal})"
        con.executa_query(sql)

    def carregar_tabela_nivel_personagem(self):
        con = DataBase()
        sql = "SELECT nome, nivel_personagem, nivel_facil, nivel_medio, nivel_dificil, nivel_mortal " \
              " FROM tb_nivel_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def limpar_tabela_nivel_personagem(self):
        con = DataBase()
        sql = "DELETE FROM tb_nivel_personagem"
        con.executa_query(sql)

    def total_nivel_facil(self):
        con = DataBase()
        sql = "SELECT SUM(nivel_facil) FROM tb_nivel_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def total_nivel_medio(self):
        con = DataBase()
        sql = "SELECT SUM(nivel_medio) FROM tb_nivel_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def total_nivel_dificil(self):
        con = DataBase()
        sql = "SELECT SUM(nivel_dificil) FROM tb_nivel_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def total_nivel_mortal(self):
        con = DataBase()
        sql = "SELECT SUM(nivel_mortal) FROM tb_nivel_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def inserir_resultado_calculo_nivel(self, nivel_facil, nivel_medio, nivel_dificil, nivel_mortal):
        con = DataBase()
        sql = f"INSERT INTO tb_nivel_calculo (nivel_facil, nivel_medio, nivel_dificil, nivel_mortal) VALUES " \
              f"({nivel_facil}, {nivel_medio}, {nivel_dificil}, {nivel_mortal})"
        con.executa_query(sql)

    def limpar_calculo_nivel(self):
        con = DataBase()
        sql = "DELETE FROM tb_nivel_calculo"
        con.executa_query(sql)
