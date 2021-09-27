"""A simple reader for data file for MST problem"""


import sys

with open(sys.argv[1]) as data_file:
    # first line is total number of vertices in file and number of edges
    (nb_v, nb_e) = data_file.readline().split(' ')

    print("expected number of vertices : {0}".format(nb_v))
    print("expected number of edges : {0}\n".format(nb_e))

    # each line contains an edge
    for line in data_file:
        (start, end, cost) = line[:-1].split(' ')
        print("edge from {0} to {1} with cost {2}".format(start, end, cost))
