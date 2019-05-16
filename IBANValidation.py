#!/usr/bin/env python3
import csv
import re
import sys

class IBAN():
    def __init__(self, file = 'Data/CountryCode_chars.csv'):
        self.filePath = file
        self.stringIntDict = {'A':10, 'B':11, 'C':12, 'D':13, 'E': 14,
                              'F':15, 'G':16, 'H':17, 'I':18, 'J': 19,
                              'K':20, 'L':21, 'M':22, 'N':23, 'O': 24,
                              'P':25, 'Q':26, 'R':27, 'S':28, 'T': 29,
                              'U':30, 'V':31, 'W':32, 'X':33, 'Y': 34,
                              'Z':35 }

    def ReadFile(self):
        with open(self.filePath, 'r') as countryCharFile:
            countryCharRaw= csv.reader(countryCharFile)
            countryCharDict = {}
            for eachRecord in countryCharRaw:
                key = eachRecord[0]
                value = eachRecord[1] ##Please note: Stored as a string.
                countryCharDict[key] = value
        return countryCharDict

    def UnformatIban(self, formatIban):
        ibanStrList = re.split(" ", formatIban)
        unformatIban = ""
        for eachIbanStr in ibanStrList:
            unformatIban += eachIbanStr
        return unformatIban

    def ValidateIban(self, ibanStr):
        countryCharMapping = self.ReadFile()
        if(' ' in ibanStr):
            ibanStr = self.UnformatIban(ibanStr)
        ibanStr = ibanStr.upper()

        ## Step 1 (of validation): Each country has different length of IBAN a.k.a Country chars match.
        countryCode = ibanStr[:2]
        try:
            expectedCountryChars = int(countryCharMapping[countryCode])
        except KeyError:
            return False
        actualCountryChars = len(ibanStr)
        if(expectedCountryChars != actualCountryChars):
            return False

        ## Step 2: Moving first 4 digits to last four.
        first4Digits = ibanStr[:4]
        ibanStr += first4Digits
        ibanStr = ibanStr[4:]

        ## Step 3: String to int conversion including country code.
        ibanIntinStr = ''
        for eachDigit in ibanStr:
            if(eachDigit in self.stringIntDict.keys()):
                ibanIntinStr += str(self.stringIntDict[eachDigit])
            else:
                ibanIntinStr += eachDigit

        ## Step 4 : Remainder check
        ibanInt = int(ibanIntinStr)
        if(ibanInt % 97 == 1):
            return True
        else:
            return False

if(__name__ == '__main__'):
    if(len(sys.argv) < 2):
        sys.exit("Please provide an IBAN to be validated while running this code in a sandboxed manner.")
    iban = IBAN()
    ibanNumberinString = ''
    for i in range(len(sys.argv)):
        if(i != 0):
            ibanNumberinString += sys.argv[i]
    iban.ValidateIban(ibanNumberinString)
