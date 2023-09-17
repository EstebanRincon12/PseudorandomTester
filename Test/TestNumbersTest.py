from NumbersTest import ChiTest as CT
from NumbersTest import VarianceTest as VT
from NumbersTest import MeanTest as MT
from NumbersTest import KSTest as KST
from NumbersTest import PokerTest as PT


print("Chi cuadrado : ",CT.verifyChiTest("../RiList.csv"))
print("Varianza : ",VT.verifyVariance("../RiList.csv"))
print("Medios : ",MT.verifyMean("../RiList.csv"))
print("KS : ", KST.verifyKSTest("../RiList.csv"))
print("poker : ", PT.verifyPoker("../RiList.csv"))

