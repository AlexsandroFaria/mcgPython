class Monstro:
    def __init__(self, id_repositorio_monstros=None, nome_monstro=None, tipo_monstro=None, classe_armadura=None,
                 pontos_vida=None, pontos_vida_atual=None, deslocamento=None, nivel_desafio=None, referencia=None):
        self._id_repositorio_monstro = id_repositorio_monstros
        self._nome_monstro = nome_monstro
        self._tipo_monstro = tipo_monstro
        self._classe_armadura = classe_armadura
        self._pontos_vida = pontos_vida
        self._pontos_vida_atual = pontos_vida_atual
        self._deslocamento = deslocamento
        self._nivel_desafio = nivel_desafio
        self._referencia = referencia

    @property
    def id_repositorio_monstro(self):
        return self._id_repositorio_monstro

    @id_repositorio_monstro.setter
    def id_repositorio_monstro(self, valor):
        self._id_repositorio_monstro = valor

    @property
    def nome_monstro(self):
        return self._nome_monstro

    @nome_monstro.setter
    def nome_monstro(self, valor):
        self._nome_monstro = valor

    @property
    def tipo_monstro(self):
        return self._tipo_monstro

    @tipo_monstro.setter
    def tipo_monstro(self, valor):
        self._tipo_monstro = valor

    @property
    def classe_armadura(self):
        return self._classe_armadura

    @classe_armadura.setter
    def classe_armadura(self, valor):
        self._classe_armadura = valor

    @property
    def pontos_vida(self):
        return self._pontos_vida

    @pontos_vida.setter
    def pontos_vida(self, valor):
        self._pontos_vida = valor

    @property
    def pontos_vida_atual(self):
        return self._pontos_vida_atual

    @pontos_vida_atual.setter
    def pontos_vida_atual(self, valor):
        self._pontos_vida_atual = valor

    @property
    def deslocamento(self):
        return self._deslocamento

    @deslocamento.setter
    def deslocamento(self, valor):
        self._deslocamento = valor

    @property
    def nivel_desafio(self):
        return self._nivel_desafio

    @nivel_desafio.setter
    def nivel_desafio(self, valor):
        self._nivel_desafio = valor

    @property
    def referencia(self):
        return self._referencia

    @referencia.setter
    def referencia(self, valor):
        self._referencia = valor