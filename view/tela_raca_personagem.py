from sqlite3 import IntegrityError
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox
from components.mensagens import Mensagens
from dao.raca_dao import RacaDao
from model.raca import Raca
from view.ui_tela_raca_personagem import Ui_TelaRaca


class TelaRacaPersonagem(QMainWindow, Ui_TelaRaca):
    def __init__(self):
        super(TelaRacaPersonagem, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Master Control Guide - Raça")
        self.setFixedSize(670, 451)

        self.btn_excluir.setEnabled(False)

        self.mensagem = Mensagens()
        self.listar_raca_personagem_tabela()
        self.btn_cadastrar.clicked.connect(self.cadastrar_raca)
        self.btn_limpar_tela.clicked.connect(self.limpar_tela)
        self.btn_carregar.clicked.connect(self.carregar_raca)
        self.btn_sair.clicked.connect(self.close)
        self.btn_pesquisar.clicked.connect(self.pesquisar_raca)
        self.btn_excluir.clicked.connect(self.excluir_raca)

    def listar_raca_personagem_tabela(self):
        try:
            dao = RacaDao()
            resultado = dao.listar_raca_tabela()

            self.tabela_raca.setRowCount(len(resultado))
            self.tabela_raca.setColumnCount(3)

            for i in range(len(resultado)):
                for j in range(0, 3):
                    self.tabela_raca.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError:
            self.mensagem.mensagem_de_erro()

    def cadastrar_raca(self):
        if self.txt_nome_raca.text() == "":
            campo = "Nome da Raça"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_referencia.text() == "":
            campo = "Referência"
            self.mensagem.mensagem_campo_em_branco(campo)
        else:
            raca = Raca()
            raca.nome_raca = self.txt_nome_raca.text()
            raca.referencia = self.txt_referencia.text()

            dao = RacaDao()
            resultado = dao.consulta_raca_nome(raca.nome_raca)

            try:
                if not resultado == raca.nome_raca:

                    dao_raca = RacaDao()
                    dao_raca.cadastrar_raca(raca.nome_raca, raca.referencia)

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_ok.png")
                    msg.setWindowTitle("Cadastro de Raca")
                    msg.setText(f'Raca {raca.nome_raca} cadastrado com sucesso.')
                    msg.exec_()

                    self.listar_raca_personagem_tabela()
                    self.limpar_tela()
                else:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_exclamacao.png")
                    msg.setWindowTitle("Cadastro de Raça")
                    msg.setText(f'Raça {raca.nome_raca} já está cadastrada.')
                    msg.exec_()
            except IntegrityError:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_exclamacao.png")
                msg.setWindowTitle("Cadastro de Raça")
                msg.setText(f'Raça {raca.nome_raca} já está cadastrada.')
                msg.exec_()

    def limpar_tela(self):
        self.txt_id.setText("")
        self.txt_nome_raca.setText("")
        self.txt_referencia.setText("")

        self.btn_excluir.setEnabled(False)

    def pesquisar_raca(self):
        if self.txt_nome_raca.text() == "":
            self.mensagem.mensagem_de_erro()
        else:
            raca = Raca()
            raca.raca = self.txt_nome_raca.text()

            try:
                dao = RacaDao()
                resultado = dao.pesquisar_raca_nome(raca.raca)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_exclamacao.png")
                    msg.setWindowTitle("Consulta Raça")
                    msg.setText('Raça informada não encontrada!')
                    msg.exec_()

                    self.limpar_tela()
                else:
                    self.tabela_raca.setRowCount(len(resultado))
                    self.tabela_raca.setColumnCount(3)

                    for i in range(len(resultado)):
                        for j in range(0, 3):
                            self.tabela_raca.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
                    self.limpar_tela()
            except ConnectionError:
                self.mensagem.mensagem_de_erro()

    def carregar_raca(self):

        linha = self.tabela_raca.currentItem().text()

        if not linha.isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Consultar Raça")
            msg.setText('Selecione somente a coluna de ID.')
            msg.exec_()
        else:
            try:
                dao = RacaDao()
                resultado = dao.carregar_raca_id(linha)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_exclamacao.png")
                    msg.setWindowTitle("Consulta Raça")
                    msg.setText('Selecione somente a coluna de ID!')
                    msg.exec_()
                else:
                    self.txt_id.setText(str(resultado[0][0]))
                    self.txt_nome_raca.setText(str(resultado[0][1]))
                    self.txt_referencia.setText(str(resultado[0][2]))

                    self.btn_excluir.setEnabled(True)
            except AttributeError:
                self.mensagem.mensagem_de_erro()

    def excluir_raca(self):
        raca = Raca()
        raca.id_raca_personagem = self.txt_id.text()
        raca.raca = self.txt_nome_raca.text()
        print(raca.id_raca_personagem)

        if raca.raca == "Anão":
            self.mensagem.mensagem_proibido_excluir_raca(raca.raca)
        elif raca.raca == "Elfo":
            self.mensagem.mensagem_proibido_excluir_raca(raca.raca)
        elif raca.raca == "Halfling":
            self.mensagem.mensagem_proibido_excluir_raca(raca.raca)
        elif raca.raca == "Humano":
            self.mensagem.mensagem_proibido_excluir_raca(raca.raca)
        elif raca.raca == "Draconato":
            self.mensagem.mensagem_proibido_excluir_raca(raca.raca)
        elif raca.raca == "Gnomo":
            self.mensagem.mensagem_proibido_excluir_raca(raca.raca)
        elif raca.raca == "Meio-Elfo":
            self.mensagem.mensagem_proibido_excluir_raca(raca.raca)
        elif raca.raca == "Meio-Orc":
            self.mensagem.mensagem_proibido_excluir_raca(raca.raca)
        elif raca.raca == "Tiefling":
            self.mensagem.mensagem_proibido_excluir_raca(raca.raca)
        elif self.txt_id == "":
            campo = "Identificador"
            self.mensagem.mensagem_campo_em_branco(campo)
        else:
            try:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_interrogacao.png")
                msg.setWindowTitle("Exclusão de Classe!")
                msg.setText("Tem certeza que deseja excluir a Classe?")
                msg.setStandardButtons(QMessageBox.Yes)
                msg.addButton(QMessageBox.No)
                msg.setDefaultButton(QMessageBox.No)
                if msg.exec_() == QMessageBox.Yes:
                    dao = RacaDao()
                    dao.excluir_raca(raca.id_raca_personagem)

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_ok.png")
                    msg.setWindowTitle("Excluir Raça")
                    msg.setText(f'Raça {raca.raca} excluida com sucesso!')
                    msg.exec_()

                    self.btn_excluir.setEnabled(False)
                    self.limpar_tela()
                    self.listar_raca_personagem_tabela()
            except AttributeError:
                self.mensagem.mensagem_de_erro()
