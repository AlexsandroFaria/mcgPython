import random

from PySide2 import QtGui

from components.mensagens import Mensagens
from view.ui_tela_dados import Ui_TelaDados
from PySide2.QtWidgets import QMainWindow, QMessageBox


class TelaDados(QMainWindow, Ui_TelaDados):
    def __init__(self):
        super(TelaDados, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Master Control Guide - Dados")
        self.setFixedSize(400, 325)

        self.mensagem = Mensagens()
        self.btn_rolar_dados.clicked.connect(self.rolar_dados)
        self.btn_limpar_tela.clicked.connect(self.limpar_tela)
        self.btn_sair.clicked.connect(self.close)

    def rolar_dados(self):
        self.txt_resultado.setText("")
        if self.combo_faces.currentText() == "Selecionar":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Dados")
            msg.setText('Selecione uma opção em Números de Faces.')
            msg.exec_()
        elif self.txt_numero_dados.text() == "":
            campo = "Número de dados"
            self.mensagem.mensagem_campo_em_branco(campo)
        else:
            numero_dados = self.txt_numero_dados.text()
            numero_faces = self.combo_faces.currentText()
            self.count = 0

            if numero_faces == "1 D 4":
                for resultado in range(int(numero_dados)):
                    resultado = random.randrange(1, 4 + 1)
                    self.count += 1
                    self.txt_resultado.append(f"Resultado {self.count} - {str(resultado)}")
            elif numero_faces == "1 D 6":
                for resultado in range(int(numero_dados)):
                    resultado = random.randrange(1, 6 + 1)
                    self.count += 1
                    self.txt_resultado.append(f"Resultado {self.count} - {str(resultado)}")
            elif numero_faces == "1 D 8":
                for resultado in range(int(numero_dados)):
                    resultado = random.randrange(1, 8 + 1)
                    self.count += 1
                    self.txt_resultado.append(f"Resultado {self.count} - {str(resultado)}")
            elif numero_faces == "1 D 10":
                for resultado in range(int(numero_dados)):
                    resultado = random.randrange(1, 10 + 1)
                    self.count += 1
                    self.txt_resultado.append(f"Resultado {self.count} - {str(resultado)}")
            elif numero_faces == "1 D 12":
                for resultado in range(int(numero_dados)):
                    resultado = random.randrange(1, 12 + 1)
                    self.count += 1
                    self.txt_resultado.append(f"Resultado {self.count} - {str(resultado)}")
            elif numero_faces == "1 D 20":
                for resultado in range(int(numero_dados)):
                    resultado = random.randrange(1, 20 + 1)
                    self.count += 1
                    self.txt_resultado.append(f"Resultado {self.count} - {str(resultado)}")

    def limpar_tela(self):
        self.combo_faces.setCurrentText("Selecionar")
        self.txt_resultado.setText("")
        self.txt_numero_dados.setText("")
