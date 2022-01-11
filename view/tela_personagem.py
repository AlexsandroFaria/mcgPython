from sqlite3 import IntegrityError

from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox

from components.mensagens import Mensagens
from dao.classe_dao import ClasseDao
from dao.personagem_dao import PersonagemDao
from dao.raca_dao import RacaDao
from model.personagem import Personagem
from view.ui_tela_personagem import Ui_TelaPersonagem


class TelaPersonagem(QMainWindow, Ui_TelaPersonagem):
    def __init__(self):
        super(TelaPersonagem, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Master Control Guide - Personagens")
        self.setFixedSize(1096, 603)

        self.mensagem = Mensagens()
        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)

        self.listar_personagem_tabela()
        self.popular_combo_classe_personagem()
        self.popular_combo_raca_personagem()
        self.popular_combo_personagem()

        self.btn_limpar_tela.clicked.connect(self.limpar_tela)
        self.btn_sair.clicked.connect(self.close)
        self.btn_cadastrar.clicked.connect(self.cadastrar_personagem)
        self.combo_selecionar_personagem.activated.connect(self.carregar_personagem_combo)
        self.btn_carregar.clicked.connect(self.carregar_campos)
        self.btn_alterar.clicked.connect(self.alterar_usuario)
        self.btn_excluir.clicked.connect(self.excluir_personagem)

    def listar_personagem_tabela(self):
        try:
            dao = PersonagemDao()
            resultado = dao.listar_personagem_tabela()

            self.tabela_personagem.setRowCount(len(resultado))
            self.tabela_personagem.setColumnCount(10)

            for i in range(len(resultado)):
                for j in range(0, 10):
                    self.tabela_personagem.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except ConnectionError:
            self.mensagem.mensagem_de_erro()

    def popular_combo_classe_personagem(self):
        try:
            dao = ClasseDao()
            resultado = dao.popular_combo_classe_nome()

            for i in resultado:
                self.combo_classe.addItem(str(i[0]))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def popular_combo_personagem(self):
        try:
            dao = PersonagemDao()
            resultado = dao.popular_combo_nome_personagem()

            for i in resultado:
                self.combo_selecionar_personagem.addItem(str(i[0]))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def popular_combo_raca_personagem(self):
        try:
            dao = RacaDao()
            resultado = dao.popular_combo_raça_nome()

            for i in resultado:
                self.combo_raca.addItem(str(i[0]))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def carregar_personagem_combo(self):
        nome_personagem = self.combo_selecionar_personagem.currentText()

        if self.combo_selecionar_personagem.currentText() == nome_personagem:
            try:
                dao = PersonagemDao()
                resultado = dao.carregar_campos_personagem(nome_personagem)

                self.txt_id.setText(str(resultado[0][0]))
                self.txt_nome_personagem.setText(str(resultado[0][1]))
                self.combo_classe.setCurrentText(str(resultado[0][2]))
                self.combo_raca.setCurrentText(str(resultado[0][3]))
                self.combo_dados_vida.setCurrentText(str(resultado[0][4]))
                self.txt_total_pontos_vida.setText(str(resultado[0][5]))
                self.txt_pontos_vida_atual.setText(str(resultado[0][6]))
                self.txt_pontos_experiencia.setText(str(resultado[0][7]))
                self.combo_nivel_personagem.setCurrentText(str(resultado[0][8]))
                self.txt_pontos_heroicos.setText(str(resultado[0][9]))

                self.btn_cadastrar.setEnabled(False)
                self.btn_excluir.setEnabled(True)
                self.btn_alterar.setEnabled(True)
            except IndexError:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_exclamacao.png")
                msg.setWindowTitle("Personagem")
                msg.setText('Selecione um Personagem')
                msg.exec_()

    def limpar_tela(self):
        self.txt_id.setText("")
        self.combo_selecionar_personagem.setCurrentText("Selecione uma opção")
        self.txt_nome_personagem.setText("")
        self.combo_classe.setCurrentText("Selecione uma opção")
        self.combo_raca.setCurrentText("Selecione uma opção")
        self.combo_dados_vida.setCurrentText("Selecione uma opção")
        self.txt_total_pontos_vida.setText("")
        self.txt_pontos_vida_atual.setText("")
        self.txt_pontos_experiencia.setText("")
        self.combo_nivel_personagem.setCurrentText("Selecionar")
        self.txt_pontos_heroicos.setText("")

        self.btn_cadastrar.setEnabled(True)
        self.btn_alterar.setEnabled(False)
        self.btn_excluir.setEnabled(False)

    def cadastrar_personagem(self):
        if self.txt_nome_personagem.text() == "":
            campo = "Nome do Personagem"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.combo_classe.currentText() == "Selecione uma opção":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro de Personagem")
            msg.setText('Em Classe Selecione uma opção válida')
            msg.exec_()
        elif self.combo_raca.currentText() == "Selecione uma opção":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro de Personagem")
            msg.setText('Em Raça Selecione uma opção válida')
            msg.exec_()
        elif self.combo_dados_vida.currentText() == "Selecione uma opção":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro de Personagem")
            msg.setText('Em Dados de Vida Selecione uma opção válida')
            msg.exec_()
        elif self.txt_total_pontos_vida.text() == "":
            campo = "Total de Pontos de vida"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_pontos_vida_atual.text() == "":
            campo = "Pontos de Vida Atual"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_pontos_experiencia.text() == "":
            campo = "Pontos de Experiência"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.combo_nivel_personagem.currentText() == "Selecionar":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro de Personagem")
            msg.setText('Em Nível de Personagem Selecione uma opção válida')
            msg.exec_()
        elif self.txt_pontos_heroicos.text() == "":
            campo = "Pontos Heróicos"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif not self.txt_total_pontos_vida.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro Personagem")
            msg.setText("Campo Total Pontos de Vida não pode ter letras.")
            msg.exec_()
        elif not self.txt_pontos_vida_atual.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro Personagem")
            msg.setText("Campo Pontos de Vida Atual não pode ter letras.")
            msg.exec_()
        elif not self.txt_pontos_experiencia.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro Personagem")
            msg.setText("Campo Pontos de Experiência não pode ter letras.")
            msg.exec_()
        elif not self.txt_pontos_heroicos.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro Personagem")
            msg.setText("Campo Ponto Heróico não pode ter letras.")
            msg.exec_()
        else:
            personagem = Personagem()
            personagem.nome_personagem = self.txt_nome_personagem.text()
            personagem.nome_classe = self.combo_classe.currentText()
            personagem.nome_raca = self.combo_raca.currentText()
            personagem.dados_vida = self.combo_dados_vida.currentText()
            personagem.total_pontos_vida = self.txt_total_pontos_vida.text()
            personagem.pontos_vida_atual = self.txt_pontos_vida_atual.text()
            personagem.pontos_experiencia = self.txt_pontos_experiencia.text()
            personagem.nivel = self.combo_nivel_personagem.currentText()
            personagem.ponto_heroico = self.txt_pontos_heroicos.text()
            personagem.situacao = "Em Combate"

            try:
                dao = PersonagemDao()
                dao.cadastrar_personagem(personagem.nome_personagem, personagem.nome_classe, personagem.nome_raca,
                                         personagem.dados_vida, personagem.total_pontos_vida,
                                         personagem.pontos_vida_atual, personagem.pontos_experiencia, personagem.nivel,
                                         personagem.ponto_heroico, personagem.situacao)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_ok.png")
                msg.setWindowTitle("Cadastro de Personagem")
                msg.setText(f'Personagem {personagem.nome_personagem} cadastrado com sucesso.')
                msg.exec_()

                self.limpar_tela()
                self.listar_personagem_tabela()
            except IntegrityError:
                self.mensagem.mensagem_de_erro()

    def carregar_campos(self):
        linha = self.tabela_personagem.currentItem().text()
        coluna = self.tabela_personagem.currentColumn()

        if coluna == 1:
            dao = PersonagemDao()
            resultado = dao.carregar_campos_personagem(linha)

            self.tab_personagem.setCurrentWidget(self.tab_cadastro_personagem)

            self.txt_id.setText(str(resultado[0][0]))
            self.txt_nome_personagem.setText(str(resultado[0][1]))
            self.combo_classe.setCurrentText(str(resultado[0][2]))
            self.combo_raca.setCurrentText(str(resultado[0][3]))
            self.combo_dados_vida.setCurrentText(str(resultado[0][4]))
            self.txt_total_pontos_vida.setText(str(resultado[0][5]))
            self.txt_pontos_vida_atual.setText(str(resultado[0][6]))
            self.txt_pontos_experiencia.setText(str(resultado[0][7]))
            self.combo_nivel_personagem.setCurrentText(str(resultado[0][8]))
            self.txt_pontos_heroicos.setText(str(resultado[0][9]))

            self.btn_cadastrar.setEnabled(False)
            self.btn_excluir.setEnabled(True)
            self.btn_alterar.setEnabled(True)
        else:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro de Personagem")
            msg.setText(f'Selecione o nome do Personagem na coluna Nome.')
            msg.exec_()

    def alterar_usuario(self):
        if self.txt_nome_personagem.text() == "":
            campo = "Nome do Personagem"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.combo_classe.currentText() == "Selecione uma opção":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro de Personagem")
            msg.setText('Em Classe Selecione uma opção válida')
            msg.exec_()
        elif self.combo_raca.currentText() == "Selecione uma opção":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro de Personagem")
            msg.setText('Em Raça Selecione uma opção válida')
            msg.exec_()
        elif self.combo_dados_vida.currentText() == "Selecione uma opção":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro de Personagem")
            msg.setText('Em Dados de Vida Selecione uma opção válida')
            msg.exec_()
        elif self.txt_total_pontos_vida.text() == "":
            campo = "Total de Pontos de vida"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_pontos_vida_atual.text() == "":
            campo = "Pontos de Vida Atual"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.txt_pontos_experiencia.text() == "":
            campo = "Pontos de Experiência"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif self.combo_nivel_personagem.currentText() == "Selecionar":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cadastro de Personagem")
            msg.setText('Em Nível de Personagem Selecione uma opção válida')
            msg.exec_()
        elif self.txt_pontos_heroicos.text() == "":
            campo = "Pontos Heróicos"
            self.mensagem.mensagem_campo_em_branco(campo)
        elif not self.txt_total_pontos_vida.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Alterar Personagem")
            msg.setText("Campo Total Pontos de Vida não pode ter letras.")
            msg.exec_()
        elif not self.txt_pontos_vida_atual.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Alterar Personagem")
            msg.setText("Campo Pontos de Vida Atual não pode ter letras.")
            msg.exec_()
        elif not self.txt_pontos_experiencia.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Alterar Personagem")
            msg.setText("Campo Pontos de Experiência não pode ter letras.")
            msg.exec_()
        elif not self.txt_pontos_heroicos.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Alterar Personagem")
            msg.setText("Campo Ponto Heróico não pode ter letras.")
            msg.exec_()
        else:
            personagem = Personagem()
            personagem.id_personagem = self.txt_id.text()
            personagem.nome_personagem = self.txt_nome_personagem.text()
            personagem.nome_classe = self.combo_classe.currentText()
            personagem.nome_raca = self.combo_raca.currentText()
            personagem.dados_vida = self.combo_dados_vida.currentText()
            personagem.total_pontos_vida = self.txt_total_pontos_vida.text()
            personagem.pontos_vida_atual = self.txt_pontos_vida_atual.text()
            personagem.pontos_experiencia = self.txt_pontos_experiencia.text()
            personagem.nivel = self.combo_nivel_personagem.currentText()
            personagem.ponto_heroico = self.txt_pontos_heroicos.text()

            try:
                dao = PersonagemDao()
                dao.alterar_cadastro_personagem(personagem.id_personagem, personagem.nome_personagem,
                                                personagem.nome_classe, personagem.nome_raca, personagem.dados_vida,
                                                personagem.total_pontos_vida, personagem.pontos_vida_atual,
                                                personagem.pontos_experiencia, personagem.nivel,
                                                personagem.ponto_heroico)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_ok.png")
                msg.setWindowTitle("Alterar de Personagem")
                msg.setText(f'Personagem {personagem.nome_personagem} atualizado com sucesso.')
                msg.exec_()

                self.limpar_tela()
                self.listar_personagem_tabela()
            except AttributeError:
                self.mensagem.mensagem_de_erro()

    def excluir_personagem(self):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
        msg.setIconPixmap("_img/botao_interrogacao.png")
        msg.setWindowTitle("Exclusão de Personagem")
        msg.setText("Tem certeza que deseja excluir o Personagem?")
        msg.setStandardButtons(QMessageBox.Yes)
        msg.addButton(QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        if msg.exec_() == QMessageBox.Yes:
            personagem = Personagem()
            personagem.id_personagem = self.txt_id.text()
            personagem.nome_personagem = self.txt_nome_personagem.text()

            try:
                dao = PersonagemDao()
                dao.excluir_personagem(personagem.id_personagem)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/logo_janela.ico"))
                msg.setIconPixmap("_img/botao_ok.png")
                msg.setWindowTitle("Exclusão de Chamado")
                msg.setText(f'Personagem {personagem.nome_personagem} excluido com sucesso!')
                msg.exec_()

                self.listar_personagem_tabela()
                self.limpar_tela()
            except AttributeError:
                self.mensagem.mensagem_de_erro()
