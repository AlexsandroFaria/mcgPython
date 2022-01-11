from conexao.database import DataBase


class PersonagemDao:

    def listar_personagem_tabela(self):
        con = DataBase()
        sql = "SELECT id_personagem, nome_personagem, nome_classe, nome_raca, dados_vida, total_pontos_vida," \
              "pontos_vida_atual, pontos_experiencia, nivel, ponto_heroico FROM tb_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def cadastrar_personagem(self, nome_personagem, nome_classe, nome_raca, dados_vida, total_pontos_vida,
                             pontos_vida_atual, pontos_experiencia, nivel, ponto_heroico, situacao):
        con = DataBase()
        sql = f"INSERT INTO tb_personagem (nome_personagem, nome_classe, nome_raca, dados_vida, total_pontos_vida," \
              f"pontos_vida_atual, pontos_experiencia, nivel, ponto_heroico, situacao) VALUES ('{nome_personagem}'," \
              f"'{nome_classe}', '{nome_raca}', '{dados_vida}', {total_pontos_vida}, {pontos_vida_atual}," \
              f"{pontos_experiencia}, {nivel}, {ponto_heroico}, '{situacao}')"
        con.executa_query(sql)

    def popular_combo_nome_personagem(self):
        con = DataBase()
        sql = f"SELECT nome_personagem FROM tb_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def carregar_campos_personagem(self, nome_personagem):
        con = DataBase()
        sql = f"SELECT * FROM tb_personagem WHERE nome_personagem='{nome_personagem}'"
        resultado = con.executa_consulta(sql)
        return resultado

    def alterar_cadastro_personagem(self, id_personagem, nome_personagem, nome_classe, nome_raca, dados_vida,
                                    total_pontos_vida, pontos_vida_atual, pontos_experiencia, nivel, ponto_heroico):
        con = DataBase()
        sql = f"UPDATE tb_personagem SET nome_personagem='{nome_personagem}'," \
              f"nome_classe='{nome_classe}', nome_raca='{nome_raca}', dados_vida='{dados_vida}'," \
              f"total_pontos_vida={total_pontos_vida}, pontos_vida_atual={pontos_vida_atual}," \
              f"pontos_experiencia={pontos_experiencia}, nivel={nivel}," \
              f"ponto_heroico={ponto_heroico} WHERE id_personagem={id_personagem}"
        con.executa_query(sql)

    def excluir_personagem(self, id_personagem):
        con = DataBase()
        sql = f"DELETE FROM tb_personagem WHERE id_personagem={id_personagem}"
        con.executa_query(sql)
