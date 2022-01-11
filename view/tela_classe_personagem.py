from sqlite3 import IntegrityError
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox
from components.mensagens import Mensagens
from dao.classe_dao import ClasseDao
from model.classe import Classe
from view.ui_tela_classe_personagem import Ui_TelaClasse


class TelaClassePersonagem(QMainWindow, Ui_TelaClasse):
    def __init__(self):
        super(TelaClassePersonagem, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Master Control Guide - Classe de Personagem")
        self.setFixedSize(670, 450)

        self.btn_excluir.setEnabled(False)

        self.listar_classe_personagem_tabela()
        self.mensagem = Mensagens()
        self.btn_sair.clicked.connect(self.close)
        self.btn_cadastrar.clicked.connect(self.cadastrar_classe)
        self.btn_pesquisar.clicked.connect(self.pesquisar_classe)
        self.btn_carregar.clicked.connect(self.carregar_classe)
        self.btn_excluir.clicked.connect(self.excluir_classe)
        self.btn_limpar_tela.clicked.connect(self.limpar_tela)

    def listar_classe_personagem_tabela(self):
        try:
            dao = ClasseDao()
            resultado = dao.listar_tabela_classe()

            self.tabela_classe.setRowCount(len(resultado))
            self.tabela_classe.setColumnCount(3)

            for i in range(len(resultado)):
                for j in range(0, 3):
                    self.tabela_classe.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError:
            self.mensagem.mensagem_de_erro()

    def cadastrar_classe(self):
        if self.txt_nome_classe.text() == "":
            campo = "Nome da Classe"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_referencia.text() == "":
            campo = "Referêcnia"
            self.mensagem.mensagem_campo_em_branco(campo)
        else:
            classe = Classe()
            classe.nome_classe = self.txt_nome_classe.text()
            classe.referencia = self.txt_referencia.text()

            dao = ClasseDao()
            resultado = dao.consulta_classe_nome(classe.nome_classe)

            try:
                if not resultado == classe.nome_classe:

                    dao = ClasseDao()
                    dao.cadastrar_classe_personagem(classe.nome_classe, classe.referencia)

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_ok.png")
                    msg.setWindowTitle("Cadastro de Classe")
                    msg.setText(f'Classe {classe.nome_classe} cadastrado com sucesso.')
                    msg.exec_()

                    self.listar_classe_personagem_tabela()
                    self.limpar_tela()
            except IntegrityError:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIcon(QMessageBox.Information)
                msg.setIconPixmap("_img/botao_exclamacao.png")
                msg.setText(f'Classe {classe.nome_classe} já está cadastrada.')
                msg.exec_()

                self.limpar_tela()

    def limpar_tela(self):
        self.txt_id.setText("")
        self.txt_nome_classe.setText("")
        self.txt_referencia.setText("")

        self.btn_excluir.setEnabled(False)

    def pesquisar_classe(self):
        if self.txt_nome_classe.text() == "":
            campo = "Nome da Classe"
            self.mensagem.mensagem_campo_em_branco(campo)
        else:
            classe = Classe()
            classe.nome_classe = self.txt_nome_classe.text()
            try:
                dao = ClasseDao()
                resultado = dao.pesquisar_classe_nome(classe.nome_classe)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_erro.png")
                    msg.setWindowTitle("Consulta Contrato")
                    msg.setText('Classe informada não encontrada!')
                    msg.exec_()

                    self.limpar_tela()
                else:
                    self.tabela_classe.setRowCount(len(resultado))
                    self.tabela_classe.setColumnCount(3)

                    for i in range(len(resultado)):
                        for j in range(0, 3):
                            self.tabela_classe.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

                    self.limpar_tela()
            except ConnectionError:
                self.mensagem.mensagem_de_erro()

    def carregar_classe(self):
        try:
            linha = self.tabela_classe.currentItem().text()

            if not linha.isdigit():
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_exclamacao.png")
                msg.setWindowTitle("Consultar Classe")
                msg.setText('Selecione somente a coluna de ID.')
                msg.exec_()
            else:
                dao = ClasseDao()
                resultado = dao.carregar_classe_id(linha)

                if len(resultado) == 0:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_exclamacao.png")
                    msg.setWindowTitle("Consulta Classe")
                    msg.setText('Selecione somente a coluna de ID!')
                    msg.exec_()
                else:
                    self.txt_id.setText(str(resultado[0][0]))
                    self.txt_nome_classe.setText(str(resultado[0][1]))
                    self.txt_referencia.setText(str(resultado[0][2]))

                    self.btn_excluir.setEnabled(True)
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def excluir_classe(self):
        classe = Classe()
        classe.nome_classe = self.txt_nome_classe.text()
        classe.id_classe = self.txt_id.text()

        if self.txt_nome_classe.text() == "Barbaro":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Bardo":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Bruxo":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Clérigo":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Druida":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Feiticeiro":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Guerreiro":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Ladino":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Mago":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Monge":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Paladino":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_nome_classe.text() == "Patrulheiro":
            self.mensagem.mensagem_proibido_excluir_classe(classe.nome_classe)
            self.limpar_tela()
        elif self.txt_id.text() == "":
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

                    dao = ClasseDao()
                    dao.excluir_classe(classe.id_classe)

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_ok.png")
                    msg.setWindowTitle("Consulta Contrato")
                    msg.setText(f'Classe {classe.nome_classe} excluida com sucesso!')
                    msg.exec_()

                    self.limpar_tela()
                    self.listar_classe_personagem_tabela()
            except AttributeError:
                self.mensagem.mensagem_de_erro()
