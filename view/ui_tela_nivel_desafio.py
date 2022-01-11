# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_nivel_desafio.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_NivelDesafio(object):
    def setupUi(self, NivelDesafio):
        if not NivelDesafio.objectName():
            NivelDesafio.setObjectName(u"NivelDesafio")
        NivelDesafio.resize(1174, 588)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        NivelDesafio.setWindowIcon(icon)
        self.frame = QFrame(NivelDesafio)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1171, 121))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 1171, 121))
        self.label_8.setPixmap(QPixmap(u"_img/banner_nivel.png"))
        self.label = QLabel(NivelDesafio)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 140, 191, 21))
        font = QFont()
        font.setFamily(u"Elephant")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.combo_selecionar_personagem = QComboBox(NivelDesafio)
        self.combo_selecionar_personagem.addItem("")
        self.combo_selecionar_personagem.setObjectName(u"combo_selecionar_personagem")
        self.combo_selecionar_personagem.setGeometry(QRect(210, 140, 201, 25))
        self.combo_selecionar_personagem.setMinimumSize(QSize(0, 25))
        font1 = QFont()
        font1.setFamily(u"Elephant")
        font1.setPointSize(10)
        self.combo_selecionar_personagem.setFont(font1)
        self.btn_inserir = QPushButton(NivelDesafio)
        self.btn_inserir.setObjectName(u"btn_inserir")
        self.btn_inserir.setGeometry(QRect(430, 140, 241, 31))
        self.btn_inserir.setMinimumSize(QSize(0, 25))
        self.btn_inserir.setFont(font)
        self.btn_inserir.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"_img/cadastrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_inserir.setIcon(icon1)
        self.btn_inserir.setIconSize(QSize(24, 24))
        self.tabela_nivel_usuario = QTableWidget(NivelDesafio)
        if (self.tabela_nivel_usuario.columnCount() < 6):
            self.tabela_nivel_usuario.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tabela_nivel_usuario.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tabela_nivel_usuario.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tabela_nivel_usuario.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tabela_nivel_usuario.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tabela_nivel_usuario.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tabela_nivel_usuario.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabela_nivel_usuario.setObjectName(u"tabela_nivel_usuario")
        self.tabela_nivel_usuario.setGeometry(QRect(20, 180, 651, 131))
        self.tabela_nivel_usuario.verticalHeader().setVisible(False)
        self.groupBox = QGroupBox(NivelDesafio)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 320, 651, 141))
        font2 = QFont()
        font2.setFamily(u"Elephant")
        font2.setPointSize(16)
        self.groupBox.setFont(font2)
        self.groupBox.setFocusPolicy(Qt.NoFocus)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(True)
        self.frame_3 = QFrame(self.groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 30, 631, 45))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamily(u"Elephant")
        font3.setPointSize(14)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.frame_4 = QFrame(self.groupBox)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 80, 631, 49))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_nivel_facil = QLabel(self.frame_4)
        self.txt_nivel_facil.setObjectName(u"txt_nivel_facil")
        self.txt_nivel_facil.setStyleSheet(u"border: 1px solid blue;\n"
"border-radius: 5px")
        self.txt_nivel_facil.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_nivel_facil)

        self.txt_nivel_medio = QLabel(self.frame_4)
        self.txt_nivel_medio.setObjectName(u"txt_nivel_medio")
        self.txt_nivel_medio.setStyleSheet(u"border: 1px solid blue;\n"
"border-radius: 5px")
        self.txt_nivel_medio.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_nivel_medio)

        self.txt_nivel_dificil = QLabel(self.frame_4)
        self.txt_nivel_dificil.setObjectName(u"txt_nivel_dificil")
        self.txt_nivel_dificil.setStyleSheet(u"border: 1px solid blue;\n"
"border-radius: 5px")
        self.txt_nivel_dificil.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_nivel_dificil)

        self.txt_nivel_mortal = QLabel(self.frame_4)
        self.txt_nivel_mortal.setObjectName(u"txt_nivel_mortal")
        self.txt_nivel_mortal.setStyleSheet(u"border: 1px solid blue;\n"
"border-radius: 5px")
        self.txt_nivel_mortal.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_nivel_mortal)

        self.frame_5 = QFrame(NivelDesafio)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(20, 460, 651, 61))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_4.addWidget(self.label_12)

        self.btn_limpar_lista = QPushButton(self.frame_5)
        self.btn_limpar_lista.setObjectName(u"btn_limpar_lista")
        self.btn_limpar_lista.setMinimumSize(QSize(0, 35))
        self.btn_limpar_lista.setFont(font)
        self.btn_limpar_lista.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"_img/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_lista.setIcon(icon2)
        self.btn_limpar_lista.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.btn_limpar_lista)

        self.label_13 = QLabel(self.frame_5)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.line = QFrame(NivelDesafio)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(690, 140, 16, 431))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label_2 = QLabel(NivelDesafio)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(710, 140, 451, 151))
        self.label_2.setPixmap(QPixmap(u"_img/multiplicadores.PNG"))
        self.label_3 = QLabel(NivelDesafio)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(720, 310, 221, 21))
        self.label_3.setFont(font)
        self.txt_total_xp_monstros = QLineEdit(NivelDesafio)
        self.txt_total_xp_monstros.setObjectName(u"txt_total_xp_monstros")
        self.txt_total_xp_monstros.setGeometry(QRect(950, 310, 113, 25))
        self.txt_total_xp_monstros.setMinimumSize(QSize(0, 25))
        self.txt_total_xp_monstros.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);")
        self.label_9 = QLabel(NivelDesafio)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(720, 350, 181, 21))
        self.label_9.setFont(font)
        self.combo_selecionar_numero_monstros = QComboBox(NivelDesafio)
        self.combo_selecionar_numero_monstros.addItem("")
        self.combo_selecionar_numero_monstros.addItem("")
        self.combo_selecionar_numero_monstros.addItem("")
        self.combo_selecionar_numero_monstros.addItem("")
        self.combo_selecionar_numero_monstros.addItem("")
        self.combo_selecionar_numero_monstros.addItem("")
        self.combo_selecionar_numero_monstros.addItem("")
        self.combo_selecionar_numero_monstros.setObjectName(u"combo_selecionar_numero_monstros")
        self.combo_selecionar_numero_monstros.setGeometry(QRect(920, 350, 141, 25))
        self.combo_selecionar_numero_monstros.setMinimumSize(QSize(0, 25))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.combo_selecionar_numero_monstros.setFont(font4)
        self.frame_2 = QFrame(NivelDesafio)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(720, 380, 431, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_calcular_encontro = QPushButton(self.frame_2)
        self.btn_calcular_encontro.setObjectName(u"btn_calcular_encontro")
        self.btn_calcular_encontro.setMinimumSize(QSize(0, 30))
        self.btn_calcular_encontro.setFont(font)
        self.btn_calcular_encontro.setStyleSheet(u"QPushButton{\n"
"	border: 1px solid gray;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"_img/calcular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_calcular_encontro.setIcon(icon3)
        self.btn_calcular_encontro.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_calcular_encontro)

        self.frame_6 = QFrame(NivelDesafio)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(720, 440, 431, 101))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_Resultado_encontro = QLabel(self.frame_6)
        self.label_Resultado_encontro.setObjectName(u"label_Resultado_encontro")
        self.label_Resultado_encontro.setFont(font3)
        self.label_Resultado_encontro.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 5px")
        self.label_Resultado_encontro.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_Resultado_encontro)


        self.retranslateUi(NivelDesafio)

        QMetaObject.connectSlotsByName(NivelDesafio)
    # setupUi

    def retranslateUi(self, NivelDesafio):
        NivelDesafio.setWindowTitle(QCoreApplication.translate("NivelDesafio", u"Form", None))
        self.label_8.setText("")
        self.label.setText(QCoreApplication.translate("NivelDesafio", u"Selecionar Peronagem:", None))
        self.combo_selecionar_personagem.setItemText(0, QCoreApplication.translate("NivelDesafio", u"Selecionar", None))

        self.btn_inserir.setText(QCoreApplication.translate("NivelDesafio", u"Inserir", None))
        ___qtablewidgetitem = self.tabela_nivel_usuario.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("NivelDesafio", u"Nome", None));
        ___qtablewidgetitem1 = self.tabela_nivel_usuario.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("NivelDesafio", u"N\u00edvel", None));
        ___qtablewidgetitem2 = self.tabela_nivel_usuario.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("NivelDesafio", u"Nivel F\u00e1cil", None));
        ___qtablewidgetitem3 = self.tabela_nivel_usuario.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("NivelDesafio", u"N\u00edvel M\u00e9dio", None));
        ___qtablewidgetitem4 = self.tabela_nivel_usuario.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("NivelDesafio", u"N\u00edvel Dificil", None));
        ___qtablewidgetitem5 = self.tabela_nivel_usuario.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("NivelDesafio", u"N\u00edvel Mortal", None));
        self.groupBox.setTitle(QCoreApplication.translate("NivelDesafio", u"Resultado", None))
        self.label_4.setText(QCoreApplication.translate("NivelDesafio", u"F\u00e1cil", None))
        self.label_5.setText(QCoreApplication.translate("NivelDesafio", u"M\u00e9dio", None))
        self.label_6.setText(QCoreApplication.translate("NivelDesafio", u"Dif\u00edcil", None))
        self.label_7.setText(QCoreApplication.translate("NivelDesafio", u"Mortal", None))
        self.txt_nivel_facil.setText("")
        self.txt_nivel_medio.setText("")
        self.txt_nivel_dificil.setText("")
        self.txt_nivel_mortal.setText("")
        self.label_12.setText("")
        self.btn_limpar_lista.setText(QCoreApplication.translate("NivelDesafio", u"Limpar Lista de N\u00edvel", None))
        self.label_13.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("NivelDesafio", u"Total de XP dos Monstros:", None))
        self.label_9.setText(QCoreApplication.translate("NivelDesafio", u"N\u00famero de Monstros:", None))
        self.combo_selecionar_numero_monstros.setItemText(0, QCoreApplication.translate("NivelDesafio", u"Selecionar", None))
        self.combo_selecionar_numero_monstros.setItemText(1, QCoreApplication.translate("NivelDesafio", u"1", None))
        self.combo_selecionar_numero_monstros.setItemText(2, QCoreApplication.translate("NivelDesafio", u"2", None))
        self.combo_selecionar_numero_monstros.setItemText(3, QCoreApplication.translate("NivelDesafio", u"3-6", None))
        self.combo_selecionar_numero_monstros.setItemText(4, QCoreApplication.translate("NivelDesafio", u"7-10", None))
        self.combo_selecionar_numero_monstros.setItemText(5, QCoreApplication.translate("NivelDesafio", u"11-14", None))
        self.combo_selecionar_numero_monstros.setItemText(6, QCoreApplication.translate("NivelDesafio", u"15 ou mais", None))

        self.btn_calcular_encontro.setText(QCoreApplication.translate("NivelDesafio", u"Calcular", None))
        self.label_10.setText(QCoreApplication.translate("NivelDesafio", u"Resultado do n\u00edvel do combate", None))
        self.label_Resultado_encontro.setText("")
    # retranslateUi

