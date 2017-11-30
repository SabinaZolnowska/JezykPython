# -*- coding: utf-8 -*-

class IntegralToRomanNumeral:
    def __init__(self, integralNumeral):
        self.integralNumeral = integralNumeral
        self.romanNumberals = {1:"I",2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX",
                               10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",
                               100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
                               1000:"M", 2000:"MM", 3000:"MMM"}
        self.romanNumberal=""

    def ifCorrectIntegral(self):
        if (isinstance(self.integralNumeral, int)):
            if(self.integralNumeral<1 or self.integralNumeral>3999):
                raise ValueError("Incorrect value")
        else:
            raise ValueError("Given value isn't integral")


    def integralToRomanNumeral(self):
        try:
            self.ifCorrectIntegral()
            listOfInt = [int(x) for x in str(self.integralNumeral)]
            for i in range(0, len(listOfInt)):
                if (listOfInt[i] * 10 ** (len(listOfInt) - i - 1)) != 0:
                    self.romanNumberal = self.romanNumberal + self.romanNumberals[
                        (listOfInt[i] * 10 ** (len(listOfInt) - i - 1))]
            return self.romanNumberal
        except ValueError as e:
            return e

