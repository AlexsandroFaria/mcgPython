from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QMainWindow, QMessageBox
from components.mensagens import Mensagens
from dao.combate_dao import CombateDao
from view.ui_tela_combate import Ui_TelaCombate


class TelaCombate(QMainWindow, Ui_TelaCombate):
    def __init__(self):
        super(TelaCombate, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Master Control Guide - Combate")
        self.setFixedSize(1083, 582)

        self.mensagem = Mensagens()
        self.btn_dano.setEnabled(False)
        self.btn_cura.setEnabled(False)
        self.btn_cura_monstro.setEnabled(False)
        self.btn_dano_monstro.setEnabled(False)

        self.listar_personagem_batalha()
        self.listar_inserir_monstros_combate()
        self.listar_tabela_monstro_combate()
        self.popular_combo_iniciativa_personagem()
        self.popular_combo_iniciativa_monstro()
        self.listar_iniciativa()

        self.btn_dano.clicked.connect(self.gerar_dano)
        self.btn_cura.clicked.connect(self.cura_personagem)
        self.btn_carregar.clicked.connect(self.carregar_personagem_batalha)
        self.btn_limpar_campos_personagem.clicked.connect(self.limpar_campos)
        self.btn_alterar_pontos_heroico.clicked.connect(self.alterar_ponto_heroico)
        self.btn_inserir_monstro_combate.clicked.connect(self.inserir_monstro_combate)
        self.btn_pesquisar_monstro.clicked.connect(self.consultar_monstro_inserir_combate_nome)
        self.btn_limpar_monstro_combate.clicked.connect(self.apagar_registros_tabela_monstro_combate)
        self.btn_carregar_monstro.clicked.connect(self.carregar_monstro_combate)
        self.btn_dano_monstro.clicked.connect(self.gerar_dano_monstro)
        self.btn_cura_monstro.clicked.connect(self.cura_monstro)
        self.btn_adicionar_personagem_iniciativa.clicked.connect(self.incluir_personagem_iniciativa)
        self.btn_limpar_tabela_iniciativa.clicked.connect(self.limpar_tabela_iniciativa)
        self.btn_adicionar_monstro_iniciativa.clicked.connect(self.incluir_monstro_iniciativa)

    def listar_personagem_batalha(self):
        try:
            dao = CombateDao()
            resultado = dao.listar_personagem_batalha()

            self.tabela_personagem_batalha.setRowCount(len(resultado))
            self.tabela_personagem_batalha.setColumnCount(6)

            for i in range(0, len(resultado)):
                for j in range(0, 6):
                    self.tabela_personagem_batalha.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def listar_inserir_monstros_combate(self):
        try:
            dao = CombateDao()
            resultado = dao.listar_inserir_monstros_tabela()

            self.tabela_inserir_monstro_combate.setRowCount(len(resultado))
            self.tabela_inserir_monstro_combate.setColumnCount(7)

            for i in range(0, len(resultado)):
                for j in range(0, 7):
                    self.tabela_inserir_monstro_combate.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def carregar_personagem_batalha(self):
        linha = self.tabela_personagem_batalha.currentItem().text()
        coluna = self.tabela_personagem_batalha.currentColumn()

        if coluna == 0:
            try:
                dao = CombateDao()
                resultado = dao.carregar_personagem_combate(linha)

                self.txt_nome.setText(str(resultado[0][0]))
                self.txt_pontos_vida.setText(str(resultado[0][1]))
                self.combo_ponto_heroico.setCurrentText(str(resultado[0][2]))

                self.btn_dano.setEnabled(True)
                self.btn_cura.setEnabled(True)
            except AttributeError:
                self.mensagem.mensagem_de_erro()
        else:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Carregar Personagem")
            msg.setText(f'Selecione o nome do Personagem na coluna Nome.')
            msg.exec_()

    def gerar_dano(self):
        if self.txt_nome.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Dano")
            msg.setText('Carregue um Personagem.')
            msg.exec_()
        elif not self.txt_dano_cura.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Dano")
            msg.setText('No campo de Dano informe somente números.')
            msg.exec_()
        else:
            nome = self.txt_nome.text()
            dano = self.txt_dano_cura.text()
            pontos_vida = self.txt_pontos_vida.text()

            if dano == "":
                campo = "Dano / Cura"
                self.mensagem.mensagem_campo_em_branco(campo)
            else:
                dano_sofrido = int(pontos_vida) - int(dano)

                if dano_sofrido <= 0:
                    situacao = "Morto em Combate"
                    dano_sofrido = 0

                    dao = CombateDao()
                    dao.dano_morte(dano_sofrido, situacao, nome)

                    self.listar_personagem_batalha()
                    self.limpar_campos()

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_morte.png")
                    msg.setWindowTitle("Dano")
                    msg.setText(f'{nome} recebeu {dano} de dano e Morreu em Combate.')
                    msg.exec_()
                else:
                    dao = CombateDao()
                    dao.dano(dano_sofrido, nome)

                    self.listar_personagem_batalha()
                    self.limpar_campos()

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_dano.png")
                    msg.setWindowTitle("Dano")
                    msg.setText(f'{nome} recebeu {dano} de dano...')
                    msg.exec_()

    def cura_personagem(self):
        if self.txt_nome.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Cura")
            msg.setText('Carregue um personagem.')
            msg.exec_()
        elif not self.txt_dano_cura.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Dano")
            msg.setText('No campo de Dano informe somente números.')
            msg.exec_()
        else:
            nome = self.txt_nome.text()
            cura = self.txt_dano_cura.text()
            pontos_vida = self.txt_pontos_vida.text()

            if cura == "":
                campo = "Cura / Dano"
                self.mensagem.mensagem_campo_em_branco(campo)
            else:
                cura_personagem = int(pontos_vida) + int(cura)
                situacao = "Em Combate"

                dao = CombateDao()
                dao.cura(cura_personagem, situacao, nome)

                self.limpar_campos()
                self.listar_personagem_batalha()

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_cura.png")
                msg.setWindowTitle("Dano")
                msg.setText(f'{nome} recebeu {cura} de cura...')
                msg.exec_()

    def alterar_ponto_heroico(self):
        if self.combo_ponto_heroico.currentText() == "Selecionar":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Ponto Heróico")
            msg.setText('Selecione uma opção no campo Ponto Heróico')
            msg.exec_()
        else:
            nome = self.txt_nome.text()
            ponto_heroico = self.combo_ponto_heroico.currentText()

            try:
                dao = CombateDao()
                dao.alterar_ponto_heroico(ponto_heroico, nome)

                self.limpar_campos()
                self.listar_personagem_batalha()

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_exclamacao.png")
                msg.setWindowTitle("Ponto Heróico")
                msg.setText(f'Ponto heróico do personagem {nome} alterado com sucesso.')
                msg.exec_()
            except AttributeError:
                self.mensagem.mensagem_de_erro()

    def limpar_campos(self):
        self.txt_nome.setText("")
        self.txt_pontos_vida.setText("")
        self.txt_dano_cura.setText("")
        self.combo_ponto_heroico.setCurrentText("Selecionar")

    def listar_tabela_monstro_combate(self):
        try:
            dao = CombateDao()
            resultado = dao.listar_tabela_monstro_combate()

            self.tabela_monstro_batalha.setRowCount(len(resultado))
            self.tabela_monstro_batalha.setColumnCount(8)

            for i in range(0, len(resultado)):
                for j in range(0, 8):
                    self.tabela_monstro_batalha.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def inserir_monstro_combate(self):
        try:
            linha = self.tabela_inserir_monstro_combate.currentItem().text()
            coluna = self.tabela_inserir_monstro_combate.currentColumn()

            if coluna == 0:
                try:
                    dao = CombateDao()
                    resultado = dao.consultar_monstro_inserir_combate(linha)

                    nome = resultado[0][1]
                    classe_armadura = resultado[0][2]
                    pontos_vida_atual = resultado[0][3]
                    deslocamento = resultado[0][4]
                    nivel_desafio = resultado[0][5]
                    referencia = resultado[0][6]
                    situacao = "Em Combate"

                    dao.inserir_monstro_combate(nome, classe_armadura, pontos_vida_atual, deslocamento, nivel_desafio,
                                                referencia, situacao)

                    self.listar_tabela_monstro_combate()

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_exclamacao.png")
                    msg.setWindowTitle("Monstros em Combate")
                    msg.setText("Monstro inserido em combate.")
                    msg.exec_()
                except AttributeError:
                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_exclamacao.png")
                    msg.setWindowTitle("Inserir Monstro Batalha")
                    msg.setText(f'Nenhum Monstro Selecionado.')
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_exclamacao.png")
                msg.setWindowTitle("Inserir Monstro Batalha")
                msg.setText(f'Selecione o Monstrom na coluna ID.')
                msg.exec_()
        except AttributeError:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Inserir Monstro Batalha")
            msg.setText(f'Nenhum Monstro Selecionado.')
            msg.exec_()

    def consultar_monstro_inserir_combate_nome(self):

        nome = self.txt_pesquisar_monstro_nome.text()

        try:
            dao = CombateDao()
            resultado = dao.pesquisar_monstro_inserir_combate_nome(nome)

            self.tabela_inserir_monstro_combate.setRowCount(len(resultado))
            self.tabela_inserir_monstro_combate.setColumnCount(7)

            for i in range(0, len(resultado)):
                for j in range(0, 7):
                    self.tabela_inserir_monstro_combate.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))

                self.txt_pesquisar_monstro_nome.setText("")
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def apagar_registros_tabela_monstro_combate(self):
        try:
            dao = CombateDao()
            dao.apagar_registros_tabela_montro_combate()

            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Limpar Monstros em Combate")
            msg.setText('Efetuado limpeza dos monstros em combate.')
            msg.exec_()

            self.listar_tabela_monstro_combate()
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def carregar_monstro_combate(self):
        linha = self.tabela_monstro_batalha.currentItem().text()
        coluna = self.tabela_monstro_batalha.currentColumn()

        if coluna == 0:
            try:
                dao = CombateDao()
                resultado = dao.carregar_monstro_combate(linha)

                self.txt_id_monstro.setText(str(resultado[0][0]))
                self.txt_nome_monstro.setText(str(resultado[0][1]))
                self.txt_pontos_vida_monstro.setText(str(resultado[0][2]))

                self.btn_dano_monstro.setEnabled(True)
                self.btn_cura_monstro.setEnabled(True)
            except AttributeError:
                self.mensagem.mensagem_de_erro()
        else:
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Inserir Monstro Combate")
            msg.setText(f'Selecione o Monstro pela coluna ID.')
            msg.exec_()

    def limpar_campos_monstro_combate(self):
        self.txt_id_monstro.setText("")
        self.txt_nome_monstro.setText("")
        self.txt_pontos_vida_monstro.setText("")
        self.txt_dano_cura_monstro.setText("")

        self.btn_cura_monstro.setEnabled(False)
        self.btn_dano_monstro.setEnabled(False)

    def gerar_dano_monstro(self):
        if self.txt_id_monstro.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Dano")
            msg.setText('Carregue um Monstro.')
            msg.exec_()
        elif not self.txt_dano_cura_monstro.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Dano")
            msg.setText('No campo de Dano informe somente números.')
            msg.exec_()
        else:
            id = self.txt_id_monstro.text()
            nome = self.txt_nome_monstro.text()
            pontos_vida_monstro = self.txt_pontos_vida_monstro.text()
            dano = self.txt_dano_cura_monstro.text()

            if id == 0:
                campo = "Dano / Cura"
                self.mensagem.mensagem_campo_em_branco(campo)
            else:
                dano_sofrido_monstro = int(pontos_vida_monstro) - int(dano)

                if dano_sofrido_monstro <= 0:
                    situacao = "Morto em Combate"
                    dano_sofrido_monstro = 0

                    dao = CombateDao()
                    dao.dano_morte_monstro(dano_sofrido_monstro, situacao, id)

                    self.listar_tabela_monstro_combate()
                    self.limpar_campos_monstro_combate()

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_morte.png")
                    msg.setWindowTitle("Dano")
                    msg.setText(f'{nome} recebeu {dano} de dano e Morreu em Combate.')
                    msg.exec_()
                else:
                    dao = CombateDao()
                    dao.dano_monstro(dano_sofrido_monstro, id)

                    self.listar_tabela_monstro_combate()
                    self.limpar_campos_monstro_combate()

                    msg = QMessageBox()
                    msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                    msg.setIconPixmap("_img/botao_dano.png")
                    msg.setWindowTitle("Dano")
                    msg.setText(f'{nome} recebeu {dano} de dano.')
                    msg.exec_()

    def cura_monstro(self):
        if self.txt_id_monstro.text() == "":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Dano")
            msg.setText('Carregue um Monstro.')
            msg.exec_()
        elif not self.txt_dano_cura_monstro.text().isdigit():
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Dano")
            msg.setText('No campo de Dano informe somente números.')
            msg.exec_()
        else:
            id = self.txt_id_monstro.text()
            nome = self.txt_nome_monstro.text()
            pontos_vida_monstro = self.txt_pontos_vida_monstro.text()
            cura = self.txt_dano_cura_monstro.text()

            if id == 0:
                campo = "Dano / Cura"
                self.mensagem.mensagem_campo_em_branco(campo)
            else:
                cura_monstro = int(pontos_vida_monstro) + int(cura)
                situacao = "Em Combate"

                dao = CombateDao()
                dao.cura_monstro(cura_monstro, situacao, id)

                self.limpar_campos_monstro_combate()
                self.listar_tabela_monstro_combate()

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_cura.png")
                msg.setWindowTitle("Cura Monstro")
                msg.setText(f'{nome} recebeu {cura} de cura...')
                msg.exec_()

    def popular_combo_iniciativa_personagem(self):
        try:
            dao = CombateDao()
            resultado = dao.popular_combo_personagem()

            for i in resultado:
                self.combo_iniciatita_personagem.addItem(str(i[0]))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def popular_combo_iniciativa_monstro(self):
        try:
            dao = CombateDao()
            resultado = dao.popular_combo_monstro()

            for i in resultado:
                self.combo_iniciatita_monstro.addItem(str(i[0]))
        except AttributeError:
            self.mensagem.mensagem_de_erro()

    def incluir_personagem_iniciativa(self):
        if self.combo_iniciatita_personagem.currentText() == "Selecionar":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Seleção de Personagem")
            msg.setText(f'Selecione um personagem.')
            msg.exec_()
        elif self.txt_iniciativa_personagem.text() == "":
            campo = "Valor iniciativa do personagem"
            self.mensagem.mensagem_campo_em_branco(campo)
        else:
            personagem = self.combo_iniciatita_personagem.currentText()
            valor_iniciativa = self.txt_iniciativa_personagem.text()

            try:
                dao = CombateDao()
                dao.incluir_iniciativa(personagem, valor_iniciativa)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_ok.png")
                msg.setWindowTitle("Iniciativa Personagem")
                msg.setText(f'Personagem inserido na Iniciativa com sucesso.')
                msg.exec_()

                self.limpar_tela_iniciativa()
                self.listar_iniciativa()
            except AttributeError:
                self.mensagem.mensagem_de_erro()

    def incluir_monstro_iniciativa(self):
        if self.combo_iniciatita_monstro.currentText() == "Selecionar":
            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_exclamacao.png")
            msg.setWindowTitle("Seleção de Monstro")
            msg.setText(f'Selecione um Monstro.')
            msg.exec_()
        elif self.txt_iniciativa_monstro.text() == "":
            campo = "Valor iniciativa do Monstro"
            self.mensagem.mensagem_campo_em_branco(campo)
        else:
            monstro = self.combo_iniciatita_monstro.currentText()
            valor_iniciativa = self.txt_iniciativa_monstro.text()

            try:
                dao = CombateDao()
                dao.incluir_iniciativa(monstro, valor_iniciativa)

                msg = QMessageBox()
                msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
                msg.setIconPixmap("_img/botao_ok.png")
                msg.setWindowTitle("Iniciativa Monstro")
                msg.setText(f'Monstro inserido na Iniciativa com sucesso.')
                msg.exec_()

                self.limpar_tela_iniciativa()
                self.listar_iniciativa()
            except AttributeError:
                self.mensagem.mensagem_de_erro()

    def listar_iniciativa(self):
        try:
            dao = CombateDao()
            resultado = dao.listar_tabela_iniciativa()

            self.tabela_iniciativa.setRowCount(len(resultado))
            self.tabela_iniciativa.setColumnCount(2)

            for i in range(len(resultado)):
                for j in range(0, 2):
                    self.tabela_iniciativa.setItem(i, j, QtWidgets.QTableWidgetItem(str(resultado[i][j])))
        except AttributeError as erro:
            self.mensagem.mensagem_de_erro()
            print(erro)

    def limpar_tela_iniciativa(self):
        self.combo_iniciatita_personagem.setCurrentText("selecionar")
        self.combo_iniciatita_monstro.setCurrentText("Selecionar")
        self.txt_iniciativa_personagem.setText("")
        self.txt_iniciativa_monstro.setText("")

    def limpar_tabela_iniciativa(self):
        try:
            dao = CombateDao()
            dao.limpar_tabela_iniciativa()

            msg = QMessageBox()
            msg.setWindowIcon(QtGui.QIcon("_img/icone_principal.png"))
            msg.setIconPixmap("_img/botao_ok.png")
            msg.setWindowTitle("Iniciativa Personagem")
            msg.setText('Lista de Iniciativa excluída com sucesso.')
            msg.exec_()

            self.listar_iniciativa()
        except AttributeError:
            self.mensagem.mensagem_de_erro()
