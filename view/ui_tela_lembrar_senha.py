# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_lembrar_senha.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_LembrarSenha(object):
    def setupUi(self, LembrarSenha):
        if not LembrarSenha.objectName():
            LembrarSenha.setObjectName(u"LembrarSenha")
        LembrarSenha.resize(397, 327)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        LembrarSenha.setWindowIcon(icon)
        self.label = QLabel(LembrarSenha)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 120, 261, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.TelaLembrarSenha = QFrame(LembrarSenha)
        self.TelaLembrarSenha.setObjectName(u"TelaLembrarSenha")
        self.TelaLembrarSenha.setGeometry(QRect(0, 0, 471, 91))
        self.TelaLembrarSenha.setFrameShape(QFrame.StyledPanel)
        self.TelaLembrarSenha.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.TelaLembrarSenha)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 461, 91))
        self.label_5.setPixmap(QPixmap(u"_img/banner_lembreme.png"))
        self.txt_lembrar_senha = QLineEdit(LembrarSenha)
        self.txt_lembrar_senha.setObjectName(u"txt_lembrar_senha")
        self.txt_lembrar_senha.setGeometry(QRect(10, 150, 221, 25))
        self.txt_lembrar_senha.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.txt_lembrar_senha.setFont(font1)
        self.txt_lembrar_senha.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(LembrarSenha)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 180, 217, 55))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.btn_lembrar_senha = QPushButton(self.frame_2)
        self.btn_lembrar_senha.setObjectName(u"btn_lembrar_senha")
        self.btn_lembrar_senha.setMinimumSize(QSize(0, 35))
        font2 = QFont()
        font2.setFamily(u"Elephant")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.btn_lembrar_senha.setFont(font2)
        self.btn_lembrar_senha.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.057, y1:0, x2:0, y2:1, stop:0 rgba(41, 41, 41, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border: 1px solid gray\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(140, 140, 140);\n"
"	border: 1px solid gray\n"
"}")

        self.horizontalLayout.addWidget(self.btn_lembrar_senha)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(LembrarSenha)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 120, 121, 161))
        self.label_4.setPixmap(QPixmap(u"_img/monstro_lembrar.png"))
        self.label_6 = QLabel(LembrarSenha)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 260, 71, 20))
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(LembrarSenha)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 290, 61, 20))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_usuario = QLabel(LembrarSenha)
        self.label_usuario.setObjectName(u"label_usuario")
        self.label_usuario.setGeometry(QRect(100, 260, 131, 16))
        font3 = QFont()
        font3.setFamily(u"Elephant")
        font3.setPointSize(12)
        self.label_usuario.setFont(font3)
        self.label_usuario.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_senha = QLabel(LembrarSenha)
        self.label_senha.setObjectName(u"label_senha")
        self.label_senha.setGeometry(QRect(100, 290, 141, 16))
        self.label_senha.setFont(font3)
        self.label_senha.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.retranslateUi(LembrarSenha)

        QMetaObject.connectSlotsByName(LembrarSenha)
    # setupUi

    def retranslateUi(self, LembrarSenha):
        LembrarSenha.setWindowTitle(QCoreApplication.translate("LembrarSenha", u"Form", None))
        self.label.setText(QCoreApplication.translate("LembrarSenha", u"Informe o lembrete de senha:", None))
        self.label_5.setText("")
        self.label_2.setText("")
        self.btn_lembrar_senha.setText(QCoreApplication.translate("LembrarSenha", u"Lembre-me", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("LembrarSenha", u"Usu\u00e1rio:", None))
        self.label_7.setText(QCoreApplication.translate("LembrarSenha", u"Senha:", None))
        self.label_usuario.setText("")
        self.label_senha.setText("")
    # retranslateUi

