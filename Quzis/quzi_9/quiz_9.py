# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with node values ranging between 0 and 999,999,
# displays it, and outputs the sum of the node values on the longest branches,
# either counting the values for a given node only once,
# or counting it for as many times as the number of branches on which the node occurs.
#
# Written by Yu Feng and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree import *

# Possibly define some functions
        
def sums_on_longest_branches(tree):
    if tree.height() == 0:
        if tree.value != None:
            a = tree.value
        else:
            a = 0

    else:
        if tree.left_node.height() > tree.right_node.height() :
            print('left',tree.value)
            a = tree.value + sums_on_longest_branches(tree.left_node)[0]
            b = tree.value + sums_on_longest_branches(tree.left_node)

        elif tree.left_node.height() < tree.right_node.height() :
            print('right',tree.value)
            a = tree.value + sums_on_longest_branches(tree.right_node)[0]

        else:
            print('all',tree.value)
            a = tree.value + \
                sums_on_longest_branches(tree.left_node)[0] + \
                sums_on_longest_branches(tree.right_node)[0]

            b = 2 * tree.value + \
                sums_on_longest_branches(tree.left_node)[1] + \
                sums_on_longest_branches(tree.right_node)[1]                
                
    return (a,b)
                
provided_input = input('Enter two integers, the second one being positive: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    seed_arg = int(provided_input[0])
    nb_of_nodes = int(provided_input[1])
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(seed_arg)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The sums of the values on the longest branches are, counting each value only once')
print('  or counting it for all branches on which its occurs: ', end = '')
print(sums_on_longest_branches(tree))
           
