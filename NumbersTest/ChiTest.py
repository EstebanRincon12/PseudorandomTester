from csvReader import csvReader as cr
import math
import scipy.stats as stats


def verifyChiTest(csvPath):
    """
    Performs a chi-squared test to verify if a sequence of numbers in a CSV file follows a uniform distribution.
    This test compares the observed frequencies to the expected frequencies in data intervals and calculates the chi-squared statistic.

    Args:
        csvPath (str): The path to the CSV file containing the sequence of numbers to analyze.

    Returns:
        tuple: A tuple containing the following values:
            - p_value (float): The p-value calculated from the chi-squared statistic.
            - min_value (float): The minimum value in the sequence of numbers.
            - interval_size (float): The size of each data interval.
            - interval_quantity (int): The number of intervals used in the test.
            - observed_frequencies (list): A list containing the observed frequencies in each interval.
            - chi_squared_statistic (float): The calculated chi-squared statistic.
            - critical_value (float): The critical chi-squared value for a significance level of 0.05.

    """
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
    """
    Verifies if a given chi-squared statistic is less than the critical chi-squared value
    for a specified degrees of freedom and a significance level of 0.05.

    Args:
        degrees_of_freedom (int): The degrees of freedom for the chi-squared distribution.
        number (int): The chi-squared statistic to be compared with the critical value.

    Returns:
        bool: True if the chi-squared statistic is less than the critical value, False otherwise.
    """
    if stats.chi2.ppf(0.95, degrees_of_freedom) > number:
        return True
    else:
        return False
