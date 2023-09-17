import numpy as np
from csvReader import csvReader as cr
import scipy.stats as stats

def verifyVariance(csvPath):
    """
    Verifies if the variance of a sequence of numbers in a CSV file falls within a confidence interval.
    This function performs a variance test with a 95% confidence level using the chi-squared distribution.

    Args:
        csvPath (str): The path to the CSV file containing the sequence of numbers to analyze.

    Returns:
        tuple: A tuple containing the following values:
            - variance_verified (bool): True if the variance falls within the confidence interval, False otherwise.
            - lower_interval (float): The lower bound of the confidence interval for the variance.
            - upper_interval (float): The upper bound of the confidence interval for the variance.
            - sample_variance (float): The calculated variance of the sequence of numbers.
    """
    reader = cr.getListRi(csvPath)
    li = stats.chi2.ppf(0.025,len(reader)-1)/(12*(len(reader)-1))
    ls = stats.chi2.ppf(0.95,len(reader)-1)/(12*(len(reader)-1))
    if li <= np.var(reader) <= ls:
        return True, li, ls, np.var(reader)
    else:
        return False, li, ls, np.var(reader)
