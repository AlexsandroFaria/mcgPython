# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_raca_personagem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaRaca(object):
    def setupUi(self, TelaRaca):
        if not TelaRaca.objectName():
            TelaRaca.setObjectName(u"TelaRaca")
        TelaRaca.resize(670, 451)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        TelaRaca.setWindowIcon(icon)
        self.frame = QFrame(TelaRaca)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 671, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 671, 111))
        self.label.setPixmap(QPixmap(u"_img/banner_raca.png"))
        self.frame_2 = QFrame(TelaRaca)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(330, 140, 121, 281))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_pesquisar = QPushButton(self.frame_2)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setFamily(u"Elephant")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_pesquisar.setFont(font)
        self.btn_pesquisar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	\n"
"	background-color: rgb(141, 141, 141);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"_img/pesquisar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pesquisar.setIcon(icon1)
        self.btn_pesquisar.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_pesquisar)

        self.btn_carregar = QPushButton(self.frame_2)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"Elephant")
        font1.setPointSize(10)
        self.btn_carregar.setFont(font1)
        self.btn_carregar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	\n"
"	background-color: rgb(141, 141, 141);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon2)
        self.btn_carregar.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_carregar)

        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 30))
        self.btn_cadastrar.setFont(font1)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	\n"
"	background-color: rgb(141, 141, 141);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"_img/cadastrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon3)
        self.btn_cadastrar.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_cadastrar)

        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 30))
        self.btn_excluir.setFont(font1)
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	\n"
"	background-color: rgb(141, 141, 141);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"_img/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon4)
        self.btn_excluir.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_excluir)

        self.btn_sair = QPushButton(self.frame_2)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setMinimumSize(QSize(0, 30))
        self.btn_sair.setFont(font1)
        self.btn_sair.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	\n"
"	background-color: rgb(141, 141, 141);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair.setIcon(icon5)
        self.btn_sair.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_sair)

        self.btn_limpar_tela = QPushButton(self.frame_2)
        self.btn_limpar_tela.setObjectName(u"btn_limpar_tela")
        self.btn_limpar_tela.setMinimumSize(QSize(0, 30))
        self.btn_limpar_tela.setFont(font1)
        self.btn_limpar_tela.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	\n"
"	background-color: rgb(141, 141, 141);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(163, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"_img/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon6)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.btn_limpar_tela)

        self.txt_nome_raca = QLineEdit(TelaRaca)
        self.txt_nome_raca.setObjectName(u"txt_nome_raca")
        self.txt_nome_raca.setGeometry(QRect(130, 160, 191, 25))
        self.txt_nome_raca.setMinimumSize(QSize(0, 25))
        self.txt_nome_raca.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.label_5 = QLabel(TelaRaca)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 130, 51, 20))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(TelaRaca)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 160, 71, 21))
        font2 = QFont()
        font2.setFamily(u"Elephant")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(TelaRaca)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 190, 101, 21))
        self.label_3.setFont(font2)
        self.txt_id = QLineEdit(TelaRaca)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setEnabled(False)
        self.txt_id.setGeometry(QRect(130, 130, 71, 25))
        self.txt_id.setMinimumSize(QSize(0, 25))
        self.txt_id.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(241, 241, 241);")
        self.txt_referencia = QLineEdit(TelaRaca)
        self.txt_referencia.setObjectName(u"txt_referencia")
        self.txt_referencia.setGeometry(QRect(130, 190, 191, 25))
        self.txt_referencia.setMinimumSize(QSize(0, 25))
        self.txt_referencia.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.tabela_raca = QTableWidget(TelaRaca)
        if (self.tabela_raca.columnCount() < 3):
            self.tabela_raca.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_raca.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_raca.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_raca.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabela_raca.setObjectName(u"tabela_raca")
        self.tabela_raca.setGeometry(QRect(15, 230, 311, 191))
        self.tabela_raca.setAlternatingRowColors(True)
        self.tabela_raca.verticalHeader().setVisible(False)
        self.label_4 = QLabel(TelaRaca)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(460, 140, 191, 281))
        self.label_4.setPixmap(QPixmap(u"_img/raca_personagem.png"))

        self.retranslateUi(TelaRaca)

        QMetaObject.connectSlotsByName(TelaRaca)
    # setupUi

    def retranslateUi(self, TelaRaca):
        TelaRaca.setWindowTitle(QCoreApplication.translate("TelaRaca", u"Form", None))
        self.label.setText("")
        self.btn_pesquisar.setText(QCoreApplication.translate("TelaRaca", u"Pesquisar", None))
        self.btn_carregar.setText(QCoreApplication.translate("TelaRaca", u"Carregar", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("TelaRaca", u"Cadastrar", None))
        self.btn_excluir.setText(QCoreApplication.translate("TelaRaca", u"Excluir", None))
        self.btn_sair.setText(QCoreApplication.translate("TelaRaca", u"Sair", None))
        self.btn_limpar_tela.setText(QCoreApplication.translate("TelaRaca", u"Limpar tela", None))
        self.label_5.setText(QCoreApplication.translate("TelaRaca", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("TelaRaca", u"Ra\u00e7a", None))
        self.label_3.setText(QCoreApplication.translate("TelaRaca", u"Refer\u00eancia:", None))
        ___qtablewidgetitem = self.tabela_raca.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaRaca", u"ID", None));
        ___qtablewidgetitem1 = self.tabela_raca.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaRaca", u"Ra\u00e7a", None));
        ___qtablewidgetitem2 = self.tabela_raca.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaRaca", u"Refer\u00eancia", None));
        self.label_4.setText("")
    # retranslateUi

