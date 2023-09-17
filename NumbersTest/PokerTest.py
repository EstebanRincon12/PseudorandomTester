from csvReader import csvReader as cr
import scipy.stats as stats

def verifyPoker(csvPath):
    """
    Realiza una prueba de Poker para verificar si una secuencia de números en un archivo CSV sigue una distribución
    uniforme entre los dígitos 0-9. La prueba de Poker divide cada número en el archivo en cuatro grupos y determina
    la frecuencia de ocurrencia de patrones de dígitos específicos.

    Args:
        csvPath (str): La ruta al archivo CSV que contiene la secuencia de números a analizar.

    Returns:
        tuple: Una tupla que contiene los siguientes valores:
            - poker_verified (bool): True si la prueba de Poker pasa, False en caso contrario.
            - frequency_dict (dict): Un diccionario que contiene las frecuencias observadas de los patrones de dígitos D, O, T, K, F, P y Q.
            - probability_dict (dict): Un diccionario que contiene las probabilidades teóricas esperadas de los patrones de dígitos D, O, T, K, F, P y Q.
            - critical_value (float): El valor crítico de chi-cuadrado para un nivel de significancia del 0.05.
            - chi_squared_sum (float): La suma de las estadísticas de chi-cuadrado calculadas para cada patrón de dígitos.
            - chi_squared_list (list): Una lista que contiene las estadísticas de chi-cuadrado calculadas para cada patrón de dígitos.
    """
    reader = cr.getListRi(csvPath)
    frecuenceList = {"D": 0, "O": 0, "T": 0, "K": 0, "F": 0, "P": 0, "Q": 0}
    sumFrecuence = 0
    probabilityList = calculateProbabilityList(len(reader))
    
    for i in reader:
        
        i_str = str(i)  # Convierte i a cadena antes de verificar si es un dígito
        i_float = float(i_str)
        if i_float > 0 and i_float < 1:
            aux = determinateLetter(determineFrequencyNumbers(divideNumber(i_str)))
            if aux:
                frecuenceList[aux] += 1
    
    chi2 = []
    for i in probabilityList:
        chi_squared = (((probabilityList.get(i) - frecuenceList.get(i))**2) / probabilityList.get(i))
        chi2.append(chi_squared)
        sumFrecuence += chi_squared
    print(chi2)
    return verifyChiTable(sumFrecuence), frecuenceList, probabilityList, stats.chi2.ppf(0.95, 6), sumFrecuence, chi2


def verifyChiTable(number: int):
    """
    Verifies if a given chi-squared statistic is less than the critical chi-squared value
    for a significance level of 0.05 and 6 degrees of freedom.

    Args:
        number (int): The chi-squared statistic to be compared with the critical value.

    Returns:
        bool: True if the chi-squared statistic is less than the critical value, False otherwise.
    """
    if stats.chi2.ppf(0.95, 6) > number:
        return True
    else:
        return False


def calculateProbabilityList(number: int):
    """
    Calculates the expected probabilities for the Poker test based on the number of observations.

    Args:
        number (int): The number of observations (typically the sample size).

    Returns:
        dict: A dictionary containing the expected probabilities for the Poker test patterns (D, O, T, K, F, P, Q).
    """
    probabilityList = {"D": 0.3024, "O": 0.504, "T": 0.108, "K": 0.072, "F": 0.009, "P": 0.0045, "Q": 0.0001}
    for i in probabilityList:
         probabilityList.update({i:probabilityList.get(i)*number})
    return probabilityList

def divideNumber(number_str: str):
    """
    Divides a string representation of a number into a list of its decimal digits.

    Args:
        number_str (str): The string representation of the number.

    Returns:
        list: A list containing the decimal digits of the number (up to 5 digits).
    """
    result = []
    decimal_part = number_str.split('.')[1] if '.' in number_str else ""  # Divide la parte decimal del número
    decimal_part = decimal_part.split('e')[0]  # Elimina la parte en notación científica, si existe
    decimal_part = decimal_part.ljust(5, '0')  # Asegura que tenga al menos 5 dígitos, rellenando con ceros si es necesario
    for i in range(5):
        result.append(int(decimal_part[i]))
    return result


def determineFrequencyNumbers(splitNumber: list):
    """
    Determines the frequencies of repeated numbers in a list and returns them as a list of frequencies.

    Args:
        splitNumber (list): A list of decimal digits extracted from a number.

    Returns:
        list: A list containing the frequencies of repeated numbers.
    """
    result = []
    auxQuantityRepeated = 0
    for i in range(len(splitNumber)):
        repeatedNumber = []
        for j in range(i, len(splitNumber)):
            if splitNumber[i] == splitNumber[j]:
                auxQuantityRepeated = auxQuantityRepeated + 1
                repeatedNumber.append(splitNumber[i])
        if auxQuantityRepeated > 1:
            result.append(auxQuantityRepeated)
            eraseList = removeRepeatedByPosition(splitNumber, repeatedNumber)
            aux = determineFrequencyNumbers(eraseList)
            if len(eraseList) >= 0 and len(aux) > 0:
                result.append(aux[0])
        repeatedNumber.clear()
        auxQuantityRepeated = 0
    return result


def removeRepeatedByPosition(numberList: list, repeatNumberList: list):
    """
    Removes elements from a list based on their positions as specified in another list.

    Args:
        numberList (list): The original list from which elements are to be removed.
        repeatNumberList (list): A list containing elements to be removed based on their positions in the original list.

    Returns:
        list: A list with elements removed as specified.
    """
    result = numberList
    for i in repeatNumberList:
        result.remove(i)
    return result


def determinateLetter(frequencyList: list):
    """
    Determines the letter corresponding to a pattern of digit frequencies in the Poker test.

    Args:
        frequencyList (list): A list containing frequencies of repeated digits.

    Returns:
        str: A letter representing the pattern of digit frequencies (D, O, T, K, F, P, or Q).
    """
    result = ""
    if len(frequencyList) == 0:
        result = "D"
    elif len(frequencyList) == 1:
        if frequencyList[0] == 2:
            result = "O"
        elif frequencyList[0] == 3:
            result = "K"
        elif frequencyList[0] == 4:
            result = "P"
        else:
            result = "Q"
    else:
        if frequencyList[0] == 2 and frequencyList[1] == 3:
            result = "F"
        elif frequencyList[0] == 3 and frequencyList[1] == 2:
            result = "F"
        elif frequencyList[0] == 2 and frequencyList[1] == 2:
            result = "T"
    return result
