from conexao.database import DataBase


class UsuarioDao:

    def consultar_usuario_senha(self, usuario, senha):
        con = DataBase()
        sql = f"SELECT * FROM tb_usuario WHERE usuario='{usuario}' and senha='{senha}'"
        resultado = con.executa_consulta(sql)
        return resultado

    def listar_usuario_tabela(self):
        con = DataBase()
        sql = "SELECT * FROM tb_usuario"
        resultado = con.executa_consulta(sql)
        return resultado

    def consultar_lembrete_senha(self, lembrar_senha):
        con = DataBase()
        sql = f"SELECT usuario, senha FROM tb_usuario WHERE lembrar_senha='{lembrar_senha}'"
        print(sql)
        resultado = con.executa_consulta(sql)
        return resultado

    def cadastrar_usuario(self, nome, email, usuario, senha, acesso, lembrar_senha):
        con = DataBase()
        sql = f"INSERT INTO tb_usuario (nome, email, usuario, senha, acesso, lembrar_senha) VALUES ('{nome}'," \
              f"'{email}', '{usuario}', '{senha}', '{acesso}', '{lembrar_senha}')"
        con.executa_query(sql)

    def consulta_id_usuario(self, id):
        con = DataBase()
        sql = f"SELECT * FROM tb_usuario WHERE id={id}"
        resultado = con.executa_consulta(sql)
        return resultado

    def alterar_usuario(self, id, nome, email, usuario, senha, acesso, lembrar_senha):
        con = DataBase()
        sql = f"UPDATE tb_usuario SET nome='{nome}', email='{email}', usuario='{usuario}', senha='{senha}'," \
              f"acesso='{acesso}', lembrar_senha='{lembrar_senha}' WHERE id={id}"
        print(sql)
        con.executa_query(sql)

    def excluir_usuario(self, id):
        con = DataBase()
        sql = f"DELETE FROM tb_usuario WHERE id={id}"
        con.executa_query(sql)
