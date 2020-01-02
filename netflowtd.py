#!/usr/bin/env python
import time
import sys

def printHelp():
    print "Usage : python netflowtd.py <TD>"
    print "\t<TD>: Date Firsteen Duration"
    print "\t\te.g.: python netflowtd.py 2020-01-01 23:00:05.000   897.000"

def main(argv):
    try:
        if len(argv) == 3:
            SD="%s_%s" %(argv[0],argv[1][:-4])
            STARTDATE=time.mktime(time.strptime(SD, '%Y-%m-%d_%H:%M:%S'))
            ENDDATE=int(STARTDATE)+int(argv[2][:-4])
            print "--- TIME WINDOWS ---"
            print time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(STARTDATE))
            print time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(ENDDATE))
        else:
            printHelp()

    except:
        printHelp()

if __name__ == "__main__":
    main(sys.argv[1:])

