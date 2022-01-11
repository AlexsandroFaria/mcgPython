from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QMessageBox

from components.mensagens import Mensagens
from dao.usuario_dao import UsuarioDao
from model.usuario import Usuario
from view.ui_tela_usuario import Ui_TelaUsuarios


class TelaUsuario(QMainWindow, Ui_TelaUsuarios):
    def __init__(self):
        super(TelaUsuario, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Master Control Guide - Usuários")
        self.setFixedSize(912, 575)

        self.listar_usuarios_tabela()

        self.mensagem = Mensagens()
        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)

        self.btn_fechar.clicked.connect(self.close)
        self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)
        self.btn_carregar.clicked.connect(self.carregar_campos_ususario)
        self.btn_limpar_campos.clicked.connect(self.limpar_campos)
        self.btn_alterar.clicked.connect(self.alterar_usuario)
        self.btn_excluir.clicked.connect(self.excluir_usuario)

    def cadastrar_usuario(self):
        if self.txt_nome_usuario.text() == "":
            campo = "Nome do Usuário"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_email.text() == "":
            campo = "E-mail"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_usuario.text() == "":
            campo = "Usuário"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_senha.text() == "":
            campo = "Senha"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.combo_acesso.currentText() == "Selecione uma opção":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Login!")
            msg.setText('Em acesso informe uma opção válida.')
            msg.exec_()
        elif self.txtlembrete_senha.text() == "":
            campo = "Lembrete de senha"
            self.mensagem.mensagem_campo_em_branco(campo)
        else:
            usuario = Usuario()
            usuario.nome = self.txt_nome_usuario.text()
            usuario.email = self.txt_usuario.text()
            usuario.usuario = self.txt_usuario.text()
            usuario.senha = self.txt_senha.text()
            usuario.acesso = self.combo_acesso.currentText()
            usuario.lembrar_senha = self.txtlembrete_senha.text()

            if usuario.senha == self.txt_confirmar_senha.text():
                try:
                    dao = UsuarioDao()
                    dao.cadastrar_usuario(usuario.nome, usuario.email, usuario.usuario, usuario.senha, usuario.acesso,
                                          usuario.lembrar_senha)

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_ok.png")
                    msg.setWindowTitle("Login!")
                    msg.setText(f'Usuario {usuario.nome} cadastrado com sucesso.')
                    msg.exec_()

                    self.listar_usuarios_tabela()
                    self.limpar_campos()
                except AttributeError:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_erro.png")
                    msg.setWindowTitle("Campos em branco!")
                    msg.setText('Erro ao cadastrar usuário!')
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_exclamacao.png")
                msg.setWindowTitle("Senha")
                msg.setText('As senhas não são iguais. Digite novamente')
                msg.exec_()

    def listar_usuarios_tabela(self):
        dao = UsuarioDao()
        resultado = dao.listar_usuario_tabela()

        self.tabela_usuarios.setRowCount(len(resultado))
        self.tabela_usuarios.setColumnCount(7)

        for i in range(0, len(resultado)):
            for j in range(0, 7):
                self.tabela_usuarios.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

    def carregar_campos_ususario(self):
        try:
            dao = UsuarioDao()
            dao.listar_usuario_tabela()

            linha = self.tabela_usuarios.currentItem().text()

            if not linha.isdigit():
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIconPixmap("_img/botao_exclamacao.png")
                msg.setWindowTitle("Consultar Chamados")
                msg.setText('Selecione somente a coluna Número identificador do Usuário.')
                msg.exec_()
            else:
                resultado = dao.consulta_id_usuario(linha)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                    msg.setIconPixmap("_img/botao_exclamacao.png")
                    msg.setWindowTitle("Consulta Contrato")
                    msg.setText('Selecione somente a coluna Número identificador do Usuário.')
                    msg.exec_()
                else:
                    self.tab_usuarios.setCurrentWidget(self.tab_usuarios_cadastro)

                    self.txt_id.setText(str(resultado[0][0]))
                    self.txt_nome_usuario.setText(str(resultado[0][1]))
                    self.txt_email.setText(str(resultado[0][2]))
                    self.txt_usuario.setText(str(resultado[0][3]))
                    self.txt_senha.setText(str(resultado[0][4]))
                    self.combo_acesso.setCurrentText(str(resultado[0][5]))
                    self.txtlembrete_senha.setText(str(resultado[0][6]))

                    self.btn_alterar.setEnabled(True)
                    self.btn_excluir.setEnabled(True)
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def limpar_campos(self):
        self.txt_id.setText("")
        self.txt_nome_usuario.setText("")
        self.txt_email.setText("")
        self.txt_usuario.setText("")
        self.txt_senha.setText("")
        self.txt_confirmar_senha.setText("")
        self.combo_acesso.setCurrentText("Selecione uma opção")
        self.txtlembrete_senha.setText("")

        self.btn_excluir.setEnabled(False)
        self.btn_alterar.setEnabled(False)

    def alterar_usuario(self):
        if self.txt_nome_usuario.text() == "":
            campo = "Nome do Usuário"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_email.text() == "":
            campo = "E-mail"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_usuario.text() == "":
            campo = "Usuário"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_senha.text() == "":
            campo = "Senha"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.combo_acesso.currentText() == "Selecione uma opção":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Login!")
            msg.setText('Em acesso informe uma opção válida.')
            msg.exec_()
        elif self.txtlembrete_senha.text() == "":
            campo = "Lembrete de Senha"
            self.mensagem.mensagem_campo_em_branco(campo)
        else:
            usuario = Usuario()
            usuario.id = self.txt_id.text()
            usuario.nome = self.txt_nome_usuario.text()
            usuario.email = self.txt_email.text()
            usuario.email = self.txt_usuario.text()
            usuario.usuario = self.txt_usuario.text()
            usuario.senha = self.txt_senha.text()
            usuario.acesso = self.combo_acesso.currentText()
            usuario.lembrar_senha = self.txtlembrete_senha.text()

            if usuario.senha == self.txt_confirmar_senha.text():
                try:
                    dao = UsuarioDao()
                    dao.alterar_usuario(usuario.id, usuario.nome, usuario.email, usuario.usuario,
                                        usuario.senha, usuario.acesso, usuario.lembrar_senha)

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_ok.png")
                    msg.setWindowTitle("Login!")
                    msg.setText(f'Usuario {usuario.nome} alterado com sucesso.')
                    msg.exec_()

                    self.listar_usuarios_tabela()
                    self.limpar_campos()
                except AttributeError:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_erro.png")
                    msg.setWindowTitle("Campos em branco!")
                    msg.setText('Erro ao altertar usuário!')
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_exclamacao.png")
                msg.setWindowTitle("Senha")
                msg.setText('As senhas não são iuais. Digite novamente')
                msg.exec_()

    def excluir_usuario(self):

        usuario = Usuario()
        usuario.id = self.txt_id.text()

        dao = UsuarioDao()
        dao.excluir_usuario(usuario.id)
        msg = QMessageBox()

        msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
        msg.setIconPixmap("_img/botao_ok.png")
        msg.setWindowTitle("Senha")
        msg.setText(f'Usuário excluido com sucesso!')
        msg.exec_()

        self.limpar_campos()
        self.listar_usuarios_tabela()
