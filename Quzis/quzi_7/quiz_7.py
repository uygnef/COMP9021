# let F be the unique function defined on sequences of distinct integers that satisfies
# the following conditions:
# - F(()) = ().
# - Let n >= 1 and e_1, ..., e_n be a sequence of distinct integers.
#   Let i_1, ..., i_k be the longest sequence of integers such that
#   1 <= i_1 < i_2 ... < i_k <= n and e_{i_1} < e_{i_2} < ... < e_{i_k}.
#   Let j_1, ..., j_{n - k} be such that 1 <= j_1 < j_2 ... < j_{n - k} <= n
#   and j_1, ..., j_{n - k} are distinct from i_1, i_2 ..., i_k.
#   Then F((e_1, ..., e_n)) = (e_{i_1}, e_{i_2}, ..., e_{i_k}) * F((e_{j_1}, ..., e_{j_{n - k}})).
#
# Prompts the user for a seed and a nonnegative integer n so as to randomly generate
# a linked list L of n distinct numbers. Prints out L, calls the function rearrange() on L
# -- a function that essentially implements F to operate on linked lists --, and prints out L again,
# which should have the same head and consist of the same nodes as the original, but linked differently.
#
# Written by *** and Eric Martin for COMP9021


import sys
from random import seed, sample
from linked_list import *
from extended_linked_list import ExtendedLinkedList

def collect_references(L, length):
    node = L.head
    references = set()
    for i in range(length):
        references.add(id(node))
        node = node.next_node
    return references
        

provided_input = input('Enter 2 positive integers: ')
try:
    provided_input = [int(arg) for arg in provided_input.split()]
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()
    
if len(provided_input) != 2:
    print('Incorrect input (not 2 arguments), giving up.')
    sys.exit()
for_seed, length = provided_input
if length < 0 or length > 100:
    print('Incorrect input (2nd integer not positive, giving up.')
    sys.exit()
seed(for_seed)

L = sample(list(range(length * 10)), length)

LL = ExtendedLinkedList(L)
LL.print()
references = collect_references(LL, length)
LL.rearrange()
if collect_references(LL, length) != references:
    print('You cheated!')
    sys.exit()
else:
    LL.print()
    

