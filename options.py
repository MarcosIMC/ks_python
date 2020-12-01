import sys


class Options():
    def __init__(self, *args):
        if 1 < len(sys.argv) < 7:
            check_first_argument(sys.argv[1])
        else:
            help_menu()