# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_usuarios.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_TelaUsuarios(object):
    def setupUi(self, TelaUsuarios):
        if not TelaUsuarios.objectName():
            TelaUsuarios.setObjectName(u"TelaUsuarios")
        TelaUsuarios.resize(912, 571)
        icon = QIcon()
        icon.addFile(u"_img/icone_principal.png", QSize(), QIcon.Normal, QIcon.Off)
        TelaUsuarios.setWindowIcon(icon)
        self.frame = QFrame(TelaUsuarios)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 891, 131))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 0, 891, 131))
        self.label_9.setPixmap(QPixmap(u"_img/banner_usuarios.png"))
        self.tab_usuarios = QTabWidget(TelaUsuarios)
        self.tab_usuarios.setObjectName(u"tab_usuarios")
        self.tab_usuarios.setGeometry(QRect(10, 160, 891, 331))
        font = QFont()
        font.setFamily(u"Elephant")
        font.setPointSize(12)
        self.tab_usuarios.setFont(font)
        self.tab_usuarios.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.tab_usuarios.setIconSize(QSize(24, 24))
        self.tab_usuarios_cadastro = QWidget()
        self.tab_usuarios_cadastro.setObjectName(u"tab_usuarios_cadastro")
        self.label = QLabel(self.tab_usuarios_cadastro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 20, 131, 21))
        font1 = QFont()
        font1.setFamily(u"Elephant")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.tab_usuarios_cadastro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 141, 16))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.tab_usuarios_cadastro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 90, 71, 16))
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.tab_usuarios_cadastro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(90, 120, 81, 16))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.tab_usuarios_cadastro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(110, 150, 61, 16))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.tab_usuarios_cadastro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 180, 151, 16))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_7 = QLabel(self.tab_usuarios_cadastro)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 210, 81, 16))
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_8 = QLabel(self.tab_usuarios_cadastro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 240, 161, 16))
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.txt_id = QLineEdit(self.tab_usuarios_cadastro)
        self.txt_id.setObjectName(u"txt_id")
        self.txt_id.setEnabled(False)
        self.txt_id.setGeometry(QRect(190, 20, 113, 25))
        self.txt_id.setMinimumSize(QSize(0, 25))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setWeight(50)
        self.txt_id.setFont(font2)
        self.txt_id.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(232, 232, 232);")
        self.txt_nome_usuario = QLineEdit(self.tab_usuarios_cadastro)
        self.txt_nome_usuario.setObjectName(u"txt_nome_usuario")
        self.txt_nome_usuario.setGeometry(QRect(190, 60, 371, 25))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.txt_nome_usuario.sizePolicy().hasHeightForWidth())
        self.txt_nome_usuario.setSizePolicy(sizePolicy)
        self.txt_nome_usuario.setMinimumSize(QSize(0, 25))
        self.txt_nome_usuario.setFont(font2)
        self.txt_nome_usuario.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_email = QLineEdit(self.tab_usuarios_cadastro)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(190, 90, 371, 25))
        self.txt_email.setMinimumSize(QSize(0, 25))
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_usuario = QLineEdit(self.tab_usuarios_cadastro)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(190, 120, 371, 25))
        self.txt_usuario.setMinimumSize(QSize(0, 25))
        self.txt_usuario.setFont(font2)
        self.txt_usuario.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_senha = QLineEdit(self.tab_usuarios_cadastro)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(190, 150, 161, 25))
        self.txt_senha.setMinimumSize(QSize(0, 25))
        self.txt_senha.setFont(font2)
        self.txt_senha.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_confirmar_senha = QLineEdit(self.tab_usuarios_cadastro)
        self.txt_confirmar_senha.setObjectName(u"txt_confirmar_senha")
        self.txt_confirmar_senha.setGeometry(QRect(190, 180, 161, 25))
        self.txt_confirmar_senha.setMinimumSize(QSize(0, 25))
        self.txt_confirmar_senha.setFont(font2)
        self.txt_confirmar_senha.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.txt_confirmar_senha.setEchoMode(QLineEdit.Password)
        self.combo_acesso = QComboBox(self.tab_usuarios_cadastro)
        self.combo_acesso.addItem("")
        self.combo_acesso.addItem("")
        self.combo_acesso.addItem("")
        self.combo_acesso.setObjectName(u"combo_acesso")
        self.combo_acesso.setGeometry(QRect(190, 210, 161, 25))
        self.combo_acesso.setMinimumSize(QSize(0, 25))
        font3 = QFont()
        font3.setFamily(u"Elephant")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.combo_acesso.setFont(font3)
        self.combo_acesso.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(232, 232, 232);")
        self.txtlembrete_senha = QLineEdit(self.tab_usuarios_cadastro)
        self.txtlembrete_senha.setObjectName(u"txtlembrete_senha")
        self.txtlembrete_senha.setGeometry(QRect(190, 240, 381, 25))
        self.txtlembrete_senha.setMinimumSize(QSize(0, 25))
        self.txtlembrete_senha.setFont(font2)
        self.txtlembrete_senha.setStyleSheet(u"border-radius: 5px;\n"
"border:1px solid gray;\n"
"background-color: rgb(255, 255, 255);")
        self.label_10 = QLabel(self.tab_usuarios_cadastro)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(400, 150, 111, 81))
        self.label_10.setPixmap(QPixmap(u"_img/mimico.png"))
        self.label_11 = QLabel(self.tab_usuarios_cadastro)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(650, 30, 151, 251))
        self.label_11.setPixmap(QPixmap(u"_img/tela_usuario.png"))
        self.btn_limpar_campos = QPushButton(self.tab_usuarios_cadastro)
        self.btn_limpar_campos.setObjectName(u"btn_limpar_campos")
        self.btn_limpar_campos.setGeometry(QRect(420, 20, 141, 31))
        self.btn_limpar_campos.setFont(font1)
        self.btn_limpar_campos.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"	color: rgb(241, 241, 241);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"_img/eraser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_campos.setIcon(icon1)
        self.btn_limpar_campos.setIconSize(QSize(24, 24))
        icon2 = QIcon()
        icon2.addFile(u"_img/usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_usuarios.addTab(self.tab_usuarios_cadastro, icon2, "")
        self.tab_usuarios_consulta = QWidget()
        self.tab_usuarios_consulta.setObjectName(u"tab_usuarios_consulta")
        self.tabela_usuarios = QTableWidget(self.tab_usuarios_consulta)
        if (self.tabela_usuarios.columnCount() < 7):
            self.tabela_usuarios.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tabela_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.tabela_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font4 = QFont()
        font4.setFamily(u"Elephant")
        font4.setPointSize(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.tabela_usuarios.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabela_usuarios.setObjectName(u"tabela_usuarios")
        self.tabela_usuarios.setGeometry(QRect(20, 50, 841, 181))
        self.tabela_usuarios.setAlternatingRowColors(True)
        self.tabela_usuarios.verticalHeader().setVisible(False)
        self.frame_3 = QFrame(self.tab_usuarios_consulta)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(23, 240, 841, 49))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_2.addWidget(self.label_12)

        self.btn_carregar = QPushButton(self.frame_3)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setMinimumSize(QSize(0, 35))
        self.btn_carregar.setFont(font)
        self.btn_carregar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"	color: rgb(241, 241, 241);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"_img/carregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_carregar.setIcon(icon3)
        self.btn_carregar.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.btn_carregar)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_2.addWidget(self.label_13)

        icon4 = QIcon()
        icon4.addFile(u"_img/consulta_usuario.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tab_usuarios.addTab(self.tab_usuarios_consulta, icon4, "")
        self.frame_2 = QFrame(TelaUsuarios)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(17, 500, 881, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout.addWidget(self.label_14)

        self.btn_cadastrar = QPushButton(self.frame_2)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(0, 35))
        self.btn_cadastrar.setFont(font)
        self.btn_cadastrar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"	color: rgb(241, 241, 241);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"_img/cadastrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cadastrar.setIcon(icon5)
        self.btn_cadastrar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_cadastrar)

        self.btn_alterar = QPushButton(self.frame_2)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(0, 35))
        self.btn_alterar.setFont(font)
        self.btn_alterar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"	color: rgb(241, 241, 241);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"_img/alterar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon6)
        self.btn_alterar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_alterar)

        self.btn_excluir = QPushButton(self.frame_2)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 35))
        self.btn_excluir.setFont(font)
        self.btn_excluir.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"	color: rgb(241, 241, 241);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"_img/excluir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir.setIcon(icon7)
        self.btn_excluir.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_excluir)

        self.btn_fechar = QPushButton(self.frame_2)
        self.btn_fechar.setObjectName(u"btn_fechar")
        self.btn_fechar.setMinimumSize(QSize(0, 35))
        self.btn_fechar.setFont(font)
        self.btn_fechar.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid gray;\n"
"	background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(141, 141, 141);\n"
"	color: rgb(241, 241, 241);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"_img/sair.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_fechar.setIcon(icon8)
        self.btn_fechar.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.btn_fechar)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout.addWidget(self.label_15)


        self.retranslateUi(TelaUsuarios)

        self.tab_usuarios.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(TelaUsuarios)
    # setupUi

    def retranslateUi(self, TelaUsuarios):
        TelaUsuarios.setWindowTitle(QCoreApplication.translate("TelaUsuarios", u"Form", None))
        self.label_9.setText("")
        self.label.setText(QCoreApplication.translate("TelaUsuarios", u"Identificador:", None))
        self.label_2.setText(QCoreApplication.translate("TelaUsuarios", u"Nome do Usu\u00e1rio:", None))
        self.label_3.setText(QCoreApplication.translate("TelaUsuarios", u"E-mail:", None))
        self.label_4.setText(QCoreApplication.translate("TelaUsuarios", u"Usu\u00e1rio:", None))
        self.label_5.setText(QCoreApplication.translate("TelaUsuarios", u"Senha:", None))
        self.label_6.setText(QCoreApplication.translate("TelaUsuarios", u"Confirmar Senha:", None))
        self.label_7.setText(QCoreApplication.translate("TelaUsuarios", u"Acesso:", None))
        self.label_8.setText(QCoreApplication.translate("TelaUsuarios", u"Lembrete de senha:", None))
        self.combo_acesso.setItemText(0, QCoreApplication.translate("TelaUsuarios", u"Selecione uma op\u00e7\u00e3o", None))
        self.combo_acesso.setItemText(1, QCoreApplication.translate("TelaUsuarios", u"Mestre", None))
        self.combo_acesso.setItemText(2, QCoreApplication.translate("TelaUsuarios", u"Jogador", None))

        self.label_10.setText("")
        self.label_11.setText("")
        self.btn_limpar_campos.setText(QCoreApplication.translate("TelaUsuarios", u"Limpar Tela", None))
        self.tab_usuarios.setTabText(self.tab_usuarios.indexOf(self.tab_usuarios_cadastro), QCoreApplication.translate("TelaUsuarios", u"Cadastro de Usu\u00e1rios", None))
        ___qtablewidgetitem = self.tabela_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("TelaUsuarios", u"Identificador", None));
        ___qtablewidgetitem1 = self.tabela_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("TelaUsuarios", u"Nome Usu\u00e1rio", None));
        ___qtablewidgetitem2 = self.tabela_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("TelaUsuarios", u"E-mail", None));
        ___qtablewidgetitem3 = self.tabela_usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("TelaUsuarios", u"Usu\u00e1rio", None));
        ___qtablewidgetitem4 = self.tabela_usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("TelaUsuarios", u"Senha", None));
        ___qtablewidgetitem5 = self.tabela_usuarios.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("TelaUsuarios", u"Acesso", None));
        ___qtablewidgetitem6 = self.tabela_usuarios.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("TelaUsuarios", u"Lembrar Senha", None));
        self.label_12.setText("")
        self.btn_carregar.setText(QCoreApplication.translate("TelaUsuarios", u"Carregar", None))
        self.label_13.setText("")
        self.tab_usuarios.setTabText(self.tab_usuarios.indexOf(self.tab_usuarios_consulta), QCoreApplication.translate("TelaUsuarios", u"Consulta Usu\u00e1rios", None))
        self.label_14.setText("")
        self.btn_cadastrar.setText(QCoreApplication.translate("TelaUsuarios", u"Cadastrar", None))
        self.btn_alterar.setText(QCoreApplication.translate("TelaUsuarios", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("TelaUsuarios", u"Excluir", None))
        self.btn_fechar.setText(QCoreApplication.translate("TelaUsuarios", u"Fechar", None))
        self.label_15.setText("")
    # retranslateUi

