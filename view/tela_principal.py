from view.tela_combate import TelaCombate
from view.tela_dados import TelaDados
from view.tela_monstros import TelaMonstros
from view.tela_nivel_desafio import TelaNivelDesafio
from view.tela_sobre import TelaSobre
from view.tela_usuario import TelaUsuario
from view.tela_classe_personagem import TelaClassePersonagem
from view.tela_personagem import TelaPersonagem
from view.tela_raca_personagem import TelaRacaPersonagem
from view.ui_tela_principal import Ui_TelaPrincipal
from PySide2.QtWidgets import QMainWindow


class TelaPrincipal(QMainWindow, Ui_TelaPrincipal):
    def __init__(self):
        super(TelaPrincipal, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('MasterControlGuide')
        self.showMaximized()

        self.menu_cadastro_usuario.triggered.connect(self.abrir_tela_usuario)
        self.menu_consulta_usuarios.triggered.connect(self.abrir_tela_usuario_consulta)
        self.menu_cadastro_classes.triggered.connect(self.abrir_tela_classe_personagem)
        self.menu_cadastro_raca.triggered.connect(self.abrir_tela_raca_personagem)
        self.menu_cadastro_personagem.triggered.connect(self.abrir_tela_personagem)
        self.menu_consultar_personagem.triggered.connect(self.abrir_tela_personagem_consulta)
        self.menu_cadastrar_monstros.triggered.connect(self.abrir_tela_monstros)
        self.menu_consultar_monstros.triggered.connect(self.abrir_tela_monstros_consulta)
        self.menu_rolar_dados.triggered.connect(self.abrir_tela_dados)
        self.menu_sair.triggered.connect(self.close)
        self.menu_combate.triggered.connect(self.abrir_tela_combate)
        self.menu_nivel_desafio.triggered.connect(self.abrir_tela_nivel_desafio)
        self.menu_sobre.triggered.connect(self.abrir_tela_sobre)

    def abrir_tela_usuario(self):
        self.tela_usuario = TelaUsuario()
        self.tela_usuario.show()

    def abrir_tela_usuario_consulta(self):
        self.tela_usuario = TelaUsuario()
        self.tela_usuario.tab_usuarios.setCurrentWidget(self.tela_usuario.tab_usuarios_consulta)
        self.tela_usuario.show()

    def abrir_tela_classe_personagem(self):
        self.tela_classe = TelaClassePersonagem()
        self.tela_classe.show()

    def abrir_tela_raca_personagem(self):
        self.tela_raca = TelaRacaPersonagem()
        self.tela_raca.show()

    def abrir_tela_personagem(self):
        self.tela_personagem = TelaPersonagem()
        self.tela_personagem.show()

    def abrir_tela_personagem_consulta(self):
        self.tela_personagem = TelaPersonagem()
        self.tela_personagem.tab_personagem.setCurrentWidget(self.tela_personagem.tab_consulta_personagem)
        self.tela_personagem.show()

    def abrir_tela_monstros(self):
        self.tela_monstros = TelaMonstros()
        self.tela_monstros.show()

    def abrir_tela_monstros_consulta(self):
        self.tela_monstros = TelaMonstros()
        self.tela_monstros.tab_monstros.setCurrentWidget(self.tela_monstros.tab_consulta_monstros)
        self.tela_monstros.show()

    def abrir_tela_dados(self):
        self.tela_dados = TelaDados()
        self.tela_dados.show()

    def abrir_tela_combate(self):
        self.tela_combate = TelaCombate()
        self.tela_combate.show()

    def abrir_tela_nivel_desafio(self):
        self.tela_nivel_desafio = TelaNivelDesafio()
        self.tela_nivel_desafio.show()

    def abrir_tela_sobre(self):
        self.tela_sobre = TelaSobre()
        self.tela_sobre.show()
