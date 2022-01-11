from conexao.database import DataBase


class RacaDao:

    def listar_raca_tabela(self):
        con = DataBase()
        sql = "SELECT * FROM tb_raca_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def cadastrar_raca(self, raca, referencia):
        con = DataBase()
        sql = f"INSERT INTO tb_raca_personagem (raca, referencia) Values ('{raca}', '{referencia}')"
        con.executa_query(sql)

    def consulta_raca_nome(self, nome_raca):
        con = DataBase()
        sql = f"SELECT raca FROM tb_raca_personagem WHERE raca='{nome_raca}'"
        resultado = con.executa_consulta(sql)
        return resultado

    def pesquisar_raca_nome(self, raca):
        con = DataBase()
        sql = f"SELECT * FROM tb_raca_personagem WHERE raca='{raca}'"
        print(sql)
        resultado = con.executa_consulta(sql)
        return resultado

    def carregar_raca_id(self, id_raca):
        con = DataBase()
        sql = f"SELECT * FROM tb_raca_personagem WHERE id_raca={id_raca}"
        resultado = con.executa_consulta(sql)
        return resultado

    def excluir_raca(self, id_raca):
        con = DataBase()
        sql = f"DELETE FROM tb_raca_personagem WHERE id_raca={id_raca}"
        con.executa_query(sql)

    def popular_combo_raça_nome(self):
        con = DataBase()
        sql = "SELECT raca FROM tb_raca_personagem"
        resultado = con.executa_consulta(sql)
        return resultado
