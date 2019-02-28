#!/usr/bin/python

import sys, getopt

from eVotUM.Cripto import eccblind
from eVotUM.Cripto import utils


# verify-app.py -cert <certificado do assinante> -msg <mensagem original a assinar> -sDash <Signature> -f <ficheiro do requerente>


# -cert key.crt -msg "Mensagem Secreta" -sDash  32ce67038beff412a4537b442d3d8b83cad42e3cf204e08e77e00d76cca06ad -f ofusca

def show_results(error_code, valid_signature):
    print("Output")
    if error_code is None:
        if valid_signature:
            print("Valid signature")
        else:
            print("Invalid signature")
    elif error_code == 1:
        print("Error: it was not possible to retrieve the public key")
    elif error_code == 2:
        print("Error: pR components are invalid")
    elif error_code == 3:
        print("Error: blind components are invalid")
    elif error_code == 4:
        print("Error: invalid signature format")


def main(argv):
    ecc_public_key_path = ''
    signature = ''
    p_r_dash_components = ''
    data = ''
    input_file = ''
    d = dict()
    try:
        opts, args = getopt.getopt(argv, "h:f:", ["cert=", "msg=", "sDash="])
    except getopt.GetoptError:
        print 'verify-app.py --cert <certificado do assinante> --msg <mensagem original a assinar> --sDash <Signature> -f <ficheiro do requerente>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'verify-app.py --cert <certificado do assinante> --msg <mensagem original a assinar> --sDash <Signature> -f <ficheiro do requerente>'
            sys.exit()
        elif opt == "--cert":
            ecc_public_key_path = arg
        elif opt == "--msg":
            data = arg
        elif opt == "--sDash":
            signature = arg
        elif opt == "-f":
            input_file = arg

    pem_public_key = utils.readFile(ecc_public_key_path)

    f = open(input_file, "r")
    for l in f:
        w = l.strip().split(":")
        d[w[0].strip()] = w[1].strip()

    blind_components = d['Blind components']
    p_r_dash_components = d["pRComponents"]

    error_code, valid_signature = eccblind.verifySignature(pem_public_key, signature, blind_components,
                                                           p_r_dash_components, data)
    show_results(error_code, valid_signature)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print 'verify-app.py --cert <certificado do assinante> --msg <mensagem original a assinar> --sDash <Signature> -f <ficheiro do requerente>'

