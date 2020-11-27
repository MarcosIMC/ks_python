
def check__argument(*argv):
    for i in argv:
        if argv == '-d':
            return "opcion d"
        elif argv == "-s":
            return "opcion s"
        else:
            return "ningun parametro"


