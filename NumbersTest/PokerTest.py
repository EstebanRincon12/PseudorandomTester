from csvReader import csvReader as cr
import scipy.stats as stats

def verifyPoker(csvPath):
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
    if stats.chi2.ppf(0.95, 6) > number:
        return True
    else:
        return False


def calculateProbabilityList(number: int):
    probabilityList = {"D": 0.3024, "O": 0.504, "T": 0.108, "K": 0.072, "F": 0.009, "P": 0.0045, "Q": 0.0001}
    for i in probabilityList:
         probabilityList.update({i:probabilityList.get(i)*number})
    return probabilityList

def divideNumber(number_str: str):
    result = []
    decimal_part = number_str.split('.')[1] if '.' in number_str else ""  # Divide la parte decimal del número
    decimal_part = decimal_part.split('e')[0]  # Elimina la parte en notación científica, si existe
    decimal_part = decimal_part.ljust(5, '0')  # Asegura que tenga al menos 5 dígitos, rellenando con ceros si es necesario
    for i in range(5):
        result.append(int(decimal_part[i]))
    return result


def determineFrequencyNumbers(splitNumber: list):
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
    result = numberList
    for i in repeatNumberList:
        result.remove(i)
    return result


def determinateLetter(frequencyList: list):
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
