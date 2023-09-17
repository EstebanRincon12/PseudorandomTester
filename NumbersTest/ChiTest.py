from csvReader import csvReader as cr
import math
import scipy.stats as stats


def verifyChiTest(csvPath):
    reader = cr.getListRi(csvPath)

    intervalQuantity = math.ceil(math.sqrt(len(reader)))
    jump = (max(reader) - min(reader)) / intervalQuantity
    frequency = len(reader) / intervalQuantity
    listGetFrecuency =[]
    downInterval = min(reader)
    upperInterval = downInterval + jump

    overallFrequency = 0
    aux = 0

    for i in range(intervalQuantity):
        for row in reader:
            if downInterval <= row <= upperInterval:
                aux = aux + 1
        listGetFrecuency.append(aux)
        auxQuantityByInterval = aux
        aux = 0
        downInterval = upperInterval
        upperInterval = downInterval + jump
        overallFrequency = overallFrequency + (((auxQuantityByInterval - frequency) ** 2) / frequency)
    return verifyChiTable((intervalQuantity - 1), overallFrequency), min(reader),jump,intervalQuantity,listGetFrecuency,overallFrequency,stats.chi2.ppf(0.95, intervalQuantity - 1)


def verifyChiTable(degrees_of_freedom: int, number: int):
    if stats.chi2.ppf(0.95, degrees_of_freedom) > number:
        return True
    else:
        return False
