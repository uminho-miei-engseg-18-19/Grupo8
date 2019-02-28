#!/usr/bin/python

import getopt
import sys

from eVotUM.Cripto import eccblind
from eVotUM.Cripto import utils


# blind_signature-app.py --key <chave privada> --bmsg <Blind message>

def show_results(error_code, blind_signature):
    print("Output")
    if error_code is None:
        print("Blind signature: %s" % blind_signature)
    elif error_code == 1:
        print("Error: it was not possible to retrieve the private key")
    elif error_code == 2:
        print("Error: init components are invalid")
    elif error_code == 3:
        print("Error: invalid blind message format")


def main(argv):
    ecc_private_key_path = ''
    blind_m = ''
    input_file = ''
    d = dict()
    try:
        opts, args = getopt.getopt(argv, "h:", ["key=", "bmsg=", "inputFile="])
    except getopt.GetoptError:
        print 'blind_signature-app.py -key <chave privada> -bmsg <Blind message>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'blind_signature-app.py --key <chave privada> --bmsg <Blind message>'
            sys.exit()
        elif opt == "--key":
            ecc_private_key_path = arg
        elif opt == "--bmsg":
            blind_m = arg
        elif opt == "--inputFile":
            input_file = arg

    pem_key = utils.readFile(ecc_private_key_path)
    passphrase = raw_input("Passphrase: ")
    f = open(input_file, "r")
    for l in f:
        w = l.strip().split(":")
        d[w[0].strip()] = w[1].strip()

    error_code, blind_signature = eccblind.generateBlindSignature(pem_key, passphrase, blind_m, d["initComponents"])
    show_results(error_code, blind_signature)


if __name__ == "__main__":
    main(sys.argv[1:])
