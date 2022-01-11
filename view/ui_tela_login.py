# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaLogin(object):
    def setupUi(self, TelaLogin):
        if not TelaLogin.objectName():
            TelaLogin.setObjectName(u"TelaLogin")
        TelaLogin.resize(395, 448)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        TelaLogin.setWindowIcon(icon)
        self.menu_criacao_banco = QAction(TelaLogin)
        self.menu_criacao_banco.setObjectName(u"menu_criacao_banco")
        icon1 = QIcon()
        icon1.addFile(u"_img/banco_dados.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_criacao_banco.setIcon(icon1)
        self.menu_sair = QAction(TelaLogin)
        self.menu_sair.setObjectName(u"menu_sair")
        icon2 = QIcon()
        icon2.addFile(u"_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_sair.setIcon(icon2)
        self.centralwidget = QWidget(TelaLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 401, 431))
        self.label.setPixmap(QPixmap(u"_img/login.png"))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 110, 101, 20))
        font = QFont()
        font.setFamily(u"Elephant")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 160, 81, 20))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 210, 371, 57))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_logar = QPushButton(self.frame)
        self.btn_logar.setObjectName(u"btn_logar")
        self.btn_logar.setMinimumSize(QSize(0, 35))
        font1 = QFont()
        font1.setFamily(u"Elephant")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.btn_logar.setFont(font1)
        self.btn_logar.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"Elephant\";\n"
"	background-color: rgb(167, 172, 172);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(141, 0, 0);\n"
"	border: solid 5p\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_logar)

        self.btn_fechar = QPushButton(self.frame)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setMinimumSize(QSize(0, 35))
        self.btn_fechar.setFont(font1)
        self.btn_fechar.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"Elephant\";\n"
"	background-color: rgb(167, 172, 172);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(141, 0, 0);\n"
"	border: solid 5p\n"
"}font: 12pt \"Elephant\";")

        self.horizontalLayout.addWidget(self.btn_fechar)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 270, 371, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_lembrar_senha = QPushButton(self.frame_2)
        self.btn_lembrar_senha.setObjectName(u"btn_lembrar_senha")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_lembrar_senha.sizePolicy().hasHeightForWidth())
        self.btn_lembrar_senha.setSizePolicy(sizePolicy)
        self.btn_lembrar_senha.setMinimumSize(QSize(0, 35))
        self.btn_lembrar_senha.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"Elephant\";\n"
"	background-color: rgb(167, 172, 172);\n"
"	border-radius: 5px;\n"
"	border: 1px solid\n"
"}\n"
"QPushButton:hover{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(141, 0, 0);\n"
"	border: solid 5p\n"
"}font: 12pt \"Elephant\";")

        self.verticalLayout.addWidget(self.btn_lembrar_senha)

        self.txt_usuario = QLineEdit(self.centralwidget)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(170, 110, 201, 25))
        self.txt_usuario.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.txt_usuario.setFont(font2)
        self.txt_usuario.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid red")
        self.txt_senha = QLineEdit(self.centralwidget)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(170, 160, 201, 25))
        self.txt_senha.setMinimumSize(QSize(0, 25))
        self.txt_senha.setFont(font2)
        self.txt_senha.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid red")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        TelaLogin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(TelaLogin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 395, 21))
        self.menuConex_o = QMenu(self.menubar)
        self.menuConex_o.setObjectName(u"menuConex_o")
        TelaLogin.setMenuBar(self.menubar)
        QWidget.setTabOrder(self.txt_usuario, self.txt_senha)
        QWidget.setTabOrder(self.txt_senha, self.btn_logar)
        QWidget.setTabOrder(self.btn_logar, self.btn_fechar)
        QWidget.setTabOrder(self.btn_fechar, self.btn_lembrar_senha)

        self.menubar.addAction(self.menuConex_o.menuAction())
        self.menuConex_o.addAction(self.menu_criacao_banco)
        self.menuConex_o.addSeparator()
        self.menuConex_o.addAction(self.menu_sair)

        self.retranslateUi(TelaLogin)

        QMetaObject.connectSlotsByName(TelaLogin)
    # setupUi

    def retranslateUi(self, TelaLogin):
        TelaLogin.setWindowTitle(QCoreApplication.translate("TelaLogin", u"MainWindow", None))
        self.menu_criacao_banco.setText(QCoreApplication.translate("TelaLogin", u"Criar estrutura de Banco de dados", None))
        self.menu_sair.setText(QCoreApplication.translate("TelaLogin", u"Sair", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("TelaLogin", u"<html><head/><body><p><span style=\" color:#ffffff;\">Usu\u00e1rio:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("TelaLogin", u"<html><head/><body><p><span style=\" color:#ffffff;\">Senha:</span></p></body></html>", None))
        self.btn_logar.setText(QCoreApplication.translate("TelaLogin", u"Logar", None))
        self.btn_fechar.setText(QCoreApplication.translate("TelaLogin", u"Fechar", None))
        self.btn_lembrar_senha.setText(QCoreApplication.translate("TelaLogin", u"Lembrar Senha", None))
        self.menuConex_o.setTitle(QCoreApplication.translate("TelaLogin", u"Conex\u00e3o", None))
    # retranslateUi

