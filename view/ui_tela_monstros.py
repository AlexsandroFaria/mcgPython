# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_monstros.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaMonstros(object):
    def setupUi(self, TelaMonstros):
        if not TelaMonstros.objectName():
            TelaMonstros.setObjectName(u"TelaMonstros")
        TelaMonstros.resize(1061, 600)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        TelaMonstros.setWindowIcon(icon)
        self.menu_reconstrui_lista_monstros = QAction(TelaMonstros)
        self.menu_reconstrui_lista_monstros.setObjectName(u"menu_reconstrui_lista_monstros")
        icon1 = QIcon()
        icon1.addFile(u"_img/dragon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_reconstrui_lista_monstros.setIcon(icon1)
        self.centralwidget = QWidget(TelaMonstros)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1061, 141))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1061, 141))
        self.label.setPixmap(QPixmap(u"_img/banner_monstros.png"))
        self.tab_monstros = QTabWidget(self.centralwidget)
        self.tab_monstros.setObjectName(u"tab_monstros")
        self.tab_monstros.setGeometry(QRect(10, 140, 1041, 361))
        font = QFont()
        font.setFamily(u"Elephant")
        font.setPointSize(12)
        self.tab_monstros.setFont(font)
        self.tab_monstros.setStyleSheet(u"background-color: rgb(241, 241, 241);")
        self.tab_monstros.setIconSize(QSize(24, 24))
        self.tab_cadastro_monstros = QWidget()
        self.tab_cadastro_monstros.setObjectName(u"tab_cadastro_monstros")
        self.label_4 = QLabel(self.tab_cadastro_monstros)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 50, 121, 21))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.tab_cadastro_monstros)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 90, 171, 20))
        font1 = QFont()
        font1.setFamily(u"Elephant")
        font1.setPointSize(8)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.tab_cadastro_monstros)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 130, 151, 21))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.tab_cadastro_monstros)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(460, 130, 171, 21))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.tab_cadastro_monstros)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 170, 131, 21))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_9 = QLabel(self.tab_cadastro_monstros)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(450, 170, 181, 21))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_10 = QLabel(self.tab_cadastro_monstros)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 210, 131, 16))
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_11 = QLabel(self.tab_cadastro_monstros)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(490, 210, 141, 21))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_12 = QLabel(self.tab_cadastro_monstros)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(60, 250, 111, 21))
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_id = QLineEdit(self.tab_cadastro_monstros)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setEnabled(False)
        self.txt_id.setGeometry(QRect(190, 50, 101, 25))
        self.txt_id.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(12)
        self.txt_id.setFont(font2)
        self.txt_id.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(241, 241, 241);\n"
"")
        self.txt_nome_monstros = QLineEdit(self.tab_cadastro_monstros)
        self.txt_nome_monstros.setObjectName(u"txt_nome_monstros")
        self.txt_nome_monstros.setGeometry(QRect(190, 90, 581, 25))
        self.txt_nome_monstros.setMinimumSize(QSize(0, 25))
        self.txt_nome_monstros.setFont(font2)
        self.txt_nome_monstros.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.combo_tipo_monstro = QComboBox(self.tab_cadastro_monstros)
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.addItem("")
        self.combo_tipo_monstro.setObjectName(u"combo_tipo_monstro")
        self.combo_tipo_monstro.setGeometry(QRect(190, 130, 271, 25))
        self.combo_tipo_monstro.setMinimumSize(QSize(0, 25))
        self.combo_tipo_monstro.setFont(font2)
        self.txt_classe_armadura = QLineEdit(self.tab_cadastro_monstros)
        self.txt_classe_armadura.setObjectName(u"txt_classe_armadura")
        self.txt_classe_armadura.setGeometry(QRect(640, 130, 131, 25))
        self.txt_classe_armadura.setMinimumSize(QSize(0, 25))
        self.txt_classe_armadura.setFont(font2)
        self.txt_classe_armadura.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_pontos_vida = QLineEdit(self.tab_cadastro_monstros)
        self.txt_pontos_vida.setObjectName(u"txt_pontos_vida")
        self.txt_pontos_vida.setGeometry(QRect(190, 170, 141, 25))
        self.txt_pontos_vida.setMinimumSize(QSize(0, 25))
        self.txt_pontos_vida.setFont(font2)
        self.txt_pontos_vida.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_pontos_vida_atual = QLineEdit(self.tab_cadastro_monstros)
        self.txt_pontos_vida_atual.setObjectName(u"txt_pontos_vida_atual")
        self.txt_pontos_vida_atual.setGeometry(QRect(640, 170, 131, 25))
        self.txt_pontos_vida_atual.setMinimumSize(QSize(0, 25))
        self.txt_pontos_vida_atual.setFont(font2)
        self.txt_pontos_vida_atual.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_deslocamento = QLineEdit(self.tab_cadastro_monstros)
        self.txt_deslocamento.setObjectName(u"txt_deslocamento")
        self.txt_deslocamento.setGeometry(QRect(190, 210, 141, 25))
        self.txt_deslocamento.setMinimumSize(QSize(0, 25))
        self.txt_deslocamento.setFont(font2)
        self.txt_deslocamento.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_referencia = QLineEdit(self.tab_cadastro_monstros)
        self.txt_referencia.setObjectName(u"txt_referencia")
        self.txt_referencia.setGeometry(QRect(190, 250, 581, 25))
        self.txt_referencia.setMinimumSize(QSize(0, 25))
        self.txt_referencia.setFont(font2)
        self.txt_referencia.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_nivel_desafio = QLineEdit(self.tab_cadastro_monstros)
        self.txt_nivel_desafio.setObjectName(u"txt_nivel_desafio")
        self.txt_nivel_desafio.setGeometry(QRect(640, 210, 131, 25))
        self.txt_nivel_desafio.setMinimumSize(QSize(0, 25))
        self.txt_nivel_desafio.setFont(font2)
        self.txt_nivel_desafio.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.label_17 = QLabel(self.tab_cadastro_monstros)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(800, 40, 181, 241))
        self.label_17.setPixmap(QPixmap(u"_img/globin.png"))
        icon2 = QIcon()
        icon2.addFile(u"_img/monstros.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_monstros.addTab(self.tab_cadastro_monstros, icon2, "")
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.txt_id.raise_()
        self.txt_nome_monstros.raise_()
        self.combo_tipo_monstro.raise_()
        self.txt_classe_armadura.raise_()
        self.txt_pontos_vida.raise_()
        self.txt_pontos_vida_atual.raise_()
        self.txt_deslocamento.raise_()
        self.txt_referencia.raise_()
        self.txt_nivel_desafio.raise_()
        self.label_17.raise_()
        self.label_4.raise_()
        self.tab_consulta_monstros = QWidget()
        self.tab_consulta_monstros.setObjectName(u"tab_consulta_monstros")
        self.tabela_Monstros = QTableWidget(self.tab_consulta_monstros)
        if (self.tabela_Monstros.columnCount() < 9):
            self.tabela_Monstros.setColumnCount(9)
        font3 = QFont()
        font3.setFamily(u"Elephant")
        font3.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tabela_Monstros.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.tabela_Monstros.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.tabela_Monstros.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.tabela_Monstros.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.tabela_Monstros.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.tabela_Monstros.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.tabela_Monstros.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.tabela_Monstros.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self.tabela_Monstros.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tabela_Monstros.setObjectName(u"tabela_Monstros")
        self.tabela_Monstros.setGeometry(QRect(20, 50, 1001, 221))
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        self.tabela_Monstros.setFont(font4)
        self.tabela_Monstros.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tabela_Monstros.setAlternatingRowColors(True)
        self.tabela_Monstros.verticalHeader().setVisible(False)
        self.tabela_Monstros.verticalHeader().setHighlightSections(True)
        self.frame_3 = QFrame(self.tab_consulta_monstros)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 270, 1001, 49))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_15 = QLabel(self.frame_3)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_2.addWidget(self.label_15)

        self.btn_carregar = QPushButton(self.frame_3)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setMinimumSize(QSize(0, 35))
        self.btn_carregar.setFont(font)
        self.btn_carregar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(76, 0, 227);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon3)
        self.btn_carregar.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_carregar)

        self.label_16 = QLabel(self.frame_3)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_2.addWidget(self.label_16)

        self.label_18 = QLabel(self.tab_consulta_monstros)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(30, 13, 161, 20))
        self.txt_pesquisar_monstro = QLineEdit(self.tab_consulta_monstros)
        self.txt_pesquisar_monstro.setObjectName(u"txt_pesquisar_monstro")
        self.txt_pesquisar_monstro.setGeometry(QRect(210, 10, 291, 25))
        self.txt_pesquisar_monstro.setMinimumSize(QSize(0, 25))
        self.txt_pesquisar_monstro.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.btn_pesquisar_monstros = QPushButton(self.tab_consulta_monstros)
        self.btn_pesquisar_monstros.setObjectName(u"btn_pesquisar_monstros")
        self.btn_pesquisar_monstros.setGeometry(QRect(520, 10, 131, 30))
        self.btn_pesquisar_monstros.setMinimumSize(QSize(0, 30))
        self.btn_pesquisar_monstros.setFont(font)
        self.btn_pesquisar_monstros.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(76, 0, 227);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"_img/pesquisar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar_monstros.setIcon(icon4)
        self.btn_pesquisar_monstros.setIconSize(QSize(24, 24))
        icon5 = QIcon()
        icon5.addFile(u"_img/consulta_monstros.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_monstros.addTab(self.tab_consulta_monstros, icon5, "")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 510, 1041, 52))
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
        self.btn_limpar_tela.setFont(font)
        self.btn_limpar_tela.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(76, 0, 227);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"_img/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon6)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_limpar_tela)

        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(76, 0, 227);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"_img/cadastrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon7)
        self.btn_cadastrar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_cadastrar)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(0, 30))
        self.btn_alterar.setFont(font)
        self.btn_alterar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(76, 0, 227);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"_img/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon8)
        self.btn_alterar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 30))
        self.btn_excluir.setFont(font)
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(76, 0, 227);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"_img/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon9)
        self.btn_excluir.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_excluir)

        self.btn_sair = QPushButton(self.frame_2)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setMinimumSize(QSize(0, 30))
        self.btn_sair.setFont(font)
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(170, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(76, 0, 227);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair.setIcon(icon10)
        self.btn_sair.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_sair)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout.addWidget(self.label_14)

        TelaMonstros.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TelaMonstros)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1061, 21))
        self.menuRepositorio_Monstros = QMenu(self.menubar)
        self.menuRepositorio_Monstros.setObjectName(u"menuRepositorio_Monstros")
        TelaMonstros.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(TelaMonstros)
        self.statusbar.setObjectName(u"statusbar")
        TelaMonstros.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.txt_id, self.txt_nome_monstros)
        QWidget.setTabOrder(self.txt_nome_monstros, self.combo_tipo_monstro)
        QWidget.setTabOrder(self.combo_tipo_monstro, self.txt_classe_armadura)
        QWidget.setTabOrder(self.txt_classe_armadura, self.txt_pontos_vida)
        QWidget.setTabOrder(self.txt_pontos_vida, self.txt_pontos_vida_atual)
        QWidget.setTabOrder(self.txt_pontos_vida_atual, self.txt_deslocamento)
        QWidget.setTabOrder(self.txt_deslocamento, self.txt_nivel_desafio)
        QWidget.setTabOrder(self.txt_nivel_desafio, self.txt_referencia)
        QWidget.setTabOrder(self.txt_referencia, self.tab_monstros)
        QWidget.setTabOrder(self.tab_monstros, self.tabela_Monstros)
        QWidget.setTabOrder(self.tabela_Monstros, self.btn_carregar)
        QWidget.setTabOrder(self.btn_carregar, self.txt_pesquisar_monstro)
        QWidget.setTabOrder(self.txt_pesquisar_monstro, self.btn_pesquisar_monstros)
        QWidget.setTabOrder(self.btn_pesquisar_monstros, self.btn_limpar_tela)
        QWidget.setTabOrder(self.btn_limpar_tela, self.btn_cadastrar)
        QWidget.setTabOrder(self.btn_cadastrar, self.btn_alterar)
        QWidget.setTabOrder(self.btn_alterar, self.btn_excluir)
        QWidget.setTabOrder(self.btn_excluir, self.btn_sair)

        self.menubar.addAction(self.menuRepositorio_Monstros.menuAction())
        self.menuRepositorio_Monstros.addAction(self.menu_reconstrui_lista_monstros)

        self.retranslateUi(TelaMonstros)

        self.tab_monstros.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TelaMonstros)
    # setupUi

    def retranslateUi(self, TelaMonstros):
        TelaMonstros.setWindowTitle(QCoreApplication.translate("TelaMonstros", u"MainWindow", None))
        self.menu_reconstrui_lista_monstros.setText(QCoreApplication.translate("TelaMonstros", u"Reorganizar lista de Monstros", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("TelaMonstros", u"<html><head/><body><p><span style=\" color:#5d5d5d;\">Identificador:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("TelaMonstros", u"<html><head/><body><p><span style=\" font-size:12pt; color:#5d5d5d;\">Nome do Monstro:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("TelaMonstros", u"<html><head/><body><p><span style=\" font-size:12pt; color:#5d5d5d;\">Tipo de Monstro:</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("TelaMonstros", u"<html><head/><body><p><span style=\" color:#5d5d5d;\">Classe de Armadura:</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("TelaMonstros", u"<html><head/><body><p><span style=\" font-size:12pt; color:#5d5d5d;\">Pontos de Vida:</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("TelaMonstros", u"<html><head/><body><p><span style=\" color:#5d5d5d;\">Pontos de Vida Atual:</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("TelaMonstros", u"<html><head/><body><p><span style=\" font-size:12pt; color:#5d5d5d;\">Deslocamento:</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("TelaMonstros", u"<html><head/><body><p><span style=\" color:#5d5d5d;\">N\u00edvel de desafio:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("TelaMonstros", u"<html><head/><body><p><span style=\" font-size:12pt; color:#5d5d5d;\">Refer\u00eancia:</span></p></body></html>", None))
        self.combo_tipo_monstro.setItemText(0, QCoreApplication.translate("TelaMonstros", u"Selecionar", None))
        self.combo_tipo_monstro.setItemText(1, QCoreApplication.translate("TelaMonstros", u"Aberra\u00e7\u00e3o Mi\u00fada", None))
        self.combo_tipo_monstro.setItemText(2, QCoreApplication.translate("TelaMonstros", u"Aberra\u00e7\u00e3o Pequena", None))
        self.combo_tipo_monstro.setItemText(3, QCoreApplication.translate("TelaMonstros", u"Aberra\u00e7\u00e3o M\u00e9dia", None))
        self.combo_tipo_monstro.setItemText(4, QCoreApplication.translate("TelaMonstros", u"Aberra\u00e7\u00e3o Grande", None))
        self.combo_tipo_monstro.setItemText(5, QCoreApplication.translate("TelaMonstros", u"Aberra\u00e7\u00e3o Enorme", None))
        self.combo_tipo_monstro.setItemText(6, QCoreApplication.translate("TelaMonstros", u"Aberra\u00e7\u00e3o Imensa", None))
        self.combo_tipo_monstro.setItemText(7, QCoreApplication.translate("TelaMonstros", u"Besta Mi\u00fada", None))
        self.combo_tipo_monstro.setItemText(8, QCoreApplication.translate("TelaMonstros", u"Besta M\u00e9dia", None))
        self.combo_tipo_monstro.setItemText(9, QCoreApplication.translate("TelaMonstros", u"Besta Grande", None))
        self.combo_tipo_monstro.setItemText(10, QCoreApplication.translate("TelaMonstros", u"Besta Enorme", None))
        self.combo_tipo_monstro.setItemText(11, QCoreApplication.translate("TelaMonstros", u"Besta Imensa", None))
        self.combo_tipo_monstro.setItemText(12, QCoreApplication.translate("TelaMonstros", u"Celestial Pequeno", None))
        self.combo_tipo_monstro.setItemText(13, QCoreApplication.translate("TelaMonstros", u"Celestial M\u00e9dio", None))
        self.combo_tipo_monstro.setItemText(14, QCoreApplication.translate("TelaMonstros", u"Celestial Grande", None))
        self.combo_tipo_monstro.setItemText(15, QCoreApplication.translate("TelaMonstros", u"Celestial Enorme", None))
        self.combo_tipo_monstro.setItemText(16, QCoreApplication.translate("TelaMonstros", u"Celestial Imenso", None))
        self.combo_tipo_monstro.setItemText(17, QCoreApplication.translate("TelaMonstros", u"Constructo Mi\u00fado", None))
        self.combo_tipo_monstro.setItemText(18, QCoreApplication.translate("TelaMonstros", u"Constructo Pequeno", None))
        self.combo_tipo_monstro.setItemText(19, QCoreApplication.translate("TelaMonstros", u"Constructo M\u00e9dio", None))
        self.combo_tipo_monstro.setItemText(20, QCoreApplication.translate("TelaMonstros", u"Constructo Grande", None))
        self.combo_tipo_monstro.setItemText(21, QCoreApplication.translate("TelaMonstros", u"Constructo Enorme", None))
        self.combo_tipo_monstro.setItemText(22, QCoreApplication.translate("TelaMonstros", u"Constructo Imenso", None))
        self.combo_tipo_monstro.setItemText(23, QCoreApplication.translate("TelaMonstros", u"Corruptor Mi\u00fado", None))
        self.combo_tipo_monstro.setItemText(24, QCoreApplication.translate("TelaMonstros", u"Corruptor Pequeno", None))
        self.combo_tipo_monstro.setItemText(25, QCoreApplication.translate("TelaMonstros", u"Corruptor M\u00e9dio", None))
        self.combo_tipo_monstro.setItemText(26, QCoreApplication.translate("TelaMonstros", u"Corruptor Grande", None))
        self.combo_tipo_monstro.setItemText(27, QCoreApplication.translate("TelaMonstros", u"Corruptor Enorme", None))
        self.combo_tipo_monstro.setItemText(28, QCoreApplication.translate("TelaMonstros", u"Corruptor Imenso", None))
        self.combo_tipo_monstro.setItemText(29, QCoreApplication.translate("TelaMonstros", u"Drag\u00e3o Mi\u00fado", None))
        self.combo_tipo_monstro.setItemText(30, QCoreApplication.translate("TelaMonstros", u"Drag\u00e3o M\u00e9dio", None))
        self.combo_tipo_monstro.setItemText(31, QCoreApplication.translate("TelaMonstros", u"Drag\u00e3o Grande", None))
        self.combo_tipo_monstro.setItemText(32, QCoreApplication.translate("TelaMonstros", u"Drag\u00e3o Enorme", None))
        self.combo_tipo_monstro.setItemText(33, QCoreApplication.translate("TelaMonstros", u"Drag\u00e3o Imenso", None))
        self.combo_tipo_monstro.setItemText(34, QCoreApplication.translate("TelaMonstros", u"Elemental Mi\u00fado", None))
        self.combo_tipo_monstro.setItemText(35, QCoreApplication.translate("TelaMonstros", u"Elemental Pequeno", None))
        self.combo_tipo_monstro.setItemText(36, QCoreApplication.translate("TelaMonstros", u"Elemental M\u00e9dio", None))
        self.combo_tipo_monstro.setItemText(37, QCoreApplication.translate("TelaMonstros", u"Elemental Grande", None))
        self.combo_tipo_monstro.setItemText(38, QCoreApplication.translate("TelaMonstros", u"Elemental Enorme", None))
        self.combo_tipo_monstro.setItemText(39, QCoreApplication.translate("TelaMonstros", u"Elemental Imenso", None))
        self.combo_tipo_monstro.setItemText(40, QCoreApplication.translate("TelaMonstros", u"Enxame M\u00e9dio de bestas Mi\u00fadas", None))
        self.combo_tipo_monstro.setItemText(41, QCoreApplication.translate("TelaMonstros", u"Fada Mi\u00fada", None))
        self.combo_tipo_monstro.setItemText(42, QCoreApplication.translate("TelaMonstros", u"Fada Pequena", None))
        self.combo_tipo_monstro.setItemText(43, QCoreApplication.translate("TelaMonstros", u"Fada M\u00e9dia", None))
        self.combo_tipo_monstro.setItemText(44, QCoreApplication.translate("TelaMonstros", u"Fada Grande", None))
        self.combo_tipo_monstro.setItemText(45, QCoreApplication.translate("TelaMonstros", u"Fada Enorme", None))
        self.combo_tipo_monstro.setItemText(46, QCoreApplication.translate("TelaMonstros", u"Fada Imensa", None))
        self.combo_tipo_monstro.setItemText(47, QCoreApplication.translate("TelaMonstros", u"Gigante Grande", None))
        self.combo_tipo_monstro.setItemText(48, QCoreApplication.translate("TelaMonstros", u"Gigante Enorme", None))
        self.combo_tipo_monstro.setItemText(49, QCoreApplication.translate("TelaMonstros", u"Gigante Imenso", None))
        self.combo_tipo_monstro.setItemText(50, QCoreApplication.translate("TelaMonstros", u"Humanoide Mi\u00fado", None))
        self.combo_tipo_monstro.setItemText(51, QCoreApplication.translate("TelaMonstros", u"Humanoide Pequeno", None))
        self.combo_tipo_monstro.setItemText(52, QCoreApplication.translate("TelaMonstros", u"Humanoide M\u00e9dio", None))
        self.combo_tipo_monstro.setItemText(53, QCoreApplication.translate("TelaMonstros", u"Humanoide Grande", None))
        self.combo_tipo_monstro.setItemText(54, QCoreApplication.translate("TelaMonstros", u"Limo Mi\u00fado", None))
        self.combo_tipo_monstro.setItemText(55, QCoreApplication.translate("TelaMonstros", u"Limo Pequeno", None))
        self.combo_tipo_monstro.setItemText(56, QCoreApplication.translate("TelaMonstros", u"Limo Grande", None))
        self.combo_tipo_monstro.setItemText(57, QCoreApplication.translate("TelaMonstros", u"Limo Enorme", None))
        self.combo_tipo_monstro.setItemText(58, QCoreApplication.translate("TelaMonstros", u"Limo Imenso", None))
        self.combo_tipo_monstro.setItemText(59, QCoreApplication.translate("TelaMonstros", u"Monstruosidade Mi\u00fada", None))
        self.combo_tipo_monstro.setItemText(60, QCoreApplication.translate("TelaMonstros", u"Monstruosidade Pequena", None))
        self.combo_tipo_monstro.setItemText(61, QCoreApplication.translate("TelaMonstros", u"Monstruosidade M\u00e9dia", None))
        self.combo_tipo_monstro.setItemText(62, QCoreApplication.translate("TelaMonstros", u"Monstruosidade Grande", None))
        self.combo_tipo_monstro.setItemText(63, QCoreApplication.translate("TelaMonstros", u"Monstruosidade Enorme", None))
        self.combo_tipo_monstro.setItemText(64, QCoreApplication.translate("TelaMonstros", u"Monstruosidade Imensa", None))
        self.combo_tipo_monstro.setItemText(65, QCoreApplication.translate("TelaMonstros", u"Morto-Vivo Mi\u00fado", None))
        self.combo_tipo_monstro.setItemText(66, QCoreApplication.translate("TelaMonstros", u"Morto_vivo Pequeno", None))
        self.combo_tipo_monstro.setItemText(67, QCoreApplication.translate("TelaMonstros", u"Morto-Vivo M\u00e9dio", None))
        self.combo_tipo_monstro.setItemText(68, QCoreApplication.translate("TelaMonstros", u"Morto-Vivo Grande", None))
        self.combo_tipo_monstro.setItemText(69, QCoreApplication.translate("TelaMonstros", u"Morto-Vivo Enorme", None))
        self.combo_tipo_monstro.setItemText(70, QCoreApplication.translate("TelaMonstros", u"Morto-Vivo Imenso", None))
        self.combo_tipo_monstro.setItemText(71, QCoreApplication.translate("TelaMonstros", u"Planta Mi\u00fada", None))
        self.combo_tipo_monstro.setItemText(72, QCoreApplication.translate("TelaMonstros", u"Planta Pequena", None))
        self.combo_tipo_monstro.setItemText(73, QCoreApplication.translate("TelaMonstros", u"Planta M\u00e9dia", None))
        self.combo_tipo_monstro.setItemText(74, QCoreApplication.translate("TelaMonstros", u"Planta Grande", None))
        self.combo_tipo_monstro.setItemText(75, QCoreApplication.translate("TelaMonstros", u"Planta Enorme", None))
        self.combo_tipo_monstro.setItemText(76, QCoreApplication.translate("TelaMonstros", u"Planta Imensa", None))

        self.label_17.setText("")
        self.tab_monstros.setTabText(self.tab_monstros.indexOf(self.tab_cadastro_monstros), QCoreApplication.translate("TelaMonstros", u"Monstros", None))
        ___qtablewidgetitem = self.tabela_Monstros.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaMonstros", u"ID", None));
        ___qtablewidgetitem1 = self.tabela_Monstros.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaMonstros", u"Nome", None));
        ___qtablewidgetitem2 = self.tabela_Monstros.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaMonstros", u"Tipo", None));
        ___qtablewidgetitem3 = self.tabela_Monstros.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TelaMonstros", u"Classe de Armadura", None));
        ___qtablewidgetitem4 = self.tabela_Monstros.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TelaMonstros", u"Pontos de Vida", None));
        ___qtablewidgetitem5 = self.tabela_Monstros.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TelaMonstros", u"Pontos de vida Atual", None));
        ___qtablewidgetitem6 = self.tabela_Monstros.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TelaMonstros", u"Deslocamento", None));
        ___qtablewidgetitem7 = self.tabela_Monstros.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("TelaMonstros", u"N\u00edvel de desafio", None));
        ___qtablewidgetitem8 = self.tabela_Monstros.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("TelaMonstros", u"Refer\u00eancia", None));
        self.label_15.setText("")
        self.btn_carregar.setText(QCoreApplication.translate("TelaMonstros", u"Carregar", None))
        self.label_16.setText("")
        self.label_18.setText(QCoreApplication.translate("TelaMonstros", u"Pesquisar Monstro:", None))
        self.btn_pesquisar_monstros.setText(QCoreApplication.translate("TelaMonstros", u"Pesquisar", None))
        self.tab_monstros.setTabText(self.tab_monstros.indexOf(self.tab_consulta_monstros), QCoreApplication.translate("TelaMonstros", u"Consulta Monstros", None))
        self.label_13.setText("")
        self.btn_limpar_tela.setText(QCoreApplication.translate("TelaMonstros", u"Limpar Tela", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("TelaMonstros", u"Cadastrar", None))
        self.btn_alterar.setText(QCoreApplication.translate("TelaMonstros", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("TelaMonstros", u"Excluir", None))
        self.btn_sair.setText(QCoreApplication.translate("TelaMonstros", u"Sair", None))
        self.label_14.setText("")
        self.menuRepositorio_Monstros.setTitle(QCoreApplication.translate("TelaMonstros", u"Repositorio Monstros", None))
    # retranslateUi

