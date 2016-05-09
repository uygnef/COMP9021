# Randomly fills a grid of size 7 x 7 with NE, SE, SW, NW,
# meant to represent North-East, South-East, North-West, South-West,
# respectively, and starting from the cell in the middle of the grid,
# determines, for each of the 4 corners of the grid, the preferred path amongst
# the shortest paths that reach that corner, if any. At a given cell, it is possible to move
# according to any of the 3 directions indicated by the value of the cell;
# e.g., from a cell storing NE, it is possible to move North-East, East, or North.
# At any given point, one prefers to move diagonally, then horizontally,
# and vertically as a last resort.
#
# Written by Yu Feng and Eric Martin for COMP9021


import sys
from random import seed, choice
from array_queue import *

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

def preferred_paths_to_corners():
    import copy
    SE = (1,1),  (0,1), (1,0)
    NE = (-1,1), (0,1), (-1,0)
    SW = (1,-1), (0,-1),(1,0)
    NW = (-1,-1),(0,-1),(-1,0)
    move = {'SE':SE, 'NE':NE, 'SW':SW, 'NW':NW}


    have_been = []
    init_path = [(3,3)]
    all_path = [init_path]
    result = {}
    for path in all_path:           
        state = grid[path[-1][0]][path[-1][1]]
        for m in move[state]:            
            i = path[-1][0]
            j = path[-1][1]
            if 0<= i+m[0] <= 6 and 0 <= j+m[1]<= 6:
                if (i+m[0], j+m[1]) not in have_been:
                    new_path = copy.deepcopy(path)
                    new_path.append((i+m[0], j+m[1]))
                
                    if (i+m[0], j+m[1]) in corners:
                        result[(i+m[0], j+m[1])] = new_path
                        have_been.append((i+m[0], j+m[1]))
                    else:
                        all_path.append(new_path)       
                        have_been.append((i+m[0], j+m[1]))

    fin_result = {}
    
    for i in result:
        fin_result[(i[1],i[0])] = []
        for j in result[i]:
            x = j[0]
            y = j[1]
            fin_result[(i[1],i[0])].append((y,x))
    return fin_result
          
    

try:
    seed_arg = int(input('Enter an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
size = 3
dim = 2 * size + 1
grid = [[0] * dim for _ in range(dim)]
directions = 'NE', 'SE', 'SW', 'NW'

for i in range(dim):
    for j in range(dim):
        grid[i][j] = choice(directions)
print('Here is the grid that has been generated:')
display_grid()

corners = (0, 0), (dim - 1, 0), (dim - 1, dim - 1), (0, dim - 1)
paths = preferred_paths_to_corners()
if not paths:
    print('There is no path to any corner')
    sys.exit()
for corner in corners:
    if corner not in paths:
        print('There is no path to {}'.format(corner))
    else:
        print('The preferred path to {} is:'.format(corner))
        print('  ', paths[corner])
