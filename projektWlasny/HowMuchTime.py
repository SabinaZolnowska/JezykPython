# -*- coding: utf-8 -*-

import datetime

class HowMuchTime:

    def __init__(self, someday=datetime.datetime(1990,01,01)):
        self.someday = someday
        self.today = datetime.datetime.now()

    def howManyYears(self):
        monthdiff = self.today.month - self.someday.month
        daydiff = self.today.day - self.someday.day
        hourdiff = self.today.hour - self.someday.hour
        minutediff = self.today.minute - self.someday.minute
        seconddiff = self.today.second - self.someday.second

        a = self.today.year - self.someday.year
        b = self.today.year - self.someday.year - 1

        if monthdiff > 0:
            return a
        if monthdiff < 0:
            return b
        if daydiff > 0:
            return a
        if daydiff < 0:
            return b
        if hourdiff > 0:
            return a
        if hourdiff < 0:
            return b
        if minutediff > 0:
            return a
        if minutediff < 0:
            return b
        if seconddiff > 0:
            return a
        if seconddiff < 0:
            return b
        return a

    def howManyMonths(self):
        monthdiff = self.today.month - self.someday.month
        daydiff = self.today.day - self.someday.day
        hourdiff = self.today.hour - self.someday.hour
        minutediff = self.today.minute - self.someday.minute
        seconddiff = self.today.second - self.someday.second

        if monthdiff >= 0:
            c = 0
        if monthdiff < 0:
            c = 12

        a = self.howManyYears()*12
        b = a + c + self.today.month - self.someday.month

        if monthdiff != 0:
            if daydiff > 0:
                return b
            if daydiff < 0:
                return b - 1
            if hourdiff > 0:
                return b
            if hourdiff < 0:
                return b - 1
            if minutediff > 0:
                return b
            if minutediff < 0:
                return b - 1
            if seconddiff > 0:
                return b
            if seconddiff < 0:
                return b - 1
        if daydiff > 0:
            return a
        if daydiff < 0:
            return a + 11
        if hourdiff > 0:
            return a
        if hourdiff < 0:
            return a + 11
        if minutediff > 0:
            return a
        if minutediff < 0:
            return a + 11
        if seconddiff > 0:
            return a
        if seconddiff < 0:
            return a + 11
        return a


    def howManyWeeks(self):
        delta = self.today - self.someday
        return int(delta.days/7)


    def howManyDays(self):
        delta = self.today - self.someday
        return delta.days

    def howManyHours(self):
        return int(self.howManySeconds()/3600)

    def howManyMinutes(self):
        return int(self.howManySeconds()/60)

    def howManySeconds(self):
        delta = self.today - self.someday
        return int(delta.total_seconds())

    def howManyMillisecond(self):
        delta = self.today - self.someday
        return int(delta.total_seconds()*1000)

    def howManyMicroseconds(self):
        delta = self.today - self.someday
        return int(delta.total_seconds()*1000000)

    def howManyNanoseconds(self):
        delta = self.today - self.someday
        return int(delta.total_seconds()*1000000000)

    def howManyPercentInTwentyFirstCentury(self):
        if self.someday > datetime.datetime(2001, 01, 01):
            return 100
        total = self.howManyDays()
        inTwentyFirstCentury = (self.today - datetime.datetime(2001, 01, 01)).days
        return round(float(inTwentyFirstCentury)/total*100,2)

    def howManyPercentInTwentyCentury(self):
        return 100-self.howManyPercentInTwentyFirstCentury()

    def howManyFebruaryTwentyNinth(self):
        if self.today.year%4 == 0:
            if self.today.month > 2:
                yeart = self.today.year
            if self.today.month < 2:
                yeart = self.today.year - 4
            if self.today.month ==2:
                if self.today.day < 29:
                    yeart = self.today.year - 4
            yeart = self.today.year
        for i in range(1,4):
            if ((self.today.year - i) % 4) == 0:
                yeart = self.today.year - i
        if self.someday.year%4 == 0:
            if self.someday.month > 2:
                years = self.someday.year + 4
            if self.someday.month < 2:
                years = self.someday.year
            if self.someday.month == 2:
                if self.someday.day <= 29:
                    years = self.someday.year
        for i in range(1,4):
            if ((self.someday.year + i) % 4) == 0:
                years = self.someday.year + i

        if years <= yeart:
            return (yeart-years)/4 + 1
        return 0

    """http://tipy.interia.pl/artykul_1420,jak-przeliczac-wiek-kota-na-wiek-czlowieka,2.html"""
    def howManyCatYears(self):
        sdays = self.howManyDays()
        #how many days in mounths
        year = 365.25
        if sdays <= year * 2:
            monthsInYear = 12.0
            humanTime = []
            catTime = []
            for i in range(1,25):
                humanTime.append(year/(monthsInYear/i))

            catTime.append(year/(monthsInYear/8))
            catTime.append(year*3 + year/(monthsInYear/4))
            catTime.append(year*5)
            catTime.append(year*6 + year/(monthsInYear/8))
            catTime.append(year*8 + year/(monthsInYear/4))
            catTime.append(year*10)
            catTime.append(year*10 + year/(monthsInYear/10))
            catTime.append(year*11 + year/(monthsInYear/8))
            catTime.append(year*12 + year/(monthsInYear/6))
            catTime.append(year*13 + year/(monthsInYear/4))
            catTime.append(year*14 + year/(monthsInYear/2))
            catTime.append(year*15)
            catTime.append(year*15 + year/(monthsInYear/10))
            catTime.append(year*16 + year/(monthsInYear/8))
            catTime.append(year*17 + year/(monthsInYear/6))
            catTime.append(year*18 + year/(monthsInYear/4))
            catTime.append(year*19 + year/(monthsInYear/2))
            catTime.append(year*20)
            catTime.append(year*20 + year/(monthsInYear/10))
            catTime.append(year*21 + year/(monthsInYear/8))
            catTime.append(year*22 + year/(monthsInYear/6))
            catTime.append(year*23 + year/(monthsInYear/4))
            catTime.append(year*24 + year/(monthsInYear/2))
            catTime.append(year*25)

            return int(self.lagrangeInterpolation(humanTime, catTime, sdays)/year)
        return int(((sdays-year*2)/year)*4 + 25)

    def lagrangeInterpolation (xs, ys, x):
        y = 0.0
        for i in range(0, len(xs)):
            t = 1.0
            for j in range(0, len(xs)):
                if i != j:
                    t=t*((x-xs[j])/(xs[i]-xs[j]))
            y = y + t*ys[i]
        return y
