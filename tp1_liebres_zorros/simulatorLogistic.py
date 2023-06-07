import numpy as np
import matplotlib.pyplot as plt


class Simulator:
    def __init__(self, liebres=500, zorros=100, semanas=600, tasa_natalidad_liebres=0.08,
                 tasa_mortandad_liebres=0.002, tasa_mortandad_zorros=0.2, tasa_natalidad_zorros=0.0004, dt=1, tiempo_inicial=1, K=1000):
        self.liebres = liebres
        self.zorros = zorros
        self.semanas = semanas
        self.tasa_natalidad_liebres = tasa_natalidad_liebres
        self.tasa_mortandad_liebres = tasa_mortandad_liebres
        self.tasa_mortandad_zorros = tasa_mortandad_zorros
        self.tasa_natalidad_zorros = tasa_natalidad_zorros
        self.dt = dt
        self.tiempo_inicial = tiempo_inicial
        self.K = K

    def calc_prey_variation(self):
        # calculo de variacion poblacional liebres
        # return ((self.tasa_natalidad_liebres * self.liebres) - (self.tasa_mortandad_liebres * self.liebres * self.zorros)) * self.dt
        variation = ((self.tasa_natalidad_liebres * self.liebres * (1 - (self.liebres / self.K))) - (self.tasa_mortandad_liebres * self.liebres * self.zorros)) * self.dt
        """if variation < 0:
            return 0"""
        print("prey",variation)
        return variation

    def calc_predator_variation(self):
        # calculo de variacion poblacional zorros
        variation = ((self.tasa_natalidad_zorros * self.liebres * self.zorros) - (self.tasa_mortandad_zorros * self.zorros)) * self.dt
        """if variation < 0:
            return 0"""
        print("pred",variation)
        return variation

    def simulation(self):
        presas_arr = [self.liebres]
        predadores_arr = [self.zorros]
        tiempo_arr = [self.tiempo_inicial]

        tiempo = self.tiempo_inicial

        for i in range(self.semanas - 1):
            tiempo = tiempo + self.dt
            self.liebres += self.calc_prey_variation()
            self.zorros += self.calc_predator_variation()
            presas_arr.append(self.liebres)
            predadores_arr.append(self.zorros)
            tiempo_arr.append(tiempo)

        return np.array(presas_arr), np.array(predadores_arr), np.array(tiempo_arr)
    # Funcion para graficar la densidad y el diagrama de fases del modelo

    def plot_graphs(self,liebres_array, zorros_array, tiempo_array):
        plt.plot(tiempo_array,
                 liebres_array,
                 label="Liebres")
        plt.plot(tiempo_array,
                 zorros_array,
                 label="Zorros")
        plt.title('Densidad poblacional de liebres y zorros.')
        plt.xlabel('Semanas')
        plt.xticks(rotation='horizontal')
        plt.legend()
        plt.ylabel('Densidad poblacional')

        plt.show()

        plt.plot(zorros_array,
                 liebres_array)
        plt.title('Diagrama de fases poblacional')
        plt.xlabel('Zorros')
        plt.xticks(rotation='vertical')
        plt.ylabel('Liebres')
        plt.show()
