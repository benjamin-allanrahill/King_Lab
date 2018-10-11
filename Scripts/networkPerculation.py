# Gene Network Perculation
# Benjamin Allan-Rahill

import csv
import sys
import networkx as nx
G = nx.Graph()

# Read in file and create gene network
def read_file_and_create_network (in_file):

    with open(in_file) as f_in:

        reader = csv.reader(f_in, delimiter=",")

        for row in reader:
            firstEdge = row[0]
            secondEdge = row[1]
            print(firstEdge,secondEdge)


def main (arguments):
    in_file = arguments[0]

    read_file_and_create_network(in_file)


# all this code does is allow the program to be run from the command line
if __name__ == '__main__':
    main(sys.argv)


