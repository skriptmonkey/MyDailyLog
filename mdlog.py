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
        '''Returns a time string in the HH:MM:SS AM/PM format.'''
        AmPm = "AM"
        self.rightNow = datetime.datetime.now()
        if self.rightNow.hour > 12:
            AmPm = "PM"
            mHour = str(self.rightNow.hour - 12)
        else:
            mHour = str(self.rightNow.hour)
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
        '''Returns a string <year>/<month.> '''
        self.rightNow = datetime.datetime.now()
        mYear = str(self.rightNow.year)
        theMonths = ["January", "February", "March", "April", "May", "June",\
                "July", "August", "September", "October", "November",\
                "December"]
        mMonth = str(self.rightNow.month) + "." +\
                theMonths[self.rightNow.month - 1]

        return mYear + "/" + mMonth

    def getLogDir(self):
        '''Returns a string for the MyDailyLog home directory.'''
        return self.MDLFolder + "/" + self.getDateString()

    def getLogFile(self):
        '''Returns a string with the full log files name.'''
        self.rightNow = datetime.datetime.now()
        return self.getLogDir() + "/%s.txt" % (self.rightNow.day)

    def checkDir(self, dirPath):
        '''Checks if a given directory (dirPath) exists, 
           if it doesn it is created'''
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)

    def newEntry(self, mEntry):
        self.checkDir(self.getLogDir())
        if os.path.isfile(self.getLogFile()):
            mLogFile = open(self.getLogFile(), 'a')
            mLogFile.write(self.getTimeString() + " " + mEntry + "\n")
            mLogFile.close()
        else:
            self.rightNow = datetime.datetime.now()
            mLogFile = open(self.getLogFile(), 'a')
            mLogFile.write(self.getDateString() + "/%s" % (self.rightNow.day))
            mLogFile.write("\n\n")
            mLogFile.write(self.getTimeString() + " " + mEntry + "\n")
            mLogFile.close()


def main():
    pass
