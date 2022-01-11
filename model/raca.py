class Raca:
    def __init__(self, id_raca_personagem=None, raca=None, referencia=None ):
        self._id_raca_personegem = id_raca_personagem
        self._raca = raca
        self._referencia = referencia

    @property
    def id_raca_personagem(self):
        return self._id_raca_personegem

    @id_raca_personagem.setter
    def id_raca_personagem(self, valor):
        self._id_raca_personegem = valor

    @property
    def raca(self):
        return self._raca

    @raca.setter
    def raca(self, valor):
        self._raca = valor

    @property
    def referencia(self):
        return self._referencia

    @referencia.setter
    def referencia(self, valor):
        self._referencia = valor
