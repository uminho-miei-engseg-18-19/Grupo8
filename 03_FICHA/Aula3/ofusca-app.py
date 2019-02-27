import sys, getopt
from eVotUM.Cripto import eccblind


def showResults(errorCode, result):
    print("Output")
    if (errorCode is None):
        blindComponents, pRComponents, blindM = result
        print("Blind message: %s" % blindM)
        print("Blind components: %s" % blindComponents)
        print("pRComponents: %s" % pRComponents)
    elif (errorCode == 1):
        print("Error: pRDash components are invalid")


def main(argv):
    pRDashComponents = ''
    data = ''
    out_file = ""
    try:
        opts, args = getopt.getopt(argv, "h:", ["msg=", "RDash=", "--out"])
    except getopt.GetoptError:
        print 'ofusca-app.py --msg <mensagem a assinar> --RDash <pRDashComponents> --out <ficheiro>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'ofusca-app.py --msg <mensagem a assinar> --RDash <pRDashComponents> --out <ficheiro>'
            sys.exit()
        elif opt in ("--msg"):
            data = arg
        elif opt in ("--RDash"):
            pRDashComponents = arg
        elif opt in ("--out"):
            out_file= arg
    s = data.encode('utf-8')
    errorCode, result = eccblind.blindData(pRDashComponents, "0x"+s.hex())
    with open(out_file, "w") as f:
        f.write(result + "\n")
    showResults(errorCode, result)



if __name__ == "__main__":
    main(sys.argv)
