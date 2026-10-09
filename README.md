# Práctica 02 - Comparación de modelos determinísticos, estocásticos, discretos y continuos

| Dato | Detalle |
|---|---|
| Universidad | Universidad Nacional de Loja - FEIRNNR, Carrera de Computación |
| Asignatura | Simulación (Ciclo 5) |
| Unidad | U1: Introducción a la Simulación |
| Docente | José O. Guamán Q. |
| Estudiante | María Soledad Buri Camacho |
| Sistema operativo | Linux (Ubuntu / Debian) |

## 1. Descripción

El programa implementa cuatro modelos de crecimiento poblacional y los compara en una sola gráfica:

| Modelo | Tipo | Ecuación |
|---|---|---|
| Determinístico | Sin aleatoriedad | `P(t) = P0 · e^(r·t)` |
| Discreto | Cambia por períodos | `P(t+1) = P(t) + r·P(t)` |
| Estocástico | Con aleatoriedad | `P(t+1) = P(t) + r·P(t) + ε`, con `ε ~ N(0, σ²)` |
| Continuo (Euler) | Aproximación numérica | `P(t+Δt) = P(t) + Δt·(r·P(t))` |

Donde:

- **P0**: población inicial.
- **r**: tasa de crecimiento.
- **σ (sigma)**: nivel de variabilidad (ruido) del modelo estocástico.
- **Δt (dt)**: tamaño del paso del modelo continuo.
- **t**: tiempo (períodos).

En el modelo estocástico, si la nueva población resulta negativa se deja en 0.

### Datos de entrada

El arreglo de entrada de la guía es:

```python
DATOS = [1000, 1100, 1250, 1400, 1600, 1850, 2100]
```

A partir de este arreglo el programa obtiene los parámetros:

- **P0** = primer valor del arreglo (1000).
- **tiempo** = número de períodos = cantidad de datos − 1 (6).
- **r** = promedio del crecimiento relativo de cada período, es decir, el promedio de `(P(i+1) − P(i)) / P(i)` (resulta 0.1318).

Si se cambia el arreglo en `datos/datos_poblacion.py`, los parámetros se recalculan solos. Los otros parámetros (`SIGMA`, `DT` y `SEMILLA`) están en el mismo archivo.

- `SIGMA = 50`: nivel de aleatoriedad.
- `DT = 0.1`: paso del modelo continuo.
- `SEMILLA = 42`: hace que el modelo estocástico dé siempre el mismo resultado. Si se cambia por `None`, el resultado cambia en cada ejecución.

## 2. Estructura del proyecto

```
practica02_simulacion/
├── main.py                          # Punto de entrada: conecta las capas
├── requirements.txt                 # Dependencias
├── README.md
├── .gitignore
├── datos/
│   └── datos_poblacion.py           # CAPA DE DATOS: arreglo de entrada, sigma, dt, semilla
├── logica/
│   ├── parametros.py                # Calcula P0, r y tiempo a partir del arreglo
│   ├── modelo_deterministico.py     # Función modelo_deterministico
│   ├── modelo_discreto.py           # Función modelo_discreto
│   ├── modelo_estocastico.py        # Función modelo_estocastico
│   └── modelo_continuo.py           # Función modelo_continuo (Euler)
└── vista/
    ├── consola.py                   # Parámetros en consola
    └── graficas.py                  # Gráfica comparativa con Matplotlib
```

Cada modelo está en su propio archivo y recibe sus parámetros (`p0`, `r`, `tiempo`, y según el caso `sigma`, `dt` o `semilla`). Devuelve el vector de tiempo y la lista de población.

- La capa de **datos** no depende de ninguna otra.
- La capa de **lógica** no imprime ni grafica nada.
- La capa de **vista** solo muestra resultados.
- `main.py` es el único archivo que conoce las tres capas.

## 3. Requisitos previos

Esta práctica se ejecuta en **Linux (Ubuntu / Debian)**. Se necesitan estos paquetes del sistema:

- `python3` (3.9 o superior)
- `python3-venv` (para crear el entorno virtual)
- `python3-pip`
- `python3-tk` (para que se abra la ventana de la gráfica)
- `git` (para clonar el repositorio)

Instalarlos (pide la contraseña de usuario):

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip python3-tk git
```

Verificar la versión de Python:

```bash
python3 --version
```

Debe mostrar `Python 3.9` o superior.

## 4. Instalación y ejecución (paso a paso)

Todos los comandos se ejecutan en una terminal de Linux.

### Paso 1. Obtener el proyecto

```bash
git clone <URL-DEL-REPOSITORIO>
cd practica02_simulacion
```

(Reemplazar `<URL-DEL-REPOSITORIO>` por la dirección del repositorio. Si se descargó un ZIP, descomprimirlo con `unzip practica02_simulacion.zip` y entrar con `cd practica02_simulacion`.)

A partir de aquí **todos los comandos se ejecutan dentro de la carpeta `practica02_simulacion`**, donde están `main.py` y `requirements.txt`. Para comprobarlo:

```bash
ls
```

Debe mostrar: `datos  logica  main.py  README.md  requirements.txt  vista`

### Paso 2. Crear el entorno virtual

```bash
python3 -m venv venv
```

Esto crea una carpeta llamada `venv`.

### Paso 3. Activar el entorno virtual

```bash
source venv/bin/activate
```

Cuando está activo, la terminal muestra `(venv)` al inicio de la línea.

### Paso 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Esto instala NumPy y Matplotlib. Debe terminar con un mensaje como `Successfully installed ...`.

### Paso 5. Ejecutar el programa

```bash
python main.py
```

### Paso 6. Qué se espera ver

1. En la terminal se imprimen los parámetros de la simulación:

```
PARAMETROS DE LA SIMULACION
----------------------------------------
P0 (poblacion inicial)  : 1000
r (tasa de crecimiento) : 0.1318
sigma (aleatoriedad)    : 50
dt (paso de Euler)      : 0.1
tiempo (periodos)       : 6
----------------------------------------
```

2. Se abre **una ventana con una sola gráfica** que compara los cuatro modelos (Tiempo en el eje X y Población en el eje Y). Con la configuración por defecto, la población en el período 6 es aproximadamente:

| Modelo | Población en t = 6 |
|---|---|
| Determinístico | 2204.7 |
| Discreto | 2101.6 |
| Estocástico (semilla 42) | 2255.9 |
| Continuo (Euler) | 2193.4 |

3. Para terminar el programa, cerrar la ventana de la gráfica.

### Paso 7. Desactivar el entorno virtual (opcional)

```bash
deactivate
```

