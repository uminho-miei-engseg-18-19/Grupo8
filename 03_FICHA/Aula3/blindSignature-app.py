#!/usr/bin/python

import sys, getopt
from eVotUM.Cripto import utils

from eVotUM.Cripto import eccblind


# blindSignature-app.py -key <chave privada> -bmsg <Blind message>

def showResults(errorCode, blindSignature):
    print("Output")
    if (errorCode is None):
        print("Blind signature: %s" % blindSignature)
    elif (errorCode == 1):
        print("Error: it was not possible to retrieve the private key")
    elif (errorCode == 2):
        print("Error: init components are invalid")
    elif (errorCode == 3):
        print("Error: invalid blind message format")



def main(argv):
    eccPrivateKeyPath = ''
    blindM = ''
    file = ''
    d = dict()
    try:
        opts, args = getopt.getopt(argv, "h:", ["key=", "bmsg=", "file="])
    except getopt.GetoptError:
        print 'blindSignature-app.py -key <chave privada> -bmsg <Blind message>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'blindSignature-app.py --key <chave privada> --bmsg <Blind message>'
            sys.exit()
        elif opt in ("--key"):
            key = arg
        elif opt in ("--RDash"):
            blindM = arg
        elif opt in ("--file"):
            file = arg

    pemKey = utils.readFile(eccPrivateKeyPath)
    print("Input")
    passphrase = raw_input("Passphrase: ")
    f = open(file, "r")
    for l in f:
        w = l.strip().split(":")
        d[w[0].strip()] = w[1].strip()
    errorCode, blindSignature = eccblind.generateBlindSignature(pemKey, passphrase, blindM, d["initComponents"])
    showResults(errorCode, blindSignature)




if __name__ == "__main__":
    main(sys.argv)



