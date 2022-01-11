from sqlite3 import OperationalError
from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QMessageBox
from components.mensagens import Mensagens
from dao.nivel_personagem_dao import NivelPersonagemDao
from view.ui_tela_nivel_desafio import Ui_NivelDesafio


class TelaNivelDesafio(QMainWindow, Ui_NivelDesafio):
    def __init__(self):
        super(TelaNivelDesafio, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Master Control Guide - Nível de desafio")
        self.setFixedSize(1174, 588)

        self.mensagem = Mensagens()

        self.carregar_personagem_combo()
        self.carregar_tabela_nivel()
        self.calcular_nivel_desafio_personagem()

        self.btn_inserir.clicked.connect(self.inserir_personagens_nivel)
        self.btn_limpar_lista.clicked.connect(self.limpar_tabela_nivel_personagem)
        self.btn_calcular_encontro.clicked.connect(self.calculo_encontro_combate)

    def carregar_personagem_combo(self):
        try:
            dao = NivelPersonagemDao()
            resultado = dao.carregar_combo_personagem()

            for i in resultado:
                self.combo_selecionar_personagem.addItem(str(i[0]))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def inserir_personagens_nivel(self):
        if self.combo_selecionar_personagem.currentText() == "Selecionar":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Nível de Desafio")
            msg.setText('Selecione um Personagem')
            msg.exec_()
        else:
            personagem = self.combo_selecionar_personagem.currentText()

            dao = NivelPersonagemDao()
            nivel = dao.consultar_nivel_personagem(personagem)

            if nivel[0][0] == 1:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 25, 50, 75, 100)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 2:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 50, 100, 150, 200)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 3:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 75, 150, 225, 400)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 4:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 125, 250, 375, 500)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 5:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 250, 500, 750, 1100)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 6:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 300, 600, 900, 1400)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 7:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 350, 750, 1100, 1700)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 8:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 450, 900, 1400, 2100)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 9:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 550, 1100, 1600, 2400)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 10:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 600, 1200, 1900, 2800)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 11:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 800, 1500, 2400, 3600)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 12:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 1000, 2000, 3000, 4500)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 13:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 1100, 2200, 3400, 5100)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 14:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 1250, 2500, 3800, 5700)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 15:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 1400, 2800, 4300, 6500)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 16:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 1600, 3200, 4800, 7200)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 17:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 2000, 3900, 5900, 8800)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 18:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 2100, 4200, 6300, 9500)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 19:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 2400, 4900, 7300, 10900)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            elif nivel[0][0] == 20:
                dao.inserir_personagem_nivel(personagem, nivel[0][0], 2800, 5700, 8500, 12700)
                self.mensagem.inclusao_personagem_nivel(personagem)
                self.carregar_tabela_nivel()
            else:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_erro.png")
                msg.setWindowTitle("Proibido excluir!")
                msg.setText(f'Nível de Personagem não encontrado.')
                msg.exec_()
        self.calcular_nivel_desafio_personagem()

    def carregar_tabela_nivel(self):
        try:
            dao = NivelPersonagemDao()
            resultado = dao.carregar_tabela_nivel_personagem()

            self.tabela_nivel_usuario.setRowCount(len(resultado))
            self.tabela_nivel_usuario.setColumnCount(6)

            for i in range(len(resultado)):
                for j in range(0, 6):
                    self.tabela_nivel_usuario.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def limpar_tabela_nivel_personagem(self):
        try:
            dao = NivelPersonagemDao()
            dao.limpar_tabela_nivel_personagem()
            dao.limpar_calculo_nivel()

            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_ok.png")
            msg.setWindowTitle("Limpar tabela de nível de Personagem")
            msg.setText('Tabela de nível de personagem apagada com sucesso.')
            msg.exec_()

            self.carregar_tabela_nivel()

            self.txt_nivel_facil.setText("")
            self.txt_nivel_medio.setText("")
            self.txt_nivel_dificil.setText("")
            self.txt_nivel_mortal.setText("")
            self.combo_selecionar_personagem.setCurrentText("Selecionar")
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def calcular_nivel_desafio_personagem(self):
        try:
            dao = NivelPersonagemDao()
            nivel_facil = dao.total_nivel_facil()
            nivel_medio = dao.total_nivel_medio()
            nivel_dificil = dao.total_nivel_dificil()
            nivel_mortal = dao.total_nivel_mortal()

            dao.limpar_calculo_nivel()
            dao.inserir_resultado_calculo_nivel(nivel_facil[0][0], nivel_medio[0][0], nivel_dificil[0][0],
                                                nivel_mortal[0][0])

            self.txt_nivel_facil.setText(str(nivel_facil[0][0]))
            self.txt_nivel_medio.setText(str(nivel_medio[0][0]))
            self.txt_nivel_dificil.setText(str(nivel_dificil[0][0]))
            self.txt_nivel_mortal.setText(str(nivel_mortal[0][0]))
        except AttributeError:
            self.mensagem.mensagem_de_erro()
        except OperationalError:
            pass

    def calculo_encontro_combate(self):
        xp = 0
        resultado = 0
        if self.txt_total_xp_monstros.text() == "":
            campo = "Total XP dos monstros"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.combo_selecionar_numero_monstros.currentText() == "Selecionar":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Encontro")
            msg.setText('Selecione a quantidade de monstros.')
            msg.exec_()
        else:
            if self.combo_selecionar_numero_monstros.currentText() == "1":
                xp = float(self.txt_total_xp_monstros.text()) * 1
            elif self.combo_selecionar_numero_monstros.currentText() == "2":
                xp = float(self.txt_total_xp_monstros.text()) * 1.5
            elif self.combo_selecionar_numero_monstros.currentText() == "3-6":
                xp = float(self.txt_total_xp_monstros.text()) * 2
            elif self.combo_selecionar_numero_monstros.currentText() == "7-10":
                xp = float(self.txt_total_xp_monstros.text()) * 2.5
            elif self.combo_selecionar_numero_monstros.currentText() == "11-14":
                xp = float(self.txt_total_xp_monstros.text()) * 3
            elif self.combo_selecionar_numero_monstros.currentText() == "15 ou mais":
                xp = float(self.txt_total_xp_monstros.text()) * 4

            facil = float(self.txt_nivel_facil.text())
            medio = float(self.txt_nivel_medio.text())
            dificil = float(self.txt_nivel_dificil.text())
            mortal = float(self.txt_nivel_mortal.text())

            if xp <= facil:
                resultado = "Encontro Fácil"
            elif xp > facil and xp <= medio:
                resultado = "Encontro Médio"
            elif xp > medio and xp <= dificil:
                resultado = "Encontro Dificil"
            elif xp > mortal:
                resultado = "Encontro Mortal"

            self.label_Resultado_encontro.setText(f"{xp} - Nível: {resultado}")
