class Personagem:
    def __init__(self, id_personagem=None, nome_personagem=None, nome_classe=None, nome_raca=None, dados_vida=None,
                 total_pontos_vida=None, pontos_vida_atual=None, pontos_experiencia=None, nivel=None,
                 ponto_heroico=None, situacao=None):
        self._id_personagem = id_personagem
        self._nome_personagem = nome_personagem
        self._nome_classe = nome_classe
        self._nome_raca = nome_raca
        self._dados_vida = dados_vida
        self._total_pontos_vida = total_pontos_vida
        self._pontos_vida_atual = pontos_vida_atual
        self._pontos_experiencia = pontos_experiencia
        self._nivel = nivel
        self._ponto_heroico = ponto_heroico
        self._situacao = situacao

    @property
    def id_personagem(self):
        return self._id_personagem

    @id_personagem.setter
    def id_personagem(self, valor):
        self._id_personagem = valor

    @property
    def nome_personagem(self):
        return self._nome_personagem

    @nome_personagem.setter
    def nome_personagem(self, valor):
        self._nome_personagem = valor

    @property
    def nome_classe(self):
        return self._nome_classe

    @nome_classe.setter
    def nome_classe(self, valor):
        self._nome_classe = valor

    @property
    def nome_raca(self):
        return self._nome_raca

    @nome_raca.setter
    def nome_raca(self, valor):
        self._nome_raca = valor

    @property
    def dados_vida(self):
        return self._dados_vida

    @dados_vida.setter
    def dados_vida(self, valor):
        self._dados_vida = valor

    @property
    def total_pontos_vida(self):
        return self._total_pontos_vida

    @total_pontos_vida.setter
    def total_pontos_vida(self, valor):
        self._total_pontos_vida = valor

    @property
    def pontos_vida_atual(self):
        return self._pontos_vida_atual

    @pontos_vida_atual.setter
    def pontos_vida_atual(self, valor):
        self._pontos_vida_atual = valor

    @property
    def pontos_experiencia(self):
        return self._pontos_experiencia

    @pontos_experiencia.setter
    def pontos_experiencia(self, valor):
        self._pontos_experiencia = valor

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, valor):
        self._nivel = valor

    @property
    def ponto_heroico(self):
        return self._ponto_heroico

    @ponto_heroico.setter
    def ponto_heroico(self, valor):
        self._ponto_heroico = valor

    @property
    def situacao(self):
        return self._situacao

    @situacao.setter
    def situacao(self, valor):
        self._situacao = valor
