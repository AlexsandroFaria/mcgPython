# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_classe_personagem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaClasse(object):
    def setupUi(self, TelaClasse):
        if not TelaClasse.objectName():
            TelaClasse.setObjectName(u"TelaClasse")
        TelaClasse.resize(670, 451)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        TelaClasse.setWindowIcon(icon)
        TelaClasse.setStyleSheet(u"")
        self.frame = QFrame(TelaClasse)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 671, 111))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 671, 111))
        self.label.setPixmap(QPixmap(u"_img/banner_classe.png"))
        self.label_2 = QLabel(TelaClasse)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 160, 71, 21))
        font = QFont()
        font.setFamily(u"Elephant")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_nome_classe = QLineEdit(TelaClasse)
        self.txt_nome_classe.setObjectName(u"txt_nome_classe")
        self.txt_nome_classe.setGeometry(QRect(130, 160, 191, 25))
        self.txt_nome_classe.setMinimumSize(QSize(0, 25))
        self.txt_nome_classe.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.tabela_classe = QTableWidget(TelaClasse)
        if (self.tabela_classe.columnCount() < 3):
            self.tabela_classe.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_classe.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_classe.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_classe.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabela_classe.setObjectName(u"tabela_classe")
        self.tabela_classe.setGeometry(QRect(15, 230, 311, 191))
        self.tabela_classe.setAlternatingRowColors(True)
        self.tabela_classe.verticalHeader().setVisible(False)
        self.label_3 = QLabel(TelaClasse)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 190, 101, 21))
        self.label_3.setFont(font)
        self.txt_referencia = QLineEdit(TelaClasse)
        self.txt_referencia.setObjectName(u"txt_referencia")
        self.txt_referencia.setGeometry(QRect(130, 190, 191, 25))
        self.txt_referencia.setMinimumSize(QSize(0, 25))
        self.txt_referencia.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(TelaClasse)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(350, 140, 121, 281))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_pesquisar = QPushButton(self.frame_2)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamily(u"Elephant")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.btn_pesquisar.setFont(font1)
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
        font2 = QFont()
        font2.setFamily(u"Elephant")
        font2.setPointSize(10)
        self.btn_carregar.setFont(font2)
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
        self.btn_cadastrar.setFont(font2)
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
        self.btn_excluir.setFont(font2)
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
        self.btn_sair.setFont(font2)
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
        self.btn_limpar_tela.setFont(font2)
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

        self.label_4 = QLabel(TelaClasse)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(480, 170, 151, 211))
        self.label_4.setPixmap(QPixmap(u"_img/classe.png"))
        self.label_5 = QLabel(TelaClasse)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 130, 51, 20))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_id = QLineEdit(TelaClasse)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setEnabled(False)
        self.txt_id.setGeometry(QRect(130, 130, 71, 25))
        self.txt_id.setMinimumSize(QSize(0, 25))
        self.txt_id.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);\n"
"background-color: rgb(241, 241, 241);")
        QWidget.setTabOrder(self.txt_id, self.txt_nome_classe)
        QWidget.setTabOrder(self.txt_nome_classe, self.txt_referencia)
        QWidget.setTabOrder(self.txt_referencia, self.btn_pesquisar)
        QWidget.setTabOrder(self.btn_pesquisar, self.btn_cadastrar)
        QWidget.setTabOrder(self.btn_cadastrar, self.btn_excluir)
        QWidget.setTabOrder(self.btn_excluir, self.btn_sair)
        QWidget.setTabOrder(self.btn_sair, self.tabela_classe)

        self.retranslateUi(TelaClasse)

        QMetaObject.connectSlotsByName(TelaClasse)
    # setupUi

    def retranslateUi(self, TelaClasse):
        TelaClasse.setWindowTitle(QCoreApplication.translate("TelaClasse", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("TelaClasse", u"Classe:", None))
        ___qtablewidgetitem = self.tabela_classe.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaClasse", u"ID", None));
        ___qtablewidgetitem1 = self.tabela_classe.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaClasse", u"Classe", None));
        ___qtablewidgetitem2 = self.tabela_classe.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaClasse", u"Refer\u00eancia", None));
        self.label_3.setText(QCoreApplication.translate("TelaClasse", u"Refer\u00eancia:", None))
        self.btn_pesquisar.setText(QCoreApplication.translate("TelaClasse", u"Pesquisar", None))
        self.btn_carregar.setText(QCoreApplication.translate("TelaClasse", u"Carregar", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("TelaClasse", u"Cadastrar", None))
        self.btn_excluir.setText(QCoreApplication.translate("TelaClasse", u"Excluir", None))
        self.btn_sair.setText(QCoreApplication.translate("TelaClasse", u"Sair", None))
        self.btn_limpar_tela.setText(QCoreApplication.translate("TelaClasse", u"Limpar tela", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("TelaClasse", u"ID:", None))
    # retranslateUi

