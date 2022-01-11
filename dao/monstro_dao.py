from conexao.database import DataBase


class MonstrosDao:

    def listar_monstros_tabela(self):
        con = DataBase()
        sql = "SELECT * FROM tb_repositorio_monstros"
        resultado = con.executa_consulta(sql)
        return resultado

    def carregar_monstros(self, nome_monstro):
        con = DataBase()
        sql = f"SELECT * FROM tb_repositorio_monstros WHERE nome_monstro='{nome_monstro}'"
        resultado = con.executa_consulta(sql)
        return resultado

    def pesquisar_monstro_tabela(self, nome_monstro):
        con = DataBase()
        sql = f"SELECT * FROM tb_repositorio_monstros WHERE nome_monstro LIKE '%{nome_monstro}%'"
        resultado = con.executa_consulta(sql)
        return resultado

    def cadastrar_monstros(self, nome_monstro, tipo_monstro, classe_armadura, pontos_vida, pontos_vida_atual,
                           deslocamento, nivel_desafio, referencia):
        con = DataBase()
        sql = f"INSERT INTO tb_repositorio_monstros (nome_monstro, tipo_monstro, classe_armadura, pontos_vida," \
              f"pontos_vida_atual, deslocamento, nivel_desafio, referencia) VALUES ('{nome_monstro}'," \
              f"'{tipo_monstro}', {classe_armadura}, {pontos_vida}, {pontos_vida_atual}, '{deslocamento}'," \
              f"{nivel_desafio}, '{referencia}')"
        con.executa_query(sql)

    def alterar_monstro(self, id, nome_monstro, tipo_monstro, classe_armadura, pontos_vida, pontos_vida_atual,
                           deslocamento, nivel_desafio, referencia):
        con = DataBase()
        sql = f"UPDATE tb_repositorio_monstros SET nome_monstro='{nome_monstro}', tipo_monstro='{tipo_monstro}'" \
              f", classe_armadura={classe_armadura}, pontos_vida='{pontos_vida}'," \
              f"pontos_vida_atual={pontos_vida_atual}, deslocamento='{deslocamento}'," \
              f"nivel_desafio='{nivel_desafio}', referencia='{referencia}' WHERE id_repositorio_monstros={id}"
        print(sql)
        con.executa_query(sql)

    def excluir_monstro(self, id):
        con = DataBase()
        sql = f"DELETE FROM tb_repositorio_monstros WHERE id_repositorio_monstros={id}"
        con.executa_query(sql)
