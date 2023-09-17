from csvReader import csvReader as cr
import math
import numpy as np
import statistics as stats


def verifyMean(csvPath):
    reader = cr.getListRi(csvPath)
    z = stats.NormalDist(mu=0, sigma=1).inv_cdf(p=(1 - (0.05 / 2)))
    li = (1 / 2) - z * (1 / math.sqrt(12 * len(reader)))
    ls = (1 / 2) + z * (1 / math.sqrt(12 * len(reader)))
    if li <= np.mean(reader) <= ls:
        return True, z ,np.mean(reader)
    else:
        return False, z ,np.mean(reader)
