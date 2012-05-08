#!/usr/bin/python

#################################################################
# MyDailyLog
# Author: Alvin D. Morris
# email: alvin.morris@gmail.com
#
# Command line utility for keeping track of daily productivity.
#################################################################

import os
import datetime

class MyDailyLog:
    def __init__(self):
        self.MDLFolder = os.getenv("HOME") + "/Dropbox/MyDailyLog"
        self.rightNow = 0
        self.MDLDir = ""
        self.MDLFile = ""

    def getTimeString(self):
        AmPm = "AM"
        self.rightNow = datetime.datetime.now()
        if self.rightNow.hour > 12:
            AmPm = "PM"
            mHour = str(self.rightNow.hour - 12)
        if mHour < 10:
            mhour = "0" + str(mHour)
        if self.rightNow.minute < 10:
            mMinute = "0" + str(self.rightNow.minute)
        else:
            mMinute = str(self.rightNow.minute)
        if self.rightNow.second < 10:
            mSecond = "0" + str(self.rightNow.second)
        else:
            mSecond = str(self.rightNow.second)

        return mHour + ":" + mMinute + ":" + mSecond + " " + AmPm

    def getDateString(self):
        self.rightNow = datetime.datetime.now()
        mYear = str(self.rightNow.year)
        theMonths = ["January", "February", "March", "April", "May", "June",\
                "July", "August", "September", "October", "November",\
                "December"]
        mMonth = str(self.rightNow.month) + "." +\
                theMonths[self.rightNow.month - 1]

        return mYear + "/" + mMonth

    def getLogDir(self):
        return self.MDLFolder + "/" + self.getDateString()

    def getLogFile(self):
        self.rightNow = datetime.datetime.now()
        return self.getLogDir() + "/%s.txt" % (self.rightNow.day)

    def checkDir(self, dirPath):
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)

    def newEntry(self, mEntry):
        pass


def main():
    pass
