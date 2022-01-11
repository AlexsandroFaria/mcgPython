# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_combate.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaCombate(object):
    def setupUi(self, TelaCombate):
        if not TelaCombate.objectName():
            TelaCombate.setObjectName(u"TelaCombate")
        TelaCombate.resize(1083, 585)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        TelaCombate.setWindowIcon(icon)
        self.frame = QFrame(TelaCombate)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1081, 141))
        self.frame.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1081, 141))
        self.label.setPixmap(QPixmap(u"_img/banner_combate.png"))
        self.tav_combate = QTabWidget(TelaCombate)
        self.tav_combate.setObjectName(u"tav_combate")
        self.tav_combate.setGeometry(QRect(10, 160, 1061, 391))
        font = QFont()
        font.setFamily(u"Elephant")
        font.setPointSize(12)
        self.tav_combate.setFont(font)
        self.tav_combate.setStyleSheet(u"background-color: rgb(241, 241, 241);")
        self.tav_combate.setIconSize(QSize(24, 24))
        self.tab_personagens = QWidget()
        self.tab_personagens.setObjectName(u"tab_personagens")
        self.tabela_personagem_batalha = QTableWidget(self.tab_personagens)
        if (self.tabela_personagem_batalha.columnCount() < 6):
            self.tabela_personagem_batalha.setColumnCount(6)
        font1 = QFont()
        font1.setFamily(u"Elephant")
        font1.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tabela_personagem_batalha.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tabela_personagem_batalha.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tabela_personagem_batalha.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tabela_personagem_batalha.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tabela_personagem_batalha.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tabela_personagem_batalha.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabela_personagem_batalha.setObjectName(u"tabela_personagem_batalha")
        self.tabela_personagem_batalha.setGeometry(QRect(10, 10, 631, 151))
        self.tabela_personagem_batalha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabela_personagem_batalha.setAlternatingRowColors(True)
        self.tabela_personagem_batalha.verticalHeader().setVisible(False)
        self.label_2 = QLabel(self.tab_personagens)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 210, 131, 21))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.tab_personagens)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 250, 111, 21))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.tab_personagens)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 290, 131, 21))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.tab_personagens)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 175, 161, 21))
        font2 = QFont()
        font2.setFamily(u"Elephant")
        font2.setPointSize(8)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_nome = QLineEdit(self.tab_personagens)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setEnabled(False)
        self.txt_nome.setGeometry(QRect(190, 170, 281, 25))
        self.txt_nome.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setFamily(u"Elephant")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.txt_nome.setFont(font3)
        self.txt_nome.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"")
        self.txt_pontos_vida = QLineEdit(self.tab_personagens)
        self.txt_pontos_vida.setObjectName(u"txt_pontos_vida")
        self.txt_pontos_vida.setEnabled(False)
        self.txt_pontos_vida.setGeometry(QRect(190, 210, 81, 25))
        self.txt_pontos_vida.setMinimumSize(QSize(0, 25))
        self.txt_pontos_vida.setFont(font1)
        self.txt_pontos_vida.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"")
        self.txt_dano_cura = QLineEdit(self.tab_personagens)
        self.txt_dano_cura.setObjectName(u"txt_dano_cura")
        self.txt_dano_cura.setGeometry(QRect(190, 250, 81, 25))
        self.txt_dano_cura.setMinimumSize(QSize(0, 25))
        self.txt_dano_cura.setFont(font1)
        self.txt_dano_cura.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"")
        self.btn_carregar = QPushButton(self.tab_personagens)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setGeometry(QRect(500, 170, 131, 31))
        font4 = QFont()
        font4.setFamily(u"Elephant")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.btn_carregar.setFont(font4)
        self.btn_carregar.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon1)
        self.btn_carregar.setIconSize(QSize(24, 24))
        self.btn_dano = QPushButton(self.tab_personagens)
        self.btn_dano.setObjectName(u"btn_dano")
        self.btn_dano.setGeometry(QRect(280, 200, 91, 41))
        self.btn_dano.setFont(font4)
        self.btn_dano.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 0, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"_img/dano.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dano.setIcon(icon2)
        self.btn_dano.setIconSize(QSize(32, 32))
        self.btn_cura = QPushButton(self.tab_personagens)
        self.btn_cura.setObjectName(u"btn_cura")
        self.btn_cura.setGeometry(QRect(380, 200, 91, 41))
        self.btn_cura.setFont(font4)
        self.btn_cura.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(32, 127, 48);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"_img/cura.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cura.setIcon(icon3)
        self.btn_cura.setIconSize(QSize(32, 32))
        self.btn_limpar_campos_personagem = QPushButton(self.tab_personagens)
        self.btn_limpar_campos_personagem.setObjectName(u"btn_limpar_campos_personagem")
        self.btn_limpar_campos_personagem.setGeometry(QRect(280, 250, 191, 31))
        self.btn_limpar_campos_personagem.setFont(font4)
        self.btn_limpar_campos_personagem.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"_img/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_campos_personagem.setIcon(icon4)
        self.btn_limpar_campos_personagem.setIconSize(QSize(24, 24))
        self.btn_alterar_pontos_heroico = QPushButton(self.tab_personagens)
        self.btn_alterar_pontos_heroico.setObjectName(u"btn_alterar_pontos_heroico")
        self.btn_alterar_pontos_heroico.setGeometry(QRect(280, 290, 191, 31))
        self.btn_alterar_pontos_heroico.setFont(font1)
        self.btn_alterar_pontos_heroico.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"_img/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar_pontos_heroico.setIcon(icon5)
        self.btn_alterar_pontos_heroico.setIconSize(QSize(24, 24))
        self.label_6 = QLabel(self.tab_personagens)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(500, 210, 121, 111))
        self.label_6.setPixmap(QPixmap(u"_img/gladiador.png"))
        self.label_7 = QLabel(self.tab_personagens)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(660, 20, 361, 271))
        self.label_7.setPixmap(QPixmap(u"_img/combate.png"))
        self.combo_ponto_heroico = QComboBox(self.tab_personagens)
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.addItem("")
        self.combo_ponto_heroico.setObjectName(u"combo_ponto_heroico")
        self.combo_ponto_heroico.setGeometry(QRect(180, 290, 91, 25))
        self.combo_ponto_heroico.setMinimumSize(QSize(0, 25))
        self.combo_ponto_heroico.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u"_img/personagem.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tav_combate.addTab(self.tab_personagens, icon6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.btn_carregar_monstro = QPushButton(self.tab_2)
        self.btn_carregar_monstro.setObjectName(u"btn_carregar_monstro")
        self.btn_carregar_monstro.setGeometry(QRect(340, 180, 131, 31))
        self.btn_carregar_monstro.setFont(font4)
        self.btn_carregar_monstro.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        self.btn_carregar_monstro.setIcon(icon1)
        self.btn_carregar_monstro.setIconSize(QSize(24, 24))
        self.btn_cura_monstro = QPushButton(self.tab_2)
        self.btn_cura_monstro.setObjectName(u"btn_cura_monstro")
        self.btn_cura_monstro.setGeometry(QRect(380, 250, 91, 41))
        self.btn_cura_monstro.setFont(font4)
        self.btn_cura_monstro.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(85, 170, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(32, 127, 48);\n"
"}")
        self.btn_cura_monstro.setIcon(icon3)
        self.btn_cura_monstro.setIconSize(QSize(32, 32))
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 225, 161, 21))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_pontos_vida_monstro = QLineEdit(self.tab_2)
        self.txt_pontos_vida_monstro.setObjectName(u"txt_pontos_vida_monstro")
        self.txt_pontos_vida_monstro.setEnabled(False)
        self.txt_pontos_vida_monstro.setGeometry(QRect(190, 260, 81, 25))
        self.txt_pontos_vida_monstro.setMinimumSize(QSize(0, 25))
        self.txt_pontos_vida_monstro.setFont(font1)
        self.txt_pontos_vida_monstro.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"")
        self.btn_limpar_campos_monstro = QPushButton(self.tab_2)
        self.btn_limpar_campos_monstro.setObjectName(u"btn_limpar_campos_monstro")
        self.btn_limpar_campos_monstro.setGeometry(QRect(280, 300, 191, 31))
        self.btn_limpar_campos_monstro.setFont(font4)
        self.btn_limpar_campos_monstro.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        self.btn_limpar_campos_monstro.setIcon(icon4)
        self.btn_limpar_campos_monstro.setIconSize(QSize(24, 24))
        self.txt_dano_cura_monstro = QLineEdit(self.tab_2)
        self.txt_dano_cura_monstro.setObjectName(u"txt_dano_cura_monstro")
        self.txt_dano_cura_monstro.setGeometry(QRect(190, 300, 81, 25))
        self.txt_dano_cura_monstro.setMinimumSize(QSize(0, 25))
        self.txt_dano_cura_monstro.setFont(font1)
        self.txt_dano_cura_monstro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"")
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(40, 260, 131, 21))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.tabela_monstro_batalha = QTableWidget(self.tab_2)
        if (self.tabela_monstro_batalha.columnCount() < 8):
            self.tabela_monstro_batalha.setColumnCount(8)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tabela_monstro_batalha.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tabela_monstro_batalha.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.tabela_monstro_batalha.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.tabela_monstro_batalha.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.tabela_monstro_batalha.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.tabela_monstro_batalha.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.tabela_monstro_batalha.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.tabela_monstro_batalha.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        self.tabela_monstro_batalha.setObjectName(u"tabela_monstro_batalha")
        self.tabela_monstro_batalha.setGeometry(QRect(10, 20, 861, 151))
        self.tabela_monstro_batalha.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabela_monstro_batalha.setAlternatingRowColors(True)
        self.tabela_monstro_batalha.verticalHeader().setVisible(False)
        self.btn_dano_monstro = QPushButton(self.tab_2)
        self.btn_dano_monstro.setObjectName(u"btn_dano_monstro")
        self.btn_dano_monstro.setGeometry(QRect(280, 250, 91, 41))
        self.btn_dano_monstro.setFont(font4)
        self.btn_dano_monstro.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(156, 0, 0);\n"
"}")
        self.btn_dano_monstro.setIcon(icon2)
        self.btn_dano_monstro.setIconSize(QSize(32, 32))
        self.txt_nome_monstro = QLineEdit(self.tab_2)
        self.txt_nome_monstro.setObjectName(u"txt_nome_monstro")
        self.txt_nome_monstro.setEnabled(False)
        self.txt_nome_monstro.setGeometry(QRect(190, 220, 281, 25))
        self.txt_nome_monstro.setMinimumSize(QSize(0, 25))
        self.txt_nome_monstro.setFont(font3)
        self.txt_nome_monstro.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"")
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 300, 111, 21))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(150, 190, 47, 13))
        self.label_11.setFont(font)
        self.txt_id_monstro = QLineEdit(self.tab_2)
        self.txt_id_monstro.setObjectName(u"txt_id_monstro")
        self.txt_id_monstro.setGeometry(QRect(190, 180, 101, 25))
        self.txt_id_monstro.setMinimumSize(QSize(0, 25))
        self.txt_id_monstro.setFont(font1)
        self.txt_id_monstro.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"")
        self.btn_limpar_monstro_combate = QPushButton(self.tab_2)
        self.btn_limpar_monstro_combate.setObjectName(u"btn_limpar_monstro_combate")
        self.btn_limpar_monstro_combate.setGeometry(QRect(490, 180, 241, 31))
        self.btn_limpar_monstro_combate.setMinimumSize(QSize(0, 25))
        self.btn_limpar_monstro_combate.setFont(font1)
        self.btn_limpar_monstro_combate.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        self.btn_limpar_monstro_combate.setIcon(icon4)
        self.btn_limpar_monstro_combate.setIconSize(QSize(24, 24))
        self.label_12 = QLabel(self.tab_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(490, 220, 251, 111))
        self.label_12.setPixmap(QPixmap(u"_img/ouro.png"))
        icon7 = QIcon()
        icon7.addFile(u"_img/dragon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tav_combate.addTab(self.tab_2, icon7, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabela_inserir_monstro_combate = QTableWidget(self.tab)
        if (self.tabela_inserir_monstro_combate.columnCount() < 7):
            self.tabela_inserir_monstro_combate.setColumnCount(7)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.tabela_inserir_monstro_combate.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font1);
        self.tabela_inserir_monstro_combate.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font1);
        self.tabela_inserir_monstro_combate.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font1);
        self.tabela_inserir_monstro_combate.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font1);
        self.tabela_inserir_monstro_combate.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font1);
        self.tabela_inserir_monstro_combate.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font1);
        self.tabela_inserir_monstro_combate.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        self.tabela_inserir_monstro_combate.setObjectName(u"tabela_inserir_monstro_combate")
        self.tabela_inserir_monstro_combate.setGeometry(QRect(20, 140, 721, 151))
        self.tabela_inserir_monstro_combate.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabela_inserir_monstro_combate.setAlternatingRowColors(True)
        self.tabela_inserir_monstro_combate.verticalHeader().setVisible(False)
        self.btn_inserir_monstro_combate = QPushButton(self.tab)
        self.btn_inserir_monstro_combate.setObjectName(u"btn_inserir_monstro_combate")
        self.btn_inserir_monstro_combate.setGeometry(QRect(30, 310, 271, 30))
        self.btn_inserir_monstro_combate.setFont(font1)
        self.btn_inserir_monstro_combate.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        self.btn_inserir_monstro_combate.setIcon(icon7)
        self.btn_inserir_monstro_combate.setIconSize(QSize(24, 24))
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 20, 381, 80))
        self.groupBox.setFont(font)
        self.groupBox.setFocusPolicy(Qt.NoFocus)
        self.groupBox.setContextMenuPolicy(Qt.NoContextMenu)
        self.groupBox.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"")
        self.txt_pesquisar_monstro_nome = QLineEdit(self.groupBox)
        self.txt_pesquisar_monstro_nome.setObjectName(u"txt_pesquisar_monstro_nome")
        self.txt_pesquisar_monstro_nome.setGeometry(QRect(20, 40, 211, 25))
        self.txt_pesquisar_monstro_nome.setMinimumSize(QSize(0, 25))
        self.txt_pesquisar_monstro_nome.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"")
        self.btn_pesquisar_monstro = QPushButton(self.groupBox)
        self.btn_pesquisar_monstro.setObjectName(u"btn_pesquisar_monstro")
        self.btn_pesquisar_monstro.setGeometry(QRect(250, 32, 111, 31))
        self.btn_pesquisar_monstro.setFont(font1)
        self.btn_pesquisar_monstro.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"_img/pesquisar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar_monstro.setIcon(icon8)
        self.btn_pesquisar_monstro.setIconSize(QSize(24, 24))
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(430, 10, 331, 111))
        self.label_13.setPixmap(QPixmap(u"_img/monstro.png"))
        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(810, 30, 201, 321))
        self.label_14.setPixmap(QPixmap(u"_img/monstro_2.png"))
        icon9 = QIcon()
        icon9.addFile(u"_img/batalha.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tav_combate.addTab(self.tab, icon9, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.groupBox_2 = QGroupBox(self.tab_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 60, 431, 101))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"")
        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(80, 30, 101, 21))
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"border: 0px")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_16 = QLabel(self.groupBox_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(100, 62, 81, 21))
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"border: opx")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.combo_iniciatita_personagem = QComboBox(self.groupBox_2)
        self.combo_iniciatita_personagem.addItem("")
        self.combo_iniciatita_personagem.setObjectName(u"combo_iniciatita_personagem")
        self.combo_iniciatita_personagem.setGeometry(QRect(200, 30, 201, 25))
        self.combo_iniciatita_personagem.setMinimumSize(QSize(0, 25))
        self.combo_iniciatita_personagem.setFont(font1)
        self.txt_iniciativa_personagem = QLineEdit(self.groupBox_2)
        self.txt_iniciativa_personagem.setObjectName(u"txt_iniciativa_personagem")
        self.txt_iniciativa_personagem.setGeometry(QRect(200, 60, 61, 25))
        self.txt_iniciativa_personagem.setMinimumSize(QSize(0, 25))
        self.txt_iniciativa_personagem.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"")
        self.btn_adicionar_personagem_iniciativa = QPushButton(self.groupBox_2)
        self.btn_adicionar_personagem_iniciativa.setObjectName(u"btn_adicionar_personagem_iniciativa")
        self.btn_adicionar_personagem_iniciativa.setGeometry(QRect(280, 60, 121, 25))
        self.btn_adicionar_personagem_iniciativa.setMinimumSize(QSize(0, 25))
        self.btn_adicionar_personagem_iniciativa.setFont(font1)
        self.btn_adicionar_personagem_iniciativa.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        self.btn_adicionar_personagem_iniciativa.setIcon(icon9)
        self.btn_adicionar_personagem_iniciativa.setIconSize(QSize(24, 24))
        self.label_17 = QLabel(self.groupBox_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 20, 71, 71))
        self.label_17.setStyleSheet(u"border: opx")
        self.label_17.setPixmap(QPixmap(u"_img/knight.png"))
        self.groupBox_3 = QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(20, 200, 431, 101))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"")
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(80, 30, 101, 21))
        self.label_18.setFont(font1)
        self.label_18.setStyleSheet(u"border: 0px")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(100, 62, 81, 21))
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"border: opx")
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.combo_iniciatita_monstro = QComboBox(self.groupBox_3)
        self.combo_iniciatita_monstro.addItem("")
        self.combo_iniciatita_monstro.setObjectName(u"combo_iniciatita_monstro")
        self.combo_iniciatita_monstro.setGeometry(QRect(200, 30, 201, 25))
        self.combo_iniciatita_monstro.setMinimumSize(QSize(0, 25))
        self.combo_iniciatita_monstro.setFont(font1)
        self.txt_iniciativa_monstro = QLineEdit(self.groupBox_3)
        self.txt_iniciativa_monstro.setObjectName(u"txt_iniciativa_monstro")
        self.txt_iniciativa_monstro.setGeometry(QRect(200, 60, 61, 25))
        self.txt_iniciativa_monstro.setMinimumSize(QSize(0, 25))
        self.txt_iniciativa_monstro.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"")
        self.btn_adicionar_monstro_iniciativa = QPushButton(self.groupBox_3)
        self.btn_adicionar_monstro_iniciativa.setObjectName(u"btn_adicionar_monstro_iniciativa")
        self.btn_adicionar_monstro_iniciativa.setGeometry(QRect(280, 60, 121, 25))
        self.btn_adicionar_monstro_iniciativa.setMinimumSize(QSize(0, 25))
        self.btn_adicionar_monstro_iniciativa.setFont(font1)
        self.btn_adicionar_monstro_iniciativa.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        self.btn_adicionar_monstro_iniciativa.setIcon(icon9)
        self.btn_adicionar_monstro_iniciativa.setIconSize(QSize(24, 24))
        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(20, 20, 71, 71))
        self.label_20.setStyleSheet(u"border: opx")
        self.label_20.setPixmap(QPixmap(u"_img/monster.png"))
        self.tabela_iniciativa = QTableWidget(self.tab_3)
        if (self.tabela_iniciativa.columnCount() < 2):
            self.tabela_iniciativa.setColumnCount(2)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font1);
        self.tabela_iniciativa.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font1);
        self.tabela_iniciativa.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        self.tabela_iniciativa.setObjectName(u"tabela_iniciativa")
        self.tabela_iniciativa.setGeometry(QRect(460, 60, 301, 241))
        self.tabela_iniciativa.setAlternatingRowColors(True)
        self.tabela_iniciativa.verticalHeader().setVisible(False)
        self.label_21 = QLabel(self.tab_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(820, 10, 191, 321))
        self.label_21.setPixmap(QPixmap(u"_img/arqueiro.png"))
        self.btn_limpar_tabela_iniciativa = QPushButton(self.tab_3)
        self.btn_limpar_tabela_iniciativa.setObjectName(u"btn_limpar_tabela_iniciativa")
        self.btn_limpar_tabela_iniciativa.setGeometry(QRect(460, 312, 301, 31))
        self.btn_limpar_tabela_iniciativa.setFont(font)
        self.btn_limpar_tabela_iniciativa.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(241, 241, 241);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"}")
        self.btn_limpar_tabela_iniciativa.setIcon(icon4)
        self.btn_limpar_tabela_iniciativa.setIconSize(QSize(24, 24))
        icon10 = QIcon()
        icon10.addFile(u"_img/iniciativa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tav_combate.addTab(self.tab_3, icon10, "")

        self.retranslateUi(TelaCombate)

        self.tav_combate.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TelaCombate)
    # setupUi

    def retranslateUi(self, TelaCombate):
        TelaCombate.setWindowTitle(QCoreApplication.translate("TelaCombate", u"Form", None))
        self.label.setText("")
        ___qtablewidgetitem = self.tabela_personagem_batalha.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaCombate", u"Nome", None));
        ___qtablewidgetitem1 = self.tabela_personagem_batalha.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaCombate", u"Total P.V.", None));
        ___qtablewidgetitem2 = self.tabela_personagem_batalha.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaCombate", u"P.V. Atual", None));
        ___qtablewidgetitem3 = self.tabela_personagem_batalha.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TelaCombate", u"N\u00edvel", None));
        ___qtablewidgetitem4 = self.tabela_personagem_batalha.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TelaCombate", u"Ponto Her\u00f3ico", None));
        ___qtablewidgetitem5 = self.tabela_personagem_batalha.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TelaCombate", u"Situa\u00e7\u00e3o", None));
        self.label_2.setText(QCoreApplication.translate("TelaCombate", u"Pontos de Vida:", None))
        self.label_3.setText(QCoreApplication.translate("TelaCombate", u"Dano / Cura:", None))
        self.label_4.setText(QCoreApplication.translate("TelaCombate", u"Ponto Her\u00f3ico:", None))
        self.label_5.setText(QCoreApplication.translate("TelaCombate", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome Personagem:</span></p></body></html>", None))
        self.btn_carregar.setText(QCoreApplication.translate("TelaCombate", u"Carregar", None))
        self.btn_dano.setText(QCoreApplication.translate("TelaCombate", u"Dano", None))
        self.btn_cura.setText(QCoreApplication.translate("TelaCombate", u"Cura", None))
        self.btn_limpar_campos_personagem.setText(QCoreApplication.translate("TelaCombate", u"Limpar Campos", None))
        self.btn_alterar_pontos_heroico.setText(QCoreApplication.translate("TelaCombate", u"Alterar Ponto Her\u00f3ico", None))
        self.label_6.setText("")
        self.label_7.setText("")
        self.combo_ponto_heroico.setItemText(0, QCoreApplication.translate("TelaCombate", u"Selecionar", None))
        self.combo_ponto_heroico.setItemText(1, QCoreApplication.translate("TelaCombate", u"1", None))
        self.combo_ponto_heroico.setItemText(2, QCoreApplication.translate("TelaCombate", u"2", None))
        self.combo_ponto_heroico.setItemText(3, QCoreApplication.translate("TelaCombate", u"3", None))
        self.combo_ponto_heroico.setItemText(4, QCoreApplication.translate("TelaCombate", u"4", None))
        self.combo_ponto_heroico.setItemText(5, QCoreApplication.translate("TelaCombate", u"5", None))
        self.combo_ponto_heroico.setItemText(6, QCoreApplication.translate("TelaCombate", u"6", None))
        self.combo_ponto_heroico.setItemText(7, QCoreApplication.translate("TelaCombate", u"7", None))
        self.combo_ponto_heroico.setItemText(8, QCoreApplication.translate("TelaCombate", u"8", None))
        self.combo_ponto_heroico.setItemText(9, QCoreApplication.translate("TelaCombate", u"9", None))
        self.combo_ponto_heroico.setItemText(10, QCoreApplication.translate("TelaCombate", u"10", None))

        self.tav_combate.setTabText(self.tav_combate.indexOf(self.tab_personagens), QCoreApplication.translate("TelaCombate", u"Personagens", None))
        self.btn_carregar_monstro.setText(QCoreApplication.translate("TelaCombate", u"Carregar", None))
        self.btn_cura_monstro.setText(QCoreApplication.translate("TelaCombate", u"Cura", None))
        self.label_8.setText(QCoreApplication.translate("TelaCombate", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome Monstro:</span></p></body></html>", None))
        self.btn_limpar_campos_monstro.setText(QCoreApplication.translate("TelaCombate", u"Limpar Campos", None))
        self.label_9.setText(QCoreApplication.translate("TelaCombate", u"Pontos de Vida:", None))
        ___qtablewidgetitem6 = self.tabela_monstro_batalha.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TelaCombate", u"ID", None));
        ___qtablewidgetitem7 = self.tabela_monstro_batalha.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TelaCombate", u"Nome", None));
        ___qtablewidgetitem8 = self.tabela_monstro_batalha.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TelaCombate", u"Classe de Armadura", None));
        ___qtablewidgetitem9 = self.tabela_monstro_batalha.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TelaCombate", u"P.V. Atual", None));
        ___qtablewidgetitem10 = self.tabela_monstro_batalha.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("TelaCombate", u"Deslocamento", None));
        ___qtablewidgetitem11 = self.tabela_monstro_batalha.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("TelaCombate", u"N\u00edvel Desafio", None));
        ___qtablewidgetitem12 = self.tabela_monstro_batalha.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("TelaCombate", u"Refer\u00eancia", None));
        ___qtablewidgetitem13 = self.tabela_monstro_batalha.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("TelaCombate", u"Situa\u00e7\u00e3o", None));
        self.btn_dano_monstro.setText(QCoreApplication.translate("TelaCombate", u"Dano", None))
        self.label_10.setText(QCoreApplication.translate("TelaCombate", u"Dano / Cura:", None))
        self.label_11.setText(QCoreApplication.translate("TelaCombate", u"ID:", None))
        self.btn_limpar_monstro_combate.setText(QCoreApplication.translate("TelaCombate", u"Limpar Monstros do Combate", None))
        self.label_12.setText("")
        self.tav_combate.setTabText(self.tav_combate.indexOf(self.tab_2), QCoreApplication.translate("TelaCombate", u"Monstro", None))
        ___qtablewidgetitem14 = self.tabela_inserir_monstro_combate.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("TelaCombate", u"ID", None));
        ___qtablewidgetitem15 = self.tabela_inserir_monstro_combate.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("TelaCombate", u"Nome", None));
        ___qtablewidgetitem16 = self.tabela_inserir_monstro_combate.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("TelaCombate", u"Classe de Armadura", None));
        ___qtablewidgetitem17 = self.tabela_inserir_monstro_combate.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("TelaCombate", u"P.V. Atual", None));
        ___qtablewidgetitem18 = self.tabela_inserir_monstro_combate.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("TelaCombate", u"Deslocamento", None));
        ___qtablewidgetitem19 = self.tabela_inserir_monstro_combate.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("TelaCombate", u"Refer\u00eancia", None));
        ___qtablewidgetitem20 = self.tabela_inserir_monstro_combate.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("TelaCombate", u"Situa\u00e7\u00e3o", None));
        self.btn_inserir_monstro_combate.setText(QCoreApplication.translate("TelaCombate", u"Inserir Monstro no Combate", None))
        self.groupBox.setTitle(QCoreApplication.translate("TelaCombate", u"Perquisar nome do Monstro", None))
        self.txt_pesquisar_monstro_nome.setPlaceholderText(QCoreApplication.translate("TelaCombate", u"Nome do Monstro", None))
        self.btn_pesquisar_monstro.setText(QCoreApplication.translate("TelaCombate", u"Pesquisar", None))
        self.label_13.setText("")
        self.label_14.setText("")
        self.tav_combate.setTabText(self.tav_combate.indexOf(self.tab), QCoreApplication.translate("TelaCombate", u"Adicionar monstro ao Combate", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("TelaCombate", u"Iniciativa do Personagem", None))
        self.label_15.setText(QCoreApplication.translate("TelaCombate", u"Personagem:", None))
        self.label_16.setText(QCoreApplication.translate("TelaCombate", u"Iniciativa:", None))
        self.combo_iniciatita_personagem.setItemText(0, QCoreApplication.translate("TelaCombate", u"Selecionar", None))

        self.btn_adicionar_personagem_iniciativa.setText(QCoreApplication.translate("TelaCombate", u"Adicionar", None))
        self.label_17.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("TelaCombate", u"Iniciativa do Monstro", None))
        self.label_18.setText(QCoreApplication.translate("TelaCombate", u"Monstro:", None))
        self.label_19.setText(QCoreApplication.translate("TelaCombate", u"Iniciativa:", None))
        self.combo_iniciatita_monstro.setItemText(0, QCoreApplication.translate("TelaCombate", u"Selecionar", None))

        self.btn_adicionar_monstro_iniciativa.setText(QCoreApplication.translate("TelaCombate", u"Adicionar", None))
        self.label_20.setText("")
        ___qtablewidgetitem21 = self.tabela_iniciativa.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("TelaCombate", u"Nome", None));
        ___qtablewidgetitem22 = self.tabela_iniciativa.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("TelaCombate", u"Valor Iniciativa", None));
        self.label_21.setText("")
        self.btn_limpar_tabela_iniciativa.setText(QCoreApplication.translate("TelaCombate", u"Limpar Lista de Iniciativa", None))
        self.tav_combate.setTabText(self.tav_combate.indexOf(self.tab_3), QCoreApplication.translate("TelaCombate", u"Iniciativa", None))
    # retranslateUi

