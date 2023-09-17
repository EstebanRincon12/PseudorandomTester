from csvReader import csvReader as cr
import math

ks_table = {1: 0.975, 2: 0.84189, 3: 0.7076, 4: 0.62394, 5: 0.56328, 6: 0.51926, 7: 0.48342, 8: 0.45427, 9: 0.43001,
            10: 0.40925, 11: 0.39122, 12: 0.37543, 13: 0.36143, 14: 0.3489, 15: 0.3375, 16: 0.32733, 17: 0.31796,
            18: 0.30936, 19: 0.30143, 20: 0.29408, 21: 0.28724, 22: 0.28087, 23: 0.2749, 24: 0.26931, 25: 0.26404,
            26: 0.25908, 27: 0.25438, 28: 0.24993, 29: 0.24571, 30: 0.2417, 31: 0.23788, 32: 0.23424, 33: 0.23076,
            34: 0.22743, 35: 0.22425, 36: 0.22119, 37: 0.21826, 38: 0.21544, 39: 0.21273, 40: 0.21012, 41: 0.20760,
            42: 0.20517, 43: 0.20283, 44: 0.20056, 45: 0.19837, 46: 0.19625, 47: 0.1942, 48: 0.19221, 49: 0.19028,
            50: 0.18841}


def verifyKSTest(csvPath):
    """
    Performs a Kolmogorov-Smirnov (KS) test to verify if a sequence of numbers in a CSV file
    follows a uniform distribution. This test compares the empirical cumulative distribution function (CDF)
    of the data with the expected CDF for a uniform distribution and calculates the KS statistic.

    Args:
        csvPath (str): The path to the CSV file containing the sequence of numbers to analyze.

    Returns:
        tuple: A tuple containing the following values:
            - ks_result (str): The result of the KS test as a string ("Pass" or "Fail").
            - min_value (float): The minimum value in the sequence of numbers.
            - interval_size (float): The size of each data interval.
            - quantity_by_interval (list): A list containing the count of data points in each interval.
            - expected_frequency (float): The expected frequency in each interval.
            - overall_frequency (list): A list containing the differences between the expected and observed frequencies in each interval.
            - sample_size (int): The size of the sample of data.

    """
    result = []
    reader = cr.getListRi(csvPath)

    intervalQuantity = math.ceil(math.sqrt(len(reader)))
    jump = (max(reader) - min(reader)) / intervalQuantity
    jumpExceptedFrecuency = len(reader)/intervalQuantity

    downInterval = min(reader)
    upperInterval = downInterval + jump

    quantityByInterval = []
    auxExpectedFrequency = jumpExceptedFrecuency
    overallFrequency = []
    aux = 0

    for i in range(intervalQuantity):
        for row in reader:
            if downInterval <= row <= upperInterval:
                aux = aux + 1
        quantityByInterval.append(aux)
        aux = 0
        downInterval = upperInterval
        upperInterval = downInterval + jump
        overallFrequency.append(abs((auxExpectedFrequency/len(reader)) -(sum(quantityByInterval)/len(reader))))
        auxExpectedFrequency = auxExpectedFrequency + jumpExceptedFrecuency
    return str(verifyKsTable(findValueKs(len(reader)), max(overallFrequency))) , min(reader),jump,quantityByInterval,auxExpectedFrequency,overallFrequency,len(reader)



def findValueKs(value: int):
    """
    Finds the critical value for the Kolmogorov-Smirnov (KS) test based on the specified value.

    Args:
        value (int): The integer value for which to find the KS critical value.

    Returns:
        float: The critical value for the KS test.
    """
    if value <= 50:
        return ks_table[value]
    else:
        return 1.36 / math.sqrt(value)


def verifyKsTable(ksValue: int, number: int):
    """
    Verifies if a given Kolmogorov-Smirnov (KS) statistic value is greater than a specified critical value.

    Args:
        ksValue (int): The Kolmogorov-Smirnov (KS) statistic value to be compared with the critical value.
        number (int): The critical value for the KS test.

    Returns:
        bool: True if the KS statistic value is greater than the critical value, False otherwise.

    """
    if ksValue > number:
        return True
    else:
        return False
