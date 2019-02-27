#!/usr/bin/python

import sys, getopt
from eVotUM.Cripto import eccblind


def getpRDashComponents():
    initComponents, pRDashComponents = eccblind.initSigner()
    return initComponents, pRDashComponents


def main(argv):
    input_file = ''

    if  len(argv) > 0:
        try:
            opts, args = getopt.getopt(argv, "h:", ["init="])
        except getopt.GetoptError:
            print('python init-app.py --init <outputfile> or python init-app.py')
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print('python init-app.py --init <outputfile> or python init-app.py ')
                sys.exit()
            elif opt == "--init":
                input_file = arg
                initComponents, pRDashComponents = getpRDashComponents()
                with open(input_file, "w") as f:
                    f.write("initComponents: " + initComponents + "\n")
                    f.write("pRDashComponents: " + pRDashComponents + "\n")

    else:
            initComponents, pRDashComponents = getpRDashComponents()
            print(pRDashComponents)


if __name__ == "__main__":
    main(sys.argv[1:])

