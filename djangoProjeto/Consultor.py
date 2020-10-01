import pandas as pd

class Consultor:

    def __init__(self, nome):
        self.nome = nome

    def corr(self, ma, mb):
        cor = ma * mb
        return cor
