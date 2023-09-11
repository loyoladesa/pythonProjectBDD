#libmath.py

class libMath(object):
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.value = 0

    def doStoreNum1Num2(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def doAdd(self):
        self.value = self.num1 + self.num2

    def getValue(self):
        return self.value






#Empty for time being