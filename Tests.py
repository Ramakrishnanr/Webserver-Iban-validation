#!/usr/bin/env python3
import unittest
import IBANValidation
import urllib.request as webRequest
import sys

## Please note: 
## Prerequisite for running this test (especially for the class TestIbanValidation_WithWebServer) :  web server should be listening at the port 80 in localhost.

class TestIbanValidation_Standalone(unittest.TestCase):
    def setUp(self):
        self.ibanObject = IBANValidation.IBAN()

    def test_validIban_with_spaces(self):
        ibanStr = 'RO09 BCYP 0000 0012 3456 7890'
        actualIbanFlag = self.ibanObject.ValidateIban(ibanStr)
        expectedIbanFlag = True
        self.assertEqual(actualIbanFlag, expectedIbanFlag)

    def test_invalidIban(self):
        ibanStr = 'RO09 BCYP 0000 0012 3456 789000'
        actualIbanFlag = self.ibanObject.ValidateIban(ibanStr)
        expectedIbanFlag = False
        self.assertEqual(actualIbanFlag, expectedIbanFlag)

    def test_validIban_without_spaces(self):
        ibanStr = 'FR7630006000011234567890189'
        actualIbanFlag = self.ibanObject.ValidateIban(ibanStr)
        expectedIbanFlag = True
        self.assertEqual(actualIbanFlag, expectedIbanFlag)

    def test_Iban_lower_case(self):
        ibanStr = 'ro09bcyp0000001234567890'
        actualIbanFlag = self.ibanObject.ValidateIban(ibanStr)
        expectedIbanFalg = True
        self.assertEqual(actualIbanFlag, expectedIbanFalg)


class TestIbanValidation_WithWebServer(unittest.TestCase):
    def setUp(self):
        self.host = host
        self.port = '80'
        self.urlFormat = 'http://'
        self.url = self.urlFormat + self.host + ':' + self.port + '/'

    def GetActualOutput(self, url):
        response = webRequest.urlopen(url)
        actualOutputInBytes = response.read()
        actualOutput = actualOutputInBytes.decode('utf-8')
        return actualOutput

    def test_validIban_with_spaces(self):
        correctSubURL = 'IBAN/'
        ibanStr = 'RO09 BCYP 0000 0012 3456 7890'
        url = self.url + correctSubURL + ibanStr
        expectedOutput = 'You sent a valid IBAN\n'
        actualOutput = self.GetActualOutput(url)
        self.assertEqual(actualOutput, expectedOutput)

    def test_invalidIban(self):
        correctSubURL = 'IBAN/'
        ibanStr = 'RO09 BCYP 0000 0012 3456 789000'
        url = self.url+ correctSubURL + ibanStr
        expectedOutput = 'You sent an invalid IBAN\n'
        actualOutput = self.GetActualOutput(url)
        self.assertEqual(actualOutput, expectedOutput)

    def test_validIban_without_spaces(self):
        correctSubUrl = 'IBAN/'
        ibanStr = 'FR7630006000011234567890189'
        url = self.url + correctSubUrl + ibanStr
        expectedOutput = 'You sent a valid IBAN\n'
        actualOutput = self.GetActualOutput(url)
        self.assertEqual(actualOutput, expectedOutput)

    def test_IncorrectUrl(self):
        incorrectSubUrl = ''
        ibanStr = '1566'
        url = self.url + incorrectSubUrl + ibanStr
        expectedOutput = 'In order to validate IBAN, please type http://localhost:80/IBAN/**IBAN_VALUE**\n'
        actualOutput = self.GetActualOutput(url)
        self.assertEqual(actualOutput, expectedOutput)

    def test_Iban_lower_case(self):
        correctSubUrl = 'IBAN/'
        ibanStr = 'ro09bcyp0000001234567890'
        url = self.url + correctSubUrl + ibanStr
        expectedOutput = 'You sent a valid IBAN\n'
        actualOutput = self.GetActualOutput(url)
        self.assertEqual(actualOutput, expectedOutput)


if(__name__ == '__main__'):
    if(len(sys.argv) < 2):
        sys.exit("Please state the host name or domain name while running the code")
    if(len(sys.argv) > 2):
        sys.exit("Too many arguments. Please provide the host name or domain name alone")
    host= sys.argv[1]
    
    testIbanStandAlone = unittest.TestLoader().loadTestsFromTestCase(TestIbanValidation_Standalone)
    unittest.TextTestRunner(verbosity=2).run(testIbanStandAlone)

    testIbanWithWebServer = unittest.TestLoader().loadTestsFromTestCase(TestIbanValidation_WithWebServer)
    unittest.TextTestRunner(verbosity=2).run(testIbanWithWebServer)
