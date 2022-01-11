from conexao.database import DataBase


class CombateDao:

    def listar_personagem_batalha(self):
        con = DataBase()
        sql = "SELECT nome_personagem, total_pontos_vida, pontos_vida_atual, nivel, ponto_heroico," \
              "situacao FROM tb_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def carregar_personagem_combate(self, nome):
        con = DataBase()
        sql = f"SELECT nome_personagem, pontos_vida_atual, ponto_heroico FROM tb_personagem WHERE nome_personagem='{nome}'"
        resultado = con.executa_consulta(sql)
        return resultado

    def dano(self, pontos_vida_atual, nome_personagem):
        con = DataBase()
        sql = f"UPDATE tb_personagem SET pontos_vida_atual={pontos_vida_atual} WHERE " \
              f"nome_personagem='{nome_personagem}'"
        con.executa_query(sql)

    def dano_morte(self, pontos_vida_atual, situacao, nome_personagem):
        con = DataBase()
        sql = f"UPDATE tb_personagem SET pontos_vida_atual={pontos_vida_atual}, situacao='{situacao}' WHERE " \
              f"nome_personagem='{nome_personagem}'"
        con.executa_query(sql)

    def cura(self, cura, situacao, nome_personagem):
        con = DataBase()
        sql = f"UPDATE tb_personagem SET pontos_vida_atual={cura}, situacao='{situacao}' WHERE " \
              f"nome_personagem='{nome_personagem}'"
        con.executa_query(sql)

    def alterar_ponto_heroico(self, ponto_heroico, nome_personagem):
        con = DataBase()
        sql = f"UPDATE tb_personagem SET ponto_heroico={ponto_heroico} WHERE nome_personagem='{nome_personagem}'"
        con.executa_query(sql)

    def listar_inserir_monstros_tabela(self):
        con = DataBase()
        sql = "SELECT id_repositorio_monstros, nome_monstro, classe_armadura, pontos_vida_atual, deslocamento, nivel_desafio, referencia " \
              "FROM tb_repositorio_monstros"
        resultado = con.executa_consulta(sql)
        return resultado

    def consultar_monstro_inserir_combate(self, id):
        con = DataBase()
        sql = f"SELECT id_repositorio_monstros, nome_monstro, classe_armadura, pontos_vida_atual, deslocamento, nivel_desafio, referencia " \
              f"FROM tb_repositorio_monstros WHERE id_repositorio_monstros={id}"
        resultado = con.executa_consulta(sql)
        return resultado

    def inserir_monstro_combate(self, nome_monstro_batalha, classe_armadura, pontos_vida_atual, deslocamento,
                                nivel_desafio, referencia, situacao):
        con = DataBase()
        sql = f"INSERT INTO tb_monstro_batalha (nome_monstro_batalha, classe_armadura, pontos_vida_atual," \
              f"deslocamento, nivel_desafio, referencia, situacao) VALUES ('{nome_monstro_batalha}'," \
              f"{classe_armadura}, {pontos_vida_atual}, '{deslocamento}', '{nivel_desafio}', '{referencia}'," \
              f"'{situacao}')"
        con.executa_query(sql)

    def listar_tabela_monstro_combate(self):
        con = DataBase()
        sql = "SELECT * FROM tb_monstro_batalha"
        resultado = con.executa_consulta(sql)
        return resultado

    def pesquisar_monstro_inserir_combate_nome(self, nome):
        con = DataBase()
        sql = f"SELECT id_repositorio_monstros, nome_monstro, classe_armadura, pontos_vida_atual, deslocamento," \
              f"nivel_desafio, referencia FROM tb_repositorio_monstros WHERE nome_monstro LIKE '%{nome}%'"
        resultado = con.executa_consulta(sql)
        return resultado

    def apagar_registros_tabela_montro_combate(self):
        con = DataBase()
        sql = "DELETE FROM tb_monstro_batalha"
        con.executa_query(sql)

    def carregar_monstro_combate(self, id):
        con = DataBase()
        sql = f"SELECT id_monstro_batalha, nome_monstro_batalha, pontos_vida_atual FROM tb_monstro_batalha WHERE " \
              f"id_monstro_batalha={id}"
        resultado = con.executa_consulta(sql)
        return resultado

    def dano_morte_monstro(self, dano_sofrido, situacao, id):
        con = DataBase()
        sql = f"UPDATE tb_monstro_batalha SET pontos_vida_atual={dano_sofrido}, situacao='{situacao}' " \
              f"WHERE id_monstro_batalha={id}"
        con.executa_query(sql)

    def dano_monstro(self, dano_sofrido, id):
        con = DataBase()
        sql = f"UPDATE tb_monstro_batalha SET pontos_vida_atual={dano_sofrido} WHERE id_monstro_batalha={id}"
        con.executa_query(sql)

    def cura_monstro(self, cura, situacao, id):
        con = DataBase()
        sql = f"UPDATE tb_monstro_batalha SET pontos_vida_atual={cura}, situacao='{situacao}' " \
              f" WHERE id_monstro_batalha={id}"
        con.executa_query(sql)

    def popular_combo_personagem(self):
        con = DataBase()
        sql = f"SELECT nome_personagem FROM tb_personagem"
        resultado = con.executa_consulta(sql)
        return resultado

    def popular_combo_monstro(self):
        con = DataBase()
        sql = f"SELECT nome_monstro FROM tb_repositorio_monstros"
        resultado = con.executa_consulta(sql)
        return resultado

    def limpar_tabela_iniciativa(self):
        con = DataBase()
        sql = "DELETE FROM tb_iniciativa"
        con.executa_query(sql)

    def incluir_iniciativa(self, personagem, valor_iniciativa):
        con = DataBase()
        sql = f"INSERT INTO tb_iniciativa (combatente, valor_iniciativa) VALUES ('{personagem}', {valor_iniciativa})"
        con.executa_query(sql)

    def listar_tabela_iniciativa(self):
        con = DataBase()
        sql = "SELECT combatente, valor_iniciativa FROM tb_iniciativa ORDER BY valor_iniciativa DESC"
        resultado = con.executa_consulta(sql)
        return resultado
