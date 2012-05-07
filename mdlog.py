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
        self.rightNow = datetime.datetime.now()

    def getTimeString(self):
        timeString = self.rightNow.hour + ":" + self.rightNow.minute + ":"\
               + self.rightNow.second
        return timeString

    def getDateString(self):
        mYear = self.rightNow.year
        
        theMonths = ["January", "February", "March", "April", "May", "June",\
                "July", "August", "September", "October", "November",\
                "December"]
        mMonth = self.rightNow.month + " - " + theMonths[self.rightNow.month]

        mDay = self.rightNow.day

        return mYear + "/" + mMonth + "/" + mDay



    def checkDir(self, dirPath):
        if not os.path.isdir(dirPath):
            os.makedirs(dirPath)

def main():
    pass
