import numpy as np
from csvReader import csvReader as cr
import scipy.stats as stats

def verifyVariance(csvPath):
    reader = cr.getListRi(csvPath)
    li = stats.chi2.ppf(0.025,len(reader)-1)/(12*(len(reader)-1))
    ls = stats.chi2.ppf(0.95,len(reader)-1)/(12*(len(reader)-1))
    if li <= np.var(reader) <= ls:
        return True, li, ls, np.var(reader)
    else:
        return False, li, ls, np.var(reader)
