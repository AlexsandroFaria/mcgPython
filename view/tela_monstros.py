from PySide2 import QtGui, QtWidgets
from PySide2.QtWidgets import QMainWindow, QMessageBox

from components.mensagens import Mensagens
from conexao.create_database import CreateDatabase
from dao.monstro_dao import MonstrosDao
from model.monstro import Monstro
from view.ui_tela_monstros import Ui_TelaMonstros


class TelaMonstros(QMainWindow, Ui_TelaMonstros):
    def __init__(self):
        super(TelaMonstros, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Master Control Guide - Monstros")
        self.setFixedSize(1061, 600)

        self.mensagem = Mensagens()
        self.btn_excluir.setEnabled(False)
        self.btn_alterar.setEnabled(False)

        self.listar_monstros_tabela()

        self.txt_pesquisar_monstro.returnPressed.connect(self.pesquisar_monstros_tabela)

        self.btn_sair.clicked.connect(self.close)
        self.menu_reconstrui_lista_monstros.triggered.connect(self.reconstruir_tabela_monstros)
        self.btn_carregar.clicked.connect(self.carregar_campos)
        self.btn_pesquisar_monstros.clicked.connect(self.pesquisar_monstros_tabela)
        self.btn_cadastrar.clicked.connect(self.cadastrar_monstro)
        self.btn_alterar.clicked.connect(self.alterar_monstro)
        self.btn_excluir.clicked.connect(self.excluir_monstro)

    def reconstruir_tabela_monstros(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
        msg.setIconPixmap("_img/botao_interrogacao.png")
        msg.setWindowTitle("Reestruturação Lista de Monstros")
        msg.setText("Esta ação irá recriar a lista de monstros para a original. Dejeja continuar?")
        msg.setStandardButtons(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            database = CreateDatabase()
            database.excluir_registros_tabela_monstros()
            database.inserir_monstros_tabela_repositorio_monstros()

            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_ok.png")
            msg.setWindowTitle("Reestruturação de Monstros")
            msg.setText('Lista retornada para a original com sucesso.')
            msg.exec_()

            self.listar_monstros_tabela()

    def listar_monstros_tabela(self):
        try:
            dao = MonstrosDao()
            resultado = dao.listar_monstros_tabela()

            self.tabela_Monstros.setRowCount(len(resultado))
            self.tabela_Monstros.setColumnCount(9)

            for i in range(len(resultado)):
                for j in range(0, 9):
                    self.tabela_Monstros.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def carregar_campos(self):
        linha = self.tabela_Monstros.currentItem().text()
        coluna = self.tabela_Monstros.currentColumn()

        if coluna == 1:
            try:
                dao = MonstrosDao()
                resultado = dao.carregar_monstros(linha)

                self.tab_monstros.setCurrentWidget(self.tab_cadastro_monstros)

                self.txt_id.setText(str(resultado[0][0]))
                self.txt_nome_monstros.setText(str(resultado[0][1]))
                self.combo_tipo_monstro.setCurrentText(str(resultado[0][2]))
                self.txt_classe_armadura.setText(str(resultado[0][3]))
                self.txt_pontos_vida.setText(str(resultado[0][4]))
                self.txt_pontos_vida_atual.setText(str(resultado[0][5]))
                self.txt_deslocamento.setText(str(resultado[0][6]))
                self.txt_nivel_desafio.setText(str(resultado[0][7]))
                self.txt_referencia.setText(str(resultado[0][8]))

                self.btn_excluir.setEnabled(True)
                self.btn_alterar.setEnabled(True)
            except AttributeError:
                self.mensagem.mensagem_de_erro()
        else:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Seleção de Monstro")
            msg.setText('Selecione o nome do Monstro na coluna Nome.')
            msg.exec_()

    def pesquisar_monstros_tabela(self):
        nome_monstro = self.txt_pesquisar_monstro.text()
        try:
            dao = MonstrosDao()
            resultado = dao.pesquisar_monstro_tabela(nome_monstro)

            self.tabela_Monstros.setRowCount(len(resultado))
            self.tabela_Monstros.setColumnCount(9)

            for i in range(len(resultado)):
                for j in range(0, 9):
                    self.tabela_Monstros.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def cadastrar_monstro(self):
        if self.txt_nome_monstros.text() == "":
            campo = "Nome monstro"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.combo_tipo_monstro.currentText() == "Selecionar":
            campo = "Tipo de Monstro"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_classe_armadura.text() == "":
            campo = "Classe de Armadura"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_pontos_vida.text() == "":
            campo = "Pontos de vida"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_pontos_vida_atual.text() == "":
            campo = "Pontos de vida atual"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_deslocamento.text() == "":
            campo = "Deslocamento"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_nivel_desafio.text() == "":
            campo = "Nível de desafio"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_referencia.text() == "":
            campo = "Referência"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif not self.txt_classe_armadura.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Altaração de Monstro")
            msg.setText("Campo Classe de Armadura não pode ter letras.")
            msg.exec_()
        elif not self.txt_pontos_vida_atual.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Altaração de Monstro")
            msg.setText("Campo Pontos de Vida não pode ter letras.")
            msg.exec_()
        else:
            monstro = Monstro()
            monstro.nome_monstro = self.txt_nome_monstros.text()
            monstro.tipo_monstro = self.combo_tipo_monstro.currentText()
            monstro.classe_armadura = self.txt_classe_armadura.text()
            monstro.pontos_vida = self.txt_pontos_vida.text()
            monstro.pontos_vida_atual = self.txt_pontos_vida_atual.text()
            monstro.deslocamento = self.txt_deslocamento.text()
            monstro.nivel_desafio = self.txt_nivel_desafio.text()
            monstro.referencia = self.txt_referencia.text()

            dao = MonstrosDao()
            dao.cadastrar_monstros(monstro.nome_monstro, monstro.tipo_monstro, monstro.classe_armadura,
                                   monstro.pontos_vida, monstro.pontos_vida_atual, monstro.deslocamento,
                                   monstro.nivel_desafio, monstro.referencia)

            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_ok.png")
            msg.setWindowTitle("Cadastro de Monstro")
            msg.setText("Monstro Cadastrado com sucesso.")
            msg.exec_()

            self.listar_monstros_tabela()
            self.limpar_tela()

    def alterar_monstro(self):
        if self.txt_nome_monstros.text() == "":
            campo = "Nome monstro"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.combo_tipo_monstro.currentText() == "Selecionar":
            campo = "Tipo de Monstro"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_classe_armadura.text() == "":
            campo = "Classe de Armadura"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_pontos_vida.text() == "":
            campo = "Pontos de vida"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_pontos_vida_atual.text() == "":
            campo = "Pontos de vida atual"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_deslocamento.text() == "":
            campo = "Deslocamento"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_nivel_desafio.text() == "":
            campo = "Nível de desafio"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_referencia.text() == "":
            campo = "Referência"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif not self.txt_classe_armadura.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Altaração de Monstro")
            msg.setText("Campo Classe de Armadura não pode ter letras.")
            msg.exec_()
        elif not self.txt_pontos_vida_atual.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Altaração de Monstro")
            msg.setText("Campo Pontos de Vida não pode ter letras.")
            msg.exec_()
        else:
            monstro = Monstro()
            monstro.id_repositorio_monstro = self.txt_id.text()
            monstro.nome_monstro = self.txt_nome_monstros.text()
            monstro.tipo_monstro = self.combo_tipo_monstro.currentText()
            monstro.classe_armadura = self.txt_classe_armadura.text()
            monstro.pontos_vida = self.txt_pontos_vida.text()
            monstro.pontos_vida_atual = self.txt_pontos_vida_atual.text()
            monstro.deslocamento = self.txt_deslocamento.text()
            monstro.nivel_desafio = self.txt_nivel_desafio.text()
            monstro.referencia = self.txt_referencia.text()

            try:
                dao = MonstrosDao()
                dao.alterar_monstro(monstro.id_repositorio_monstro, monstro.nome_monstro, monstro.tipo_monstro,
                                    monstro.classe_armadura, monstro.pontos_vida, monstro.pontos_vida_atual,
                                    monstro.deslocamento, monstro.nivel_desafio, monstro.referencia)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_ok.png")
                msg.setWindowTitle("Alteração de Monstro")
                msg.setText("Monstro alterado com sucesso.")
                msg.exec_()

                self.limpar_tela()
                self.listar_monstros_tabela()
            except AttributeError:
                self.mensagem.mensagem_de_erro()

    def excluir_monstro(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setIconPixmap("_img/botao_interrogacao.png")
        msg.setWindowTitle("Exclusão de Monstros")
        msg.setText("Tem certeza que deseja excluir o Monstro Selecionado?")
        msg.setStandardButtons(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            monstro = Monstro()
            monstro.id_repositorio_monstro = self.txt_id.text()

            try:
                dao = MonstrosDao()
                dao.excluir_monstro(monstro.id_repositorio_monstro)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_ok.png")
                msg.setWindowTitle("Excluir Monstros")
                msg.setText("Monstro excluido com sucesso.")
                msg.exec_()

                self.limpar_tela()
                self.listar_monstros_tabela()
            except AttributeError:
                self.mensagem.mensagem_de_erro()

    def limpar_tela(self):
        self.txt_id.setText("")
        self.txt_nome_monstros.setText("")
        self.combo_tipo_monstro.setCurrentText("Selecionar")
        self.txt_classe_armadura.setText("")
        self.txt_pontos_vida.setText("")
        self.txt_pontos_vida_atual.setText("")
        self.txt_deslocamento.setText("")
        self.txt_nivel_desafio.setText("")
        self.txt_referencia.setText("")

        self.btn_excluir.setEnabled(False)
        self.btn_alterar.setEnabled(False)
