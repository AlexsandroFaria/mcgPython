from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox

from conexao.create_database import CreateDatabase
from dao.usuario_dao import UsuarioDao
from model.usuario import Usuario
from view.tela_lembrar_senha import TelaLembrarSenha
from view.tela_principal import TelaPrincipal
from view.ui_tela_login import Ui_TelaLogin


class TelaLogin(QMainWindow, Ui_TelaLogin):
    def __init__(self):
        super(TelaLogin, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Master Control Guide')

        self.txt_senha.returnPressed.connect(self.efetuar_login)

        self.btn_fechar.clicked.connect(self.close)
        self.menu_sair.triggered.connect(self.close)
        self.menu_criacao_banco.triggered.connect(self.criar_estrutura_banco)
        self.btn_logar.clicked.connect(self.efetuar_login)
        self.btn_lembrar_senha.clicked.connect(self.abrir_tela_lembrar_senha)

    def criar_estrutura_banco(self):
        db = CreateDatabase()
        db.create_table_users()
        db.create_table_classe_personagem()
        db.create_table_iniciativa()
        db.create_table_nivel_personagem()
        db.create_table_personagem()
        db.create_table_raca_personagem()
        db.create_table_repositorio_monstros()
        db.create_table_monstro_batalha()
        db.inserir_monstros_tabela_repositorio_monstros()
        db.inserir_raca_tabela_raca()
        db.inserir_classes_tabela_classe()
        db.create_table_calculo_nivel()
        db.inserir_usuario()

        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
        msg.setIconPixmap("_img/botao_ok.png")
        msg.setWindowTitle("Consulta Contrato")
        msg.setText('Banco de dados criado com sucesso!')
        msg.exec_()

    def efetuar_login(self):
        if self.txt_usuario.text() == "" and self.txt_senha.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Campos em branco!")
            msg.setText('Campos Login ou senha em Branco')
            msg.exec_()
        else:
            user = Usuario()

            user.usuario = self.txt_usuario.text()
            user.senha = self.txt_senha.text()

            dao = UsuarioDao()
            resultado = dao.consultar_usuario_senha(user.usuario, user.senha)

            if resultado:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_ok.png")
                msg.setWindowTitle("Login!")
                msg.setText(f'Seja bem vindo {resultado[0][1]}.')
                msg.exec_()

                if resultado[0][5] == "Jogador":
                    self.tela_principal = TelaPrincipal()

                    self.tela_principal.menu_cadastro_usuario.setEnabled(False)
                    self.tela_principal.menu_consulta_usuarios.setEnabled(False)
                    self.tela_principal.menu_cadastro_personagem.setEnabled(False)
                    self.tela_principal.menu_cadastro_classes.setEnabled(False)
                    self.tela_principal.menu_cadastro_raca.setEnabled(False)
                    self.tela_principal.menu_cadastrar_monstros.setEnabled(False)

                    self.tela_principal.label_nome.setText(str(resultado[0][1]))
                    self.tela_principal.show()
                    self.close()
                else:
                    self.tela_principal = TelaPrincipal()
                    self.tela_principal.show()
                    self.tela_principal.label_nome.setText(str(resultado[0][1]))
                    self.close()
            else:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_erro.png")
                msg.setWindowTitle("Login!")
                msg.setText('Login ou senha incorretos.')
                msg.exec_()

                self.txt_usuario.setText("")
                self.txt_senha.setText("")

    def abrir_tela_lembrar_senha(self):
        self.tela_lembrar_senha = TelaLembrarSenha()
        self.tela_lembrar_senha.show()
