from PySide2 import QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox

from dao.usuario_dao import UsuarioDao
from view.ui_tela_lembrar_senha import Ui_LembrarSenha


class TelaLembrarSenha(QMainWindow, Ui_LembrarSenha):
    def __init__(self):
        super(TelaLembrarSenha, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Master Control Guide - Lembrar Senha")
        self.setFixedSize(397, 327)

        self.btn_lembrar_senha.clicked.connect(self.lembrar_senha_usuario)

    def lembrar_senha_usuario(self):
        if self.txt_lembrar_senha.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Lembrar Senha")
            msg.setText('Campo Lembrar Senha em branco.')
            msg.exec_()
        else:
            lembrete = self.txt_lembrar_senha.text()

            try:
                dao = UsuarioDao()
                resultado = dao.consultar_lembrete_senha(lembrete)

                self.label_usuario.setText(str(resultado[0][0]))
                self.label_senha.setText(str(resultado[0][1]))

            except ValueError:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_erro.png")
                msg.setWindowTitle("Lembrar Senha")
                msg.setText('Lembrete não confere. Por favor digite novamente.')
                msg.exec_()
