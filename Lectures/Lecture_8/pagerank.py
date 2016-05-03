# Iteratively computes the pageranks of the 11 nodes of the graph
# of the wikipedia entry that illustrates the pagerank algorithm,
# with a damping factor of 0.85.
# The number of iterations is input by the user, prompted to do so.
# Otuputs the labels and pageranks of pages from largest to smallest value.
#
# Written by Eric Martin for COMP9021

import sys
import numpy as np

NODE_NB = 11

adjacency_matrix = np.matrix([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])


# Given i and j smaller than NODE_NB, probabilistic_transitions[i, j] is set to
# the damping factor divided by the outdegree of the (i + 1)st node if there
# is a link from that node to the (j + 1)st node, to 0 if there is no such link
# but the (i + 1)st node is not a dangling node, and to the damping factor divided
# by the total number of nodes otherwise.
def attach_weights_to_links(damping_factor = .85):
    for i in range(NODE_NB):
        out_degree = sum(1 for j in range(NODE_NB) if adjacency_matrix[i, j])
        for j in range(NODE_NB):
            if adjacency_matrix[i, j]:
                probabilistic_transitions[i, j] = damping_factor / out_degree
            elif not out_degree:
                probabilistic_transitions[i, j] = damping_factor / NODE_NB


# First sets the pageranks to the inverse of the number of nodes
# (the random walker randomly chooses a node to start with).
# Then for every stage n > 0 smaller than the number of iterations and
# for all j smaller than NODE_NB, updates the pagerank of the (j + 1)st node by
# adding to (1 - damping_factor) / NODE_NB (the probability of being teleported
# from some node to the (j + 1)st node) the product of the pagerank of the
# (i + 1)st node at stage n - 1 with the value of probabilistic_transitions[i, j]
# (the probability that if the random walker arrives at stage n at the (j + 1)st node,
# then it actually comes from the (i + 1)st node without using teleportation),
# for all i smaller than NODE_NB.
def compute_pageranks(nb_of_iterations, damping_factor = .85):
    teleportation = np.full((1, NODE_NB), (1 - damping_factor) / NODE_NB, dtype = float)
    current_page_ranks =np.full((1, NODE_NB), 1 / NODE_NB, dtype = float)
    for n in range(nb_of_iterations):
        current_page_ranks = current_page_ranks * probabilistic_transitions + teleportation
    return current_page_ranks


try:
    nb_of_iterations = int(input('How many iterations do you want? '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

probabilistic_transitions = np.asmatrix(np.zeros(shape = (NODE_NB, NODE_NB), dtype = float))
attach_weights_to_links()
pageranks = compute_pageranks(nb_of_iterations)
pageranks = {chr(ord('A') + i): pageranks[0, i] for i in range(NODE_NB)}
for page in sorted(pageranks, key = pageranks.get, reverse = True):
    print('{} : {:.3f}'.format(page, pageranks[page]))

