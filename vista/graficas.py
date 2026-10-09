

import matplotlib.pyplot as plt


class Graficas:

    def comparar_modelos(self, resultados):
        plt.figure(figsize=(10, 5))
        for nombre, (tiempo, poblacion) in resultados.items():
            plt.plot(tiempo, poblacion, label=nombre)
        plt.xlabel("Tiempo")
        plt.ylabel("Población")
        plt.title("Comparación de modelos de crecimiento poblacional")
        plt.grid(True)
        plt.legend()

        plt.show()
