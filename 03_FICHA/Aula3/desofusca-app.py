#!/usr/bin/python

import getopt
import sys

from eVotUM.Cripto import eccblind


def show_results(error_code, signature):
    print("Output")
    if error_code is None:
        print("Signature: %s" % signature)
    elif error_code == 1:
        print("Error: pRDash components are invalid")
    elif error_code == 2:
        print("Error: blind components are invalid")
    elif error_code == 3:
        print("Error: invalid blind signature format")


def main(argv):
    blind_signature = ''
    p_r_dash_components = ''
    d = dict()
    input_file = ''
    try:
        opts, args = getopt.getopt(argv, "h:s:", ["signature=", "RDash=", "in="])
    except getopt.GetoptError:
        print 'desofusca-app.py -s <Blind Signature> --RDash <pRDashComponents> --in file'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'desofusca-app.py -s <Blind Signature> --RDash <pRDashComponents> --in file'
            sys.exit()
        elif opt in ("-s", "--signature"):
            blind_signature = arg
        elif opt == "--RDash":
            p_r_dash_components = arg
        elif opt == "--in":
            input_file = arg

    f = open(input_file, "r")
    for l in f:
        w = l.strip().split(":")
        d[w[0].strip()] = w[1].strip()

    blind_components = d['Blind components']

    error_code, signature = eccblind.unblindSignature(blind_signature, p_r_dash_components, blind_components)

    show_results(error_code, signature)


if __name__ == "__main__":
    if len(sys.argv) > 1:

        main(sys.argv[1:])
    else:
        print 'desofusca-app.py -s <Blind Signature> --RDash <pRDashComponents> --in file'

