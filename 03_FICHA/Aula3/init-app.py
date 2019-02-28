#!/usr/bin/python

import sys, getopt
from eVotUM.Cripto import eccblind


def get_p_r_dash_components():
    init_components, pr_dash_components = eccblind.initSigner()
    return init_components, pr_dash_components


def main(argv):

    if len(argv) > 0:
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
                out_file = arg

                init_components, pr_dash_components = get_p_r_dash_components()
                with open(out_file, "w") as f:
                    f.write("initComponents: " + init_components + "\n")
                    f.write("pRDashComponents: " + pr_dash_components + "\n")
                # print "File {} created".format(out_file)

    else:
            init_components, pr_dash_components = get_p_r_dash_components()
            print(pr_dash_components)


if __name__ == "__main__":
    main(sys.argv[1:])

