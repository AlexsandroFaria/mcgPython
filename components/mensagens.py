from PySide2 import QtGui
from PySide2.QtWidgets import QMessageBox


class Mensagens:

    def mensagem_campo_em_branco(self, campo):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
        msg.setIconPixmap("_img/botao_exclamacao.png")
        msg.setWindowTitle("Campos em branco!")
        msg.setText(f'Campo {campo} não pode estar em branco.')
        msg.exec_()

    def mensagem_de_erro(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
        msg.setIconPixmap("_img/botao_erro.png")
        msg.setWindowTitle("Erro de conexão!")
        msg.setText('Erro de conexão no banco de dados.')
        msg.exec_()

    def mensagem_proibido_excluir_classe(self, nome_classe):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
        msg.setIconPixmap("_img/botao_erro.png")
        msg.setWindowTitle("Proibido excluir!")
        msg.setText(f'A classe de personagem {nome_classe} não pode ser excluida.')
        msg.exec_()

    def mensagem_proibido_excluir_raca(self, nome_raca):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
        msg.setIconPixmap("_img/botao_erro.png")
        msg.setWindowTitle("Proibido excluir!")
        msg.setText(f'A Raça {nome_raca} não pode ser excluida.')
        msg.exec_()

    def inclusao_personagem_nivel(self, nome):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
        msg.setIconPixmap("_img/botao_ok.png")
        msg.setWindowTitle("Proibido excluir!")
        msg.setText(f'Personagem {nome} Inserido com sucesso.')
        msg.exec_()
