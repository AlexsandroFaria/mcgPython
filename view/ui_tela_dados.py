# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_dados.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaDados(object):
    def setupUi(self, TelaDados):
        if not TelaDados.objectName():
            TelaDados.setObjectName(u"TelaDados")
        TelaDados.resize(400, 325)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        TelaDados.setWindowIcon(icon)
        self.frame = QFrame(TelaDados)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 401, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 401, 81))
        self.label_3.setPixmap(QPixmap(u"_img/banner_dados.png"))
        self.label = QLabel(TelaDados)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 100, 151, 21))
        font = QFont()
        font.setFamily(u"Elephant")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(TelaDados)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 140, 161, 21))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.combo_faces = QComboBox(TelaDados)
        self.combo_faces.addItem("")
        self.combo_faces.addItem("")
        self.combo_faces.addItem("")
        self.combo_faces.addItem("")
        self.combo_faces.addItem("")
        self.combo_faces.addItem("")
        self.combo_faces.addItem("")
        self.combo_faces.setObjectName(u"combo_faces")
        self.combo_faces.setGeometry(QRect(170, 100, 211, 25))
        self.combo_faces.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setFamily(u"Elephant")
        font1.setPointSize(10)
        self.combo_faces.setFont(font1)
        self.txt_numero_dados = QLineEdit(TelaDados)
        self.txt_numero_dados.setObjectName(u"txt_numero_dados")
        self.txt_numero_dados.setGeometry(QRect(170, 140, 81, 25))
        self.txt_numero_dados.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        self.txt_numero_dados.setFont(font2)
        self.txt_numero_dados.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray")
        self.btn_rolar_dados = QPushButton(TelaDados)
        self.btn_rolar_dados.setObjectName(u"btn_rolar_dados")
        self.btn_rolar_dados.setGeometry(QRect(260, 130, 121, 41))
        self.btn_rolar_dados.setFont(font1)
        self.btn_rolar_dados.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u"_img/dado.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_rolar_dados.setIcon(icon1)
        self.btn_rolar_dados.setIconSize(QSize(24, 24))
        self.label_4 = QLabel(TelaDados)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 80, 401, 241))
        self.label_4.setPixmap(QPixmap(u"_img/fundo_dados.png"))
        self.txt_resultado = QTextEdit(TelaDados)
        self.txt_resultado.setObjectName(u"txt_resultado")
        self.txt_resultado.setGeometry(QRect(173, 180, 211, 71))
        self.txt_resultado.setStyleSheet(u"border-radius: 5px;\n"
"border: 1px solid gray;")
        self.label_5 = QLabel(TelaDados)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 210, 111, 16))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_2 = QFrame(TelaDados)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(19, 250, 371, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.btn_limpar_tela = QPushButton(self.frame_2)
        self.btn_limpar_tela.setObjectName(u"btn_limpar_tela")
        self.btn_limpar_tela.setFont(font)
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
        icon2 = QIcon()
        icon2.addFile(u"_img/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_tela.setIcon(icon2)
        self.btn_limpar_tela.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_limpar_tela)

        self.btn_sair = QPushButton(self.frame_2)
        self.btn_sair.setObjectName(u"btn_sair")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sair.sizePolicy().hasHeightForWidth())
        self.btn_sair.setSizePolicy(sizePolicy)
        self.btn_sair.setMinimumSize(QSize(55, 0))
        self.btn_sair.setFont(font)
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
        icon3 = QIcon()
        icon3.addFile(u"_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sair.setIcon(icon3)
        self.btn_sair.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_sair)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.label_4.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.combo_faces.raise_()
        self.txt_numero_dados.raise_()
        self.btn_rolar_dados.raise_()
        self.txt_resultado.raise_()
        self.label_5.raise_()
        self.frame_2.raise_()

        self.retranslateUi(TelaDados)

        QMetaObject.connectSlotsByName(TelaDados)
    # setupUi

    def retranslateUi(self, TelaDados):
        TelaDados.setWindowTitle(QCoreApplication.translate("TelaDados", u"Form", None))
        self.label_3.setText("")
        self.label.setText(QCoreApplication.translate("TelaDados", u"N\u00famero de Faces:", None))
        self.label_2.setText(QCoreApplication.translate("TelaDados", u"N\u00famero de Dados:", None))
        self.combo_faces.setItemText(0, QCoreApplication.translate("TelaDados", u"Selecionar", None))
        self.combo_faces.setItemText(1, QCoreApplication.translate("TelaDados", u"1 D 4", None))
        self.combo_faces.setItemText(2, QCoreApplication.translate("TelaDados", u"1 D 6", None))
        self.combo_faces.setItemText(3, QCoreApplication.translate("TelaDados", u"1 D 8", None))
        self.combo_faces.setItemText(4, QCoreApplication.translate("TelaDados", u"1 D 10", None))
        self.combo_faces.setItemText(5, QCoreApplication.translate("TelaDados", u"1 D 12", None))
        self.combo_faces.setItemText(6, QCoreApplication.translate("TelaDados", u"1 D 20", None))

        self.btn_rolar_dados.setText(QCoreApplication.translate("TelaDados", u"Rolar dados", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate("TelaDados", u"Resultado:", None))
        self.label_6.setText("")
        self.btn_limpar_tela.setText(QCoreApplication.translate("TelaDados", u"Limpar Tela", None))
        self.btn_sair.setText(QCoreApplication.translate("TelaDados", u"Sair", None))
        self.label_7.setText("")
    # retranslateUi

