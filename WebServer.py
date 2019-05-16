#!/usr/bin/env python3

from socket import *
import re
from urllib import parse
import IBANValidation
import time
import sys

class WebServer_class():
    def __init__(self, host = '', port = 80, connections = 5):
        self.webHost = host
        self.webPort = port
        self.allowedConnections = connections
        self.commonResponse = (b'HTTP/1.0 200 OK \n'
                               b'Content-Type:text/html \n'
                               b'\n')
        self.outputForValidIban = (b'You sent a valid IBAN\n')
        self.outputForInvalidIban = (b'You sent an invalid IBAN\n')
        self.outputForIncorrectURL = (b'In order to validate IBAN, please type http://localhost:80/IBAN/**IBAN_VALUE**\n')
        self.ibanSubUrlFormat = 'iban'
        self.favIconRequestFormat = 'favicon.ico'

    def Parse_webRequest_For_Iban(self, webreqInBytes):
        webreqBytesList = webreqInBytes.split(b'\r\n')
        subURLinBytes = webreqBytesList[0]
        unparsedSubURL = subURLinBytes.decode()
        subURLlist = re.split("\s", unparsedSubURL)
        httpIndex = 0
        for i in range(len(subURLlist)):
            if(subURLlist[i] == 'HTTP/1.1'):
                httpIndex = i
        ibanSubURL = ''
        ibanStrIndex = 1
        while (ibanStrIndex < httpIndex):
            ibanSubURL += subURLlist[ibanStrIndex]
            ibanStrIndex += 1
        ibanSubURL = re.split("/", ibanSubURL)
        return ibanSubURL

    def RemoveFavIconRequest(self, webReqList):
        webReqList[1] = webReqList[1].lower()
        if(webReqList[1] == self.ibanSubUrlFormat):
            ibanNum = webReqList[2]
            ibanNum = parse.unquote(ibanNum,encoding = 'UTF-8', errors ='replace')
            return str(ibanNum)
        if(webReqList[1] == self.favIconRequestFormat):
            return -1
        else:
            return 0 ##For incorrect URL.

    def HandleClient(self, clientSocket):
        unParsedWebRequest = clientSocket.recv(1024)
        semiParsedWebReq = self.Parse_webRequest_For_Iban(unParsedWebRequest)
        ibanStr = self.RemoveFavIconRequest(semiParsedWebReq)
        if(ibanStr != -1) & (ibanStr != 0): #-1 is to avoid fav icon issue.
                iban = IBANValidation.IBAN()
                ibanFlag = iban.ValidateIban(ibanStr)
                if(ibanFlag):
                    outputForValidIban = self.commonResponse + self.outputForValidIban
                    clientSocket.sendall(outputForValidIban)
                else:
                    outputForInvalidIban = self.commonResponse + self.outputForInvalidIban
                    clientSocket.sendall(outputForInvalidIban)

        if(ibanStr == 0):
                outputForIncorrectURL = self.commonResponse + self.outputForIncorrectURL
                clientSocket.sendall(outputForIncorrectURL)
        print("Output has been delivered to the client.")
        clientSocket.close()


    def Set_ServerSocket(self):
        serverSocket = socket(AF_INET, SOCK_STREAM)
        print("******************* Server side output **************************")
        try:
            serverSocket.bind((self.webHost, self.webPort))
        except OSError:
            print("Address is already in use. It may be due to temporary block and so the program will sleep for 100 seconds now. It will try connecting again after the sleep.")
            time.sleep(100)
            print("Sleep is over.")
            try:
                serverSocket.bind((self.webHost, self.webPort))
            except OSError:
                sys.exit("Address is still in use even after a sleep of 100 seconds and hence the issue is not related to temporary block. Can you please ensure that the address is not being used elsewhere")

        serverSocket.listen(self.allowedConnections)
        print("Server is ready to listen client's request.")
        while True:
            clientSocket, clientAddress = serverSocket.accept()
            print("A client has been connected from", clientAddress)
            self.HandleClient(clientSocket)

if(__name__ == '__main__'):
    WebServer_obj = WebServer_class()
    WebServer_obj.Set_ServerSocket()

