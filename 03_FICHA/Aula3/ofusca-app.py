import sys, getopt
from eVotUM.Cripto import eccblind


def show_results(error_code, result):
    print("Output")
    if error_code is None:
        blind_components, p_r_components, blind_m = result
        print("Blind message: %s" % blind_m)
    elif error_code == 1:
        print("Error: pRDash components are invalid")


def main(argv):
    p_r_dash_components = ''
    data = ''
    out_file = ''
    try:
        opts, args = getopt.getopt(argv, "h:", ["msg=", "RDash=", "out="])
    except getopt.GetoptError:
        print 'ofusca-app.py --msg <mensagem a assinar> --RDash <pRDashComponents> --out <ficheiro>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'ofusca-app.py --msg <mensagem a assinar> --RDash <pRDashComponents> --out <ficheiro>'
            sys.exit()
        elif opt == "--msg":
            data = arg
        elif opt == "--RDash":
            p_r_dash_components = arg
        elif opt == "--out":
            out_file = arg

    data_hex = '0x' + data.encode('hex')
    error_code, result = eccblind.blindData(p_r_dash_components, data)
    with open(out_file, "w") as f:
        f.write("Blind components: " + result[0] + '\n')
        f.write("pRComponents: " + result[1] + '\n')
    show_results(error_code, result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
    else:
        print 'ofusca-app.py --msg <mensagem a assinar> --RDash <pRDashComponents> --out <ficheiro>'
