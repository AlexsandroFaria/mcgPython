# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_sobre.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Sobre(object):
    def setupUi(self, Sobre):
        if not Sobre.objectName():
            Sobre.setObjectName(u"Sobre")
        Sobre.resize(400, 505)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        Sobre.setWindowIcon(icon)
        self.label = QLabel(Sobre)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 401, 231))
        self.label.setPixmap(QPixmap(u"_img/tela_sobre.png"))
        self.groupBox = QGroupBox(Sobre)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 240, 381, 251))
        font = QFont()
        font.setFamily(u"Elephant")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 361, 21))
        font1 = QFont()
        font1.setFamily(u"Elephant")
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 331, 31))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 150, 361, 31))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(10)
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 180, 361, 16))
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 130, 361, 21))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(14)
        font3.setUnderline(True)
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 210, 361, 20))
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Sobre)

        QMetaObject.connectSlotsByName(Sobre)
    # setupUi

    def retranslateUi(self, Sobre):
        Sobre.setWindowTitle(QCoreApplication.translate("Sobre", u"Form", None))
        self.label.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("Sobre", u"Sobre", None))
        self.label_2.setText(QCoreApplication.translate("Sobre", u"Desenvolvido por: Alexsandro Luiz de Faria", None))
        self.label_3.setText(QCoreApplication.translate("Sobre", u"E-mail: alexsandro.lfaria@gmail.com", None))
        self.label_4.setText(QCoreApplication.translate("Sobre", u"Programa de RPG para sistema D&D 5 Edi\u00e7\u00e3o.", None))
        self.label_5.setText(QCoreApplication.translate("Sobre", u"Sistema para uso pr\u00f3prio n\u00e3o comercial.", None))
        self.label_6.setText(QCoreApplication.translate("Sobre", u"ATEN\u00c7\u00c2O", None))
        self.label_7.setText(QCoreApplication.translate("Sobre", u"N\u00e3o comercialize este produto.", None))
    # retranslateUi

