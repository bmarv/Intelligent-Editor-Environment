__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

"""Mathematical Analysis of the given file. Includes the linear Regression Analysis for the Slope of the Distribution,
    the calculation of the zipfian exponent, the zipfian probability mass function, the estimated occurrences
    and the deviation of the estimated to the real occurrences.
    All relevant methods have been tested using PyTest
    Every methods is calculated from scratch without the use of any additional libraries or modules
"""
class MathematicalAnalysis:
    def __init__(self):
        pass

    "calculates the Median over all values x in xArr until max is reached"
    "returns Median value"
    # (\sum_{i=0}^{n=max-1}{x_i})/n
    def calcXMedian(self, xArr, max):
        xSum=0
        for i in range(max):
            xSum+=xArr[i]
        xMedian=xSum/max
        print("\txMedian: ", xMedian)
        return xMedian

    # (\sum_{i=0}^{n=max-1}{y_i})/n
    def calcYMedian(self, yArr, max):
        ySum=0
        for i in range(max):
            ySum+=yArr[i]
        yMedian=ySum/max
        print("\tyMedian: ",yMedian)
        return yMedian

    "calculates the average square of deviation"
    # \sum_{i=0}^{n=max-1}{x_i - xMed}^2
    def calcSxx(self, xArr, xMed, max):
        Sxx=0
        for i in range(max):
            Sxx+= (xArr[i]-xMed)**2
        print("\tSxx: ",Sxx)
        return Sxx

    # not used
    # \sum_{i=0}^{n=max-1}{y_i - yMed}^2
    def calcSyy(self, yArr, yMed, max):
        Syy=0
        for i in range (max):
            Syy+=(yArr[i]-yMed)**2
        print("\tSyy: ",Syy)
        return Syy

    "calculates the product of the x- and y-Deviation"
    # \sum_{i=0}^{n=max-1}{x_i - xMed}*{y_i - yMed}
    def calcSxy(self, xArr, yArr, xMed, yMed, max):
        Sxy=0
        for i in range(max):
            Sxy+=(xArr[i]-xMed)*(yArr[i]-yMed)
        print("\tSxy: ",Sxy)
        return Sxy

    "calculates Slope of Distribution using linear Regression"
    # \frac{Sxy}{Sxx}
    def linRegSlope(self, xArr, yArr, max):
        xMed = self.calcXMedian(xArr, max)
        yMed = self.calcYMedian(yArr, max)
        Sxy = self.calcSxy(xArr, yArr, xMed, yMed, max)
        Sxx = self.calcSxx(xArr, xMed, max)
        slope = Sxy / Sxx
        print("slope: ", slope)
        print("\t{0}/{1}={2}".format(Sxy, Sxx, slope))
        return slope

    "calculates the exponent of the Distribution"
    # exp= 1+ \frac{1}{|m|} //m = linRegSlope() //Exponent der Verteilungsfunktion
    def exponentZipf(self, xArr, yArr, max):
        m = self.linRegSlope(xArr, yArr, max)
        exp = 1+ (1/ abs(m))
        print("expZipf: ",exp)
        print("\t1+(1/{0}) = {1}".format(abs(m),exp))
        return exp

    "calculates the normalized frequency of elements of rank k / Probability Mass Function of Zipf-Function"
    # pmf(k;s,N) = \frac{1}{k^s * H_{N,s}}
    # Rank k >=1, Exponent of Zipf-Distribution (shape parameter) s>1,
    def pmfZipf(self, k, N, xArr, yArr):
        if(k>N):
            return "0%"
        s = self.exponentZipf(xArr, yArr, N)
        H = self.zetaRiemann(xArr, N, s)
        pmf = 1/((k**s)*H)
        pmfPercentage= str(pmf*100)[:5],"%"
        print("pmfZipf: ",pmf)
        print("\t 1/(({0}^{1})*{2})".format(k,s,H))
        return pmf, pmfPercentage

    "calculates Riemanns Zeta-Function over all given Ranks"
    # H_{N,s}= \sum_{n=1}^{N}(frac{1}{n^s}) //Riemanns Zeta-Function
    def zetaRiemann(self, xArr, N, s):
        H=0
        for n in xArr:
            H += (1/n**s)
        print("zetaRiemann: ",H)
        return H

    "calculate the estimated occurrences for the given rank and percentage"
    # estOcc(wordLimit, percentage)_{rank} = wordLimit \cdot percentage
    def estOccurrences(self, rank, wordLimit, percentage):
        estOcc = wordLimit * percentage
        print("estOcc for rank {0}: {1}".format(rank, estOcc))
        return rank, estOcc

    "says whether the deviation is 'zipfy' or not / deviation of real to estimated occurrences"
    # deviation(rank, real, est, wordLimit) = |real-est|/wordLimit < 0,10    //<10% is a random argument for ziphy
    def estToRealOccurrences(self, rank, realOcc, estOcc, wordLimit):
        deviation = abs(realOcc-estOcc) /wordLimit
        deviationPercentage = str(deviation * 100)[:5], "%"
        if(deviation<0.10):
            print("deviation: ",deviation," pretty zipfy")
            return deviation, deviationPercentage, "pretty zipfy"
        else:
            print("deviation: ", deviation, " not really zipfy")
            return deviation, deviationPercentage, "not really zipfy"