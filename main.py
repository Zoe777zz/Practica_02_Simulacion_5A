
from datos.datos_poblacion import DATOS, DT, SEMILLA, SIGMA
from logica.modelo_continuo import modelo_continuo
from logica.modelo_deterministico import modelo_deterministico
from logica.modelo_discreto import modelo_discreto
from logica.modelo_estocastico import modelo_estocastico
from logica.parametros import calcular_parametros
from vista.consola import mostrar_parametros
from vista.graficas import Graficas


def main():
    # Logica
    parametros = calcular_parametros(DATOS, SIGMA, DT, SEMILLA)
    p0 = parametros["p0"]
    r = parametros["r"]
    sigma = parametros["sigma"]
    dt = parametros["dt"]
    tiempo = parametros["tiempo"]
    semilla = parametros["semilla"]

    resultados = {
        "Determinístico": modelo_deterministico(p0, r, tiempo),
        "Discreto": modelo_discreto(p0, r, tiempo),
        "Estocástico": modelo_estocastico(p0, r, sigma, tiempo, semilla),
        "Continuo (Euler)": modelo_continuo(p0, r, tiempo, dt),
    }

    # Vista
    mostrar_parametros(parametros)
    Graficas().comparar_modelos(resultados)


if __name__ == "__main__":
    main()
