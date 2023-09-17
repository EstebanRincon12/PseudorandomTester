from csvReader import csvReader as cr
import math
import numpy as np
import statistics as stats


def verifyMean(csvPath):
    """
    Verifica si la media de una secuencia de números en un archivo CSV se encuentra dentro de un intervalo de confianza
    dado para una distribución normal estándar. La verificación se realiza con un nivel de significancia del 0.05.

    Args:
        csvPath (str): La ruta al archivo CSV que contiene la secuencia de números a analizar.

    Returns:
        tuple: Una tupla que contiene los siguientes valores:
            - mean_verified (bool): True si la media se encuentra dentro del intervalo de confianza, False en caso contrario.
            - z_value (float): El valor crítico Z para un nivel de significancia del 0.05/2 (dos colas).
            - sample_mean (float): La media de la secuencia de números en el archivo CSV.
    """

    reader = cr.getListRi(csvPath)
    z = stats.NormalDist(mu=0, sigma=1).inv_cdf(p=(1 - (0.05 / 2)))
    li = (1 / 2) - z * (1 / math.sqrt(12 * len(reader)))
    ls = (1 / 2) + z * (1 / math.sqrt(12 * len(reader)))
    if li <= np.mean(reader) <= ls:
        return True, z ,np.mean(reader)
    else:
        return False, z ,np.mean(reader)
