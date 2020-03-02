__author__="Marvin Beese"
__email__="marvin.beese@uni-potsdam.de"

import unittest
from Statistics import MathematicalAnalysis

class MyTestCase(unittest.TestCase):

    MathAna = MathematicalAnalysis.MathematicalAnalysis()
    xArr = [1,2,3,4,5,6,7,8,9,10]
    yArr = [7,5,3,2,1,1,1,1,1,1]

    def test_XMedian(self):
        assert self.MathAna.calcXMedian(self.xArr, len(self.xArr))==5.5

    def test_YMedian(self):
        assert self.MathAna.calcYMedian(self.yArr, len(self.yArr))==2.3

    def test_Sxx(self):
        assert self.MathAna.calcSxx(self.xArr, self.MathAna.calcXMedian(self.xArr, len(self.xArr)), len(self.xArr))==82.5

    def test_Sxy(self):
        # self.MathAna.linRegSlope(self.xArr, self.yArr, len(self.xArr))
        assert self.MathAna.calcSxy(self.xArr, self.yArr, self.MathAna.calcXMedian(self.xArr, len(self.xArr)), self.MathAna.calcYMedian(self.yArr,len(self.yArr)),len(self.xArr)) == -47.5

    def test_slope(self):
        assert round(self.MathAna.linRegSlope(self.xArr, self.yArr, len(self.xArr)),4)==-0.5758

    def test_Exp(self):
        assert round(self.MathAna.exponentZipf(self.xArr,self.yArr,len(self.xArr)),3)==2.737

    def test_zetaRiemann(self):
        assert round(self.MathAna.zetaRiemann(self.xArr,len(self.xArr), self.MathAna.exponentZipf(self.xArr,self.yArr, len(self.xArr))),2) == 1.25

    def test_pmf(self):
        assert round(self.MathAna.pmfZipf(3, len(self.xArr), self.xArr, self.yArr)[0], 2)==0.04


if __name__ == '__main__':
    unittest.main()
