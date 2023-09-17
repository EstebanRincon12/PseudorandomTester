from NumbersTest import PokerTest as PT

def individualTest():
    print("1",PT.determineFrequencyNumbers(PT.divideNumber("0.73435")))
    print("2",PT.determineFrequencyNumbers(PT.divideNumber("0.22678")))
    print("3",PT.determineFrequencyNumbers(PT.divideNumber("0.26279")))
    print("4",PT.determineFrequencyNumbers(PT.divideNumber("0.25628")))
    print("5",PT.determineFrequencyNumbers(PT.divideNumber("0.26742")))
    print("6",PT.determineFrequencyNumbers(PT.divideNumber("0.14444")))
    print("7",PT.determineFrequencyNumbers(PT.divideNumber("0.22441")))
    print("8",PT.determineFrequencyNumbers(PT.divideNumber("0.12244")))
    print("9",PT.determineFrequencyNumbers(PT.divideNumber("0.88888")))
    print("10",PT.determineFrequencyNumbers(PT.divideNumber("0.12345")))

individualTest()

import numpy as np

# Generar 50 datos pseudoaleatorios entre 0 y 1
datos = np.random.uniform(0, 1, 50)

# Asignar un valor constante a los primeros 25 elementos
datos[:25] = 0.5

# Imprimir la varianza de los datos
print(datos)