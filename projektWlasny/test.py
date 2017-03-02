# -*- coding: utf-8 -*-

from freezegun import freeze_time
from HowMuchTime import HowMuchTime
import unittest
import datetime

@freeze_time("2017-02-27 19:07:30")

class TestClassHowMuchTime(unittest.TestCase):

    def setUp(self):
        self.someday = datetime.datetime(2016, 02, 25, 1, 0)
        self.someday2 = datetime.datetime(2000, 01, 01)
        self.someday3 = datetime.datetime(2007, 10, 11)
        self.someday4 = datetime.datetime(2016, 2, 27, 19, 7, 31)
        self.someday5 = datetime.datetime(2006, 2, 27, 19, 6, 30)
        self.someday6 = datetime.datetime(2003, 2, 27, 20, 7, 30)
        self.someday7 = datetime.datetime(1995, 2, 27, 19, 7, 29)
        self.someday8 = datetime.datetime(1981, 2, 27, 19, 6, 30)
        self.someday9 = datetime.datetime(1979, 2, 27, 18, 7, 30)
        self.someday10 = datetime.datetime(2017, 2, 26, 19)
        self.someday11 = datetime.datetime(2017, 2, 26, 20)
        self.someday12 = datetime.datetime(2004, 2, 29)

    def test__init__(self):
        self.assertEqual(HowMuchTime(self.someday).today, datetime.datetime(2017, 02, 27, 19, 7, 30))
        self.assertEqual(HowMuchTime(self.someday).someday, self.someday)
        self.assertEqual(HowMuchTime(self.someday2).today, datetime.datetime(2017, 2, 27, 19, 7, 30))
        self.assertEqual(HowMuchTime(self.someday2).someday, datetime.datetime(2000, 1, 1))

    def testHowManyYears(self):
        self.assertEqual(HowMuchTime(self.someday).howManyYears(), 1)
        self.assertEqual(HowMuchTime(self.someday2).howManyYears(), 17)
        self.assertEqual(HowMuchTime(self.someday3).howManyYears(), 9)
        self.assertEqual(HowMuchTime(self.someday4).howManyYears(), 0)
        self.assertEqual(HowMuchTime(self.someday5).howManyYears(), 11)
        self.assertEqual(HowMuchTime(self.someday6).howManyYears(), 13)
        self.assertEqual(HowMuchTime(self.someday7).howManyYears(), 22)
        self.assertEqual(HowMuchTime(self.someday8).howManyYears(), 36)
        self.assertEqual(HowMuchTime(self.someday9).howManyYears(), 38)
        self.assertEqual(HowMuchTime(self.someday10).howManyYears(), 0)
        self.assertEqual(HowMuchTime(self.someday11).howManyYears(), 0)
        self.assertEqual(HowMuchTime(self.someday12).howManyYears(), 12)

    def testHowManyMonths(self):
        self.assertEqual(HowMuchTime(self.someday).howManyMonths(), 12)
        self.assertEqual(HowMuchTime(self.someday2).howManyMonths(), 205)
        self.assertEqual(HowMuchTime(self.someday3).howManyMonths(), 112)
        self.assertEqual(HowMuchTime(self.someday4).howManyMonths(), 11)
        self.assertEqual(HowMuchTime(self.someday5).howManyMonths(), 132)
        self.assertEqual(HowMuchTime(self.someday6).howManyMonths(), 167)
        self.assertEqual(HowMuchTime(self.someday7).howManyMonths(), 264)
        self.assertEqual(HowMuchTime(self.someday8).howManyMonths(), 432)
        self.assertEqual(HowMuchTime(self.someday9).howManyMonths(), 456)
        self.assertEqual(HowMuchTime(self.someday10).howManyMonths(), 0)
        self.assertEqual(HowMuchTime(self.someday11).howManyMonths(), 0)
        self.assertEqual(HowMuchTime(self.someday12).howManyMonths(), 155)

    def testHowManyWeeks(self):
        self.assertEqual(HowMuchTime(self.someday).howManyWeeks(), 52)
        self.assertEqual(HowMuchTime(self.someday2).howManyWeeks(), 895)
        self.assertEqual(HowMuchTime(self.someday3).howManyWeeks(), 489)
        self.assertEqual(HowMuchTime(self.someday4).howManyWeeks(), 52)
        self.assertEqual(HowMuchTime(self.someday5).howManyWeeks(), 574)
        self.assertEqual(HowMuchTime(self.someday6).howManyWeeks(), 730)
        self.assertEqual(HowMuchTime(self.someday7).howManyWeeks(), 1148)
        self.assertEqual(HowMuchTime(self.someday8).howManyWeeks(), 1878)
        self.assertEqual(HowMuchTime(self.someday9).howManyWeeks(), 1982)
        self.assertEqual(HowMuchTime(self.someday10).howManyWeeks(), 0)
        self.assertEqual(HowMuchTime(self.someday11).howManyWeeks(), 0)
        self.assertEqual(HowMuchTime(self.someday12).howManyWeeks(), 678)

    def testHowManyDays(self):
        self.assertEqual(HowMuchTime(self.someday).howManyDays(), 368)
        self.assertEqual(HowMuchTime(self.someday2).howManyDays(), 6267)
        self.assertEqual(HowMuchTime(self.someday3).howManyDays(), 3427)
        self.assertEqual(HowMuchTime(self.someday4).howManyDays(), 365)
        self.assertEqual(HowMuchTime(self.someday5).howManyDays(), 4018)
        self.assertEqual(HowMuchTime(self.someday6).howManyDays(), 5113)
        self.assertEqual(HowMuchTime(self.someday7).howManyDays(), 8036)
        self.assertEqual(HowMuchTime(self.someday8).howManyDays(), 13149)
        self.assertEqual(HowMuchTime(self.someday9).howManyDays(), 13880)
        self.assertEqual(HowMuchTime(self.someday10).howManyDays(), 1)
        self.assertEqual(HowMuchTime(self.someday11).howManyDays(), 0)
        self.assertEqual(HowMuchTime(self.someday12).howManyDays(), 4747)

    def testHowManyHours(self):
        pass

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()