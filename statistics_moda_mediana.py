import statistics 

class Lista:
    def __init__(self, elementos):
        self.elementos = elementos

    def calc_media(self):
        resultado_media = statistics.mean(self.elementos)
        print(f'Média: {resultado_media:.2f}')
        return resultado_media

    def calc_mediana(self):
        resultado_mediana = statistics.median(self.elementos)
        print(f'Mediana: {resultado_mediana:.2f}')
        return resultado_mediana
    
lista1 = Lista([14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])    
lista1.calc_media()
lista1.calc_mediana()

import statistics as st

class Lista:
    def __init__(self, elementos):
        self.elementos = elementos

    def calc_media(self):
        resultado_media = st.mean(self.elementos)
        print(f'Média: {resultado_media:.2f}')
        return resultado_media

    def calc_mediana(self):
        resultado_mediana = st.median(self.elementos)
        print(f'Mediana: {resultado_mediana:.2f}')
        return resultado_mediana

lista1 = Lista([14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

lista1.calc_media()
lista1.calc_mediana()

from statistics import mean, median

class Lista:
    def __init__(self, elementos):
        self.elementos = elementos

    def calc_media(self):
        resultado_media = mean(self.elementos)
        print(f'Média: {resultado_media:.2f}')
        return resultado_media

    def calc_mediana(self):
        resultado_mediana = median(self.elementos)
        print(f'Mediana: {resultado_mediana:.2f}')
        return resultado_mediana

lista1 = Lista([14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

lista1.calc_media()
lista1.calc_mediana()
