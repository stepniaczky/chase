import argparse


class Parser:

    def __init__(self):

        self.parser = argparse.ArgumentParser(allow_abbrev=False)
        self.add_arguments()

    def add_arguments(self):
        self.parser.add_argument('-c', '--config', action='store', type=str, required=False,
                                 help='Path to config file')

        self.parser.add_argument('-d', '--dir', action='store', type=str, required=False,
                                 help='Path to subdirectory where pos.json, alive.csv and -- optionally -- chase.log should be placed.')

        self.parser.add_argument('-l', '--log', action='store', type=str, required=False,
                                 help='Logging events on different levels. Possible values: "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL".')

        self.parser.add_argument('-r', '--rounds', action='store', type=int, required=False,
                                 help='Number of maximal rounds of simulation.')

        self.parser.add_argument('-s', '--sheep', action='store', type=int, required=False,
                                 help='Number of sheep in flock.')

        self.parser.add_argument('-w', '--wait', action='store_true', required=False,
                                 help='Wait for user input after each round.')

    def get_args(self):
        args = self.parser.parse_args()
        return args
