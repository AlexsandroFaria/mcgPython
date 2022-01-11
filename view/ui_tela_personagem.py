# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_personagem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaPersonagem(object):
    def setupUi(self, TelaPersonagem):
        if not TelaPersonagem.objectName():
            TelaPersonagem.setObjectName(u"TelaPersonagem")
        TelaPersonagem.resize(1089, 594)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        TelaPersonagem.setWindowIcon(icon)
        self.frame = QFrame(TelaPersonagem)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1091, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 1091, 111))
        self.label_12.setPixmap(QPixmap(u"_img/banner_personagem.png"))
        self.tab_personagem = QTabWidget(TelaPersonagem)
        self.tab_personagem.setObjectName(u"tab_personagem")
        self.tab_personagem.setGeometry(QRect(10, 130, 1061, 381))
        font = QFont()
        font.setFamily(u"Elephant")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tab_personagem.setFont(font)
        self.tab_personagem.setStyleSheet(u"color: rgb(10, 18, 170);\n"
"background-color: rgb(241, 241, 241);")
        self.tab_personagem.setIconSize(QSize(24, 24))
        self.tab_personagem.setElideMode(Qt.ElideLeft)
        self.tab_cadastro_personagem = QWidget()
        self.tab_cadastro_personagem.setObjectName(u"tab_cadastro_personagem")
        self.label = QLabel(self.tab_cadastro_personagem)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 59, 121, 31))
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.tab_cadastro_personagem)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 100, 71, 31))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.tab_cadastro_personagem)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 140, 71, 21))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.tab_cadastro_personagem)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 140, 61, 31))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.tab_cadastro_personagem)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 180, 131, 21))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.tab_cadastro_personagem)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(410, 180, 201, 31))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.tab_cadastro_personagem)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 220, 181, 21))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.tab_cadastro_personagem)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(410, 220, 201, 31))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.tab_cadastro_personagem)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 260, 181, 21))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_10 = QLabel(self.tab_cadastro_personagem)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(470, 260, 141, 31))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_id = QLineEdit(self.tab_cadastro_personagem)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setEnabled(False)
        self.txt_id.setGeometry(QRect(210, 60, 71, 25))
        self.txt_id.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.txt_id.setFont(font1)
        self.txt_id.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(241, 241, 241);")
        self.txt_nome_personagem = QLineEdit(self.tab_cadastro_personagem)
        self.txt_nome_personagem.setObjectName(u"txt_nome_personagem")
        self.txt_nome_personagem.setGeometry(QRect(210, 100, 491, 25))
        self.txt_nome_personagem.setMinimumSize(QSize(0, 25))
        self.txt_nome_personagem.setFont(font1)
        self.txt_nome_personagem.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.combo_classe = QComboBox(self.tab_cadastro_personagem)
        self.combo_classe.addItem("")
        self.combo_classe.setObjectName(u"combo_classe")
        self.combo_classe.setGeometry(QRect(210, 140, 200, 25))
        self.combo_classe.setMinimumSize(QSize(0, 25))
        self.combo_classe.setFont(font1)
        self.combo_classe.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.combo_raca = QComboBox(self.tab_cadastro_personagem)
        self.combo_raca.addItem("")
        self.combo_raca.setObjectName(u"combo_raca")
        self.combo_raca.setGeometry(QRect(500, 140, 200, 25))
        self.combo_raca.setMinimumSize(QSize(0, 25))
        self.combo_raca.setFont(font1)
        self.combo_raca.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.combo_dados_vida = QComboBox(self.tab_cadastro_personagem)
        self.combo_dados_vida.addItem("")
        self.combo_dados_vida.addItem("")
        self.combo_dados_vida.addItem("")
        self.combo_dados_vida.addItem("")
        self.combo_dados_vida.addItem("")
        self.combo_dados_vida.setObjectName(u"combo_dados_vida")
        self.combo_dados_vida.setGeometry(QRect(210, 180, 200, 25))
        self.combo_dados_vida.setMinimumSize(QSize(0, 25))
        self.combo_dados_vida.setFont(font1)
        self.combo_dados_vida.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_total_pontos_vida = QLineEdit(self.tab_cadastro_personagem)
        self.txt_total_pontos_vida.setObjectName(u"txt_total_pontos_vida")
        self.txt_total_pontos_vida.setGeometry(QRect(620, 180, 81, 25))
        self.txt_total_pontos_vida.setMinimumSize(QSize(0, 25))
        self.txt_total_pontos_vida.setFont(font1)
        self.txt_total_pontos_vida.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_pontos_experiencia = QLineEdit(self.tab_cadastro_personagem)
        self.txt_pontos_experiencia.setObjectName(u"txt_pontos_experiencia")
        self.txt_pontos_experiencia.setGeometry(QRect(620, 220, 81, 25))
        self.txt_pontos_experiencia.setMinimumSize(QSize(0, 25))
        self.txt_pontos_experiencia.setFont(font1)
        self.txt_pontos_experiencia.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_pontos_vida_atual = QLineEdit(self.tab_cadastro_personagem)
        self.txt_pontos_vida_atual.setObjectName(u"txt_pontos_vida_atual")
        self.txt_pontos_vida_atual.setGeometry(QRect(210, 220, 91, 25))
        self.txt_pontos_vida_atual.setMinimumSize(QSize(0, 25))
        self.txt_pontos_vida_atual.setFont(font1)
        self.txt_pontos_vida_atual.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.combo_nivel_personagem = QComboBox(self.tab_cadastro_personagem)
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.addItem("")
        self.combo_nivel_personagem.setObjectName(u"combo_nivel_personagem")
        self.combo_nivel_personagem.setGeometry(QRect(210, 260, 91, 25))
        self.combo_nivel_personagem.setFont(font1)
        self.combo_nivel_personagem.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_pontos_heroicos = QLineEdit(self.tab_cadastro_personagem)
        self.txt_pontos_heroicos.setObjectName(u"txt_pontos_heroicos")
        self.txt_pontos_heroicos.setGeometry(QRect(620, 260, 81, 25))
        self.txt_pontos_heroicos.setMinimumSize(QSize(0, 25))
        self.txt_pontos_heroicos.setFont(font1)
        self.txt_pontos_heroicos.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.groupBox = QGroupBox(self.tab_cadastro_personagem)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(310, 39, 391, 51))
        font2 = QFont()
        font2.setFamily(u"Elephant")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        self.groupBox.setFont(font2)
        self.groupBox.setMouseTracking(False)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid rgb(141, 141, 141);\n"
"color: rgb(0, 0, 255);")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.combo_selecionar_personagem = QComboBox(self.groupBox)
        self.combo_selecionar_personagem.addItem("")
        self.combo_selecionar_personagem.setObjectName(u"combo_selecionar_personagem")
        self.combo_selecionar_personagem.setGeometry(QRect(30, 20, 351, 22))
        self.combo_selecionar_personagem.setFont(font1)
        self.combo_selecionar_personagem.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_18 = QLabel(self.tab_cadastro_personagem)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(790, 40, 211, 271))
        self.label_18.setPixmap(QPixmap(u"_img/anao.png"))
        icon1 = QIcon()
        icon1.addFile(u"_img/personagem.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_personagem.addTab(self.tab_cadastro_personagem, icon1, "")
        self.tab_consulta_personagem = QWidget()
        self.tab_consulta_personagem.setObjectName(u"tab_consulta_personagem")
        self.tabela_personagem = QTableWidget(self.tab_consulta_personagem)
        if (self.tabela_personagem.columnCount() < 10):
            self.tabela_personagem.setColumnCount(10)
        font3 = QFont()
        font3.setFamily(u"Elephant")
        font3.setBold(False)
        font3.setWeight(50)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tabela_personagem.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font4 = QFont()
        font4.setFamily(u"Elephant")
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tabela_personagem.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tabela_personagem.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tabela_personagem.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tabela_personagem.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self.tabela_personagem.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.tabela_personagem.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.tabela_personagem.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        self.tabela_personagem.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        self.tabela_personagem.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tabela_personagem.setObjectName(u"tabela_personagem")
        self.tabela_personagem.setGeometry(QRect(10, 40, 1031, 241))
        self.frame_3 = QFrame(self.tab_consulta_personagem)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 290, 1031, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_2.addWidget(self.label_15)

        self.btn_carregar = QPushButton(self.frame_3)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setMinimumSize(QSize(0, 30))
        font5 = QFont()
        font5.setFamily(u"Elephant")
        font5.setPointSize(12)
        self.btn_carregar.setFont(font5)
        self.btn_carregar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(26, 5, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(24, 8, 255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_carregar)

        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_2.addWidget(self.label_16)

        icon2 = QIcon()
        icon2.addFile(u"_img/consultar_personagem.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_personagem.addTab(self.tab_consulta_personagem, icon2, "")
        self.frame_2 = QFrame(TelaPersonagem)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(18, 520, 1051, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout.addWidget(self.label_13)

        self.btn_limpar_tela = QPushButton(self.frame_2)
        self.btn_limpar_tela.setObjectName(u"btn_limpar_tela")
        self.btn_limpar_tela.setMinimumSize(QSize(0, 30))
        self.btn_limpar_tela.setFont(font5)
        self.btn_limpar_tela.setStyleSheet(u"QPushButton{\n"
"	\n"
"	color: rgb(26, 5, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(24, 8, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"_img/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon3)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_limpar_tela)

        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font5)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(26, 5, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(24, 8, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"_img/cadastrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon4)
        self.btn_cadastrar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_cadastrar)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(0, 30))
        self.btn_alterar.setFont(font5)
        self.btn_alterar.setStyleSheet(u"QPushButton{\n"
"	color: rgb(26, 5, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(24, 8, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"_img/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon5)
        self.btn_alterar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 30))
        self.btn_excluir.setFont(font5)
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"	color: rgb(26, 5, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(24, 8, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"_img/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon6)
        self.btn_excluir.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_excluir)

        self.btn_sair = QPushButton(self.frame_2)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setMinimumSize(QSize(0, 30))
        self.btn_sair.setFont(font5)
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
"	color: rgb(26, 5, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(24, 8, 255);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair.setIcon(icon7)
        self.btn_sair.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_sair)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout.addWidget(self.label_14)

        QWidget.setTabOrder(self.txt_id, self.txt_nome_personagem)
        QWidget.setTabOrder(self.txt_nome_personagem, self.combo_classe)
        QWidget.setTabOrder(self.combo_classe, self.combo_raca)
        QWidget.setTabOrder(self.combo_raca, self.combo_dados_vida)
        QWidget.setTabOrder(self.combo_dados_vida, self.txt_total_pontos_vida)
        QWidget.setTabOrder(self.txt_total_pontos_vida, self.txt_pontos_vida_atual)
        QWidget.setTabOrder(self.txt_pontos_vida_atual, self.txt_pontos_experiencia)
        QWidget.setTabOrder(self.txt_pontos_experiencia, self.combo_nivel_personagem)
        QWidget.setTabOrder(self.combo_nivel_personagem, self.txt_pontos_heroicos)
        QWidget.setTabOrder(self.txt_pontos_heroicos, self.btn_limpar_tela)
        QWidget.setTabOrder(self.btn_limpar_tela, self.btn_cadastrar)
        QWidget.setTabOrder(self.btn_cadastrar, self.btn_alterar)
        QWidget.setTabOrder(self.btn_alterar, self.btn_excluir)
        QWidget.setTabOrder(self.btn_excluir, self.btn_sair)
        QWidget.setTabOrder(self.btn_sair, self.combo_selecionar_personagem)
        QWidget.setTabOrder(self.combo_selecionar_personagem, self.tabela_personagem)
        QWidget.setTabOrder(self.tabela_personagem, self.btn_carregar)
        QWidget.setTabOrder(self.btn_carregar, self.tab_personagem)

        self.retranslateUi(TelaPersonagem)

        self.tab_personagem.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TelaPersonagem)
    # setupUi

    def retranslateUi(self, TelaPersonagem):
        TelaPersonagem.setWindowTitle(QCoreApplication.translate("TelaPersonagem", u"Form", None))
        self.label_12.setText("")
#if QT_CONFIG(tooltip)
        self.tab_cadastro_personagem.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("TelaPersonagem", u"Identificador:", None))
        self.label_2.setText(QCoreApplication.translate("TelaPersonagem", u"Nome:", None))
        self.label_3.setText(QCoreApplication.translate("TelaPersonagem", u"Classe:", None))
        self.label_4.setText(QCoreApplication.translate("TelaPersonagem", u"Ra\u00e7a:", None))
        self.label_5.setText(QCoreApplication.translate("TelaPersonagem", u"Dados de Vida:", None))
        self.label_6.setText(QCoreApplication.translate("TelaPersonagem", u"Total de Pontos de Vida:", None))
        self.label_7.setText(QCoreApplication.translate("TelaPersonagem", u"Pontos de Vida Atual:", None))
        self.label_8.setText(QCoreApplication.translate("TelaPersonagem", u"Pontos de Experi\u00eancia:", None))
        self.label_9.setText(QCoreApplication.translate("TelaPersonagem", u"Nivel de Personagem:", None))
        self.label_10.setText(QCoreApplication.translate("TelaPersonagem", u"Pontos her\u00f3icos:", None))
        self.combo_classe.setItemText(0, QCoreApplication.translate("TelaPersonagem", u"Selecione uma op\u00e7\u00e3o", None))

        self.combo_raca.setItemText(0, QCoreApplication.translate("TelaPersonagem", u"Selecione uma op\u00e7\u00e3o", None))

        self.combo_dados_vida.setItemText(0, QCoreApplication.translate("TelaPersonagem", u"Selecione uma op\u00e7\u00e3o", None))
        self.combo_dados_vida.setItemText(1, QCoreApplication.translate("TelaPersonagem", u"1 D 6", None))
        self.combo_dados_vida.setItemText(2, QCoreApplication.translate("TelaPersonagem", u"1 D 8", None))
        self.combo_dados_vida.setItemText(3, QCoreApplication.translate("TelaPersonagem", u"1 D 10", None))
        self.combo_dados_vida.setItemText(4, QCoreApplication.translate("TelaPersonagem", u"1 D 12", None))

        self.combo_nivel_personagem.setItemText(0, QCoreApplication.translate("TelaPersonagem", u"Selecionar", None))
        self.combo_nivel_personagem.setItemText(1, QCoreApplication.translate("TelaPersonagem", u"1", None))
        self.combo_nivel_personagem.setItemText(2, QCoreApplication.translate("TelaPersonagem", u"2", None))
        self.combo_nivel_personagem.setItemText(3, QCoreApplication.translate("TelaPersonagem", u"3", None))
        self.combo_nivel_personagem.setItemText(4, QCoreApplication.translate("TelaPersonagem", u"4", None))
        self.combo_nivel_personagem.setItemText(5, QCoreApplication.translate("TelaPersonagem", u"5", None))
        self.combo_nivel_personagem.setItemText(6, QCoreApplication.translate("TelaPersonagem", u"6", None))
        self.combo_nivel_personagem.setItemText(7, QCoreApplication.translate("TelaPersonagem", u"7", None))
        self.combo_nivel_personagem.setItemText(8, QCoreApplication.translate("TelaPersonagem", u"8", None))
        self.combo_nivel_personagem.setItemText(9, QCoreApplication.translate("TelaPersonagem", u"9", None))
        self.combo_nivel_personagem.setItemText(10, QCoreApplication.translate("TelaPersonagem", u"10", None))
        self.combo_nivel_personagem.setItemText(11, QCoreApplication.translate("TelaPersonagem", u"11", None))
        self.combo_nivel_personagem.setItemText(12, QCoreApplication.translate("TelaPersonagem", u"12", None))
        self.combo_nivel_personagem.setItemText(13, QCoreApplication.translate("TelaPersonagem", u"13", None))
        self.combo_nivel_personagem.setItemText(14, QCoreApplication.translate("TelaPersonagem", u"14", None))
        self.combo_nivel_personagem.setItemText(15, QCoreApplication.translate("TelaPersonagem", u"15", None))
        self.combo_nivel_personagem.setItemText(16, QCoreApplication.translate("TelaPersonagem", u"16", None))
        self.combo_nivel_personagem.setItemText(17, QCoreApplication.translate("TelaPersonagem", u"17", None))
        self.combo_nivel_personagem.setItemText(18, QCoreApplication.translate("TelaPersonagem", u"18", None))
        self.combo_nivel_personagem.setItemText(19, QCoreApplication.translate("TelaPersonagem", u"19", None))
        self.combo_nivel_personagem.setItemText(20, QCoreApplication.translate("TelaPersonagem", u"20", None))

        self.groupBox.setTitle(QCoreApplication.translate("TelaPersonagem", u"Selecionar Personagem", None))
        self.combo_selecionar_personagem.setItemText(0, QCoreApplication.translate("TelaPersonagem", u"Selecione uma op\u00e7\u00e3o", None))

#if QT_CONFIG(tooltip)
        self.combo_selecionar_personagem.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_18.setText("")
        self.tab_personagem.setTabText(self.tab_personagem.indexOf(self.tab_cadastro_personagem), QCoreApplication.translate("TelaPersonagem", u"Personagem", None))
        ___qtablewidgetitem = self.tabela_personagem.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaPersonagem", u"Identificador", None));
        ___qtablewidgetitem1 = self.tabela_personagem.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaPersonagem", u"Nome", None));
        ___qtablewidgetitem2 = self.tabela_personagem.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaPersonagem", u"Classe", None));
        ___qtablewidgetitem3 = self.tabela_personagem.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TelaPersonagem", u"Ra\u00e7a", None));
        ___qtablewidgetitem4 = self.tabela_personagem.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TelaPersonagem", u"Dados de vida", None));
        ___qtablewidgetitem5 = self.tabela_personagem.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TelaPersonagem", u"PV Total", None));
        ___qtablewidgetitem6 = self.tabela_personagem.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TelaPersonagem", u"PV Atual", None));
        ___qtablewidgetitem7 = self.tabela_personagem.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TelaPersonagem", u"Experi\u00eancia", None));
        ___qtablewidgetitem8 = self.tabela_personagem.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TelaPersonagem", u"N\u00edvel", None));
        ___qtablewidgetitem9 = self.tabela_personagem.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("TelaPersonagem", u"Ponto Her\u00f3ico", None));
        self.label_15.setText("")
        self.btn_carregar.setText(QCoreApplication.translate("TelaPersonagem", u"Carregar", None))
        self.label_16.setText("")
        self.tab_personagem.setTabText(self.tab_personagem.indexOf(self.tab_consulta_personagem), QCoreApplication.translate("TelaPersonagem", u"Consulta de Personagem", None))
        self.label_13.setText("")
        self.btn_limpar_tela.setText(QCoreApplication.translate("TelaPersonagem", u"Limpar Tela", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("TelaPersonagem", u"Cadastrar", None))
        self.btn_alterar.setText(QCoreApplication.translate("TelaPersonagem", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("TelaPersonagem", u"Excluir", None))
        self.btn_sair.setText(QCoreApplication.translate("TelaPersonagem", u"Sair", None))
        self.label_14.setText("")
    # retranslateUi

