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
# Written by *** and Eric Martin for COMP9021


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
    
    stack = []
    move = {'SE':[[1,1], [0,1], [1,0]], 'NE':[[-1,1], [0,1], [-1,0]], \
            'SW':[[1,-1],[0,-1],[1,0]], 'NW':[[-1,-1],[0,-1],[-1,0]]}
    path = [grid[3][3]]
    end = True
    while end:
        for direction in move[path[t]]:
            for m in direction:
                if 0<= i+m[0] <= 6 and 0 <=j+m[1]<= 6: 
                    path.append(grid[i+m[0]][j+m[1]])
                    if i+m[0] == 0 and j+m[1] == 0 :
                        path['(0,0)'] = stack
        
                
        path.append(grid[i+move[path[i]][0][0]][j+move[path[i]][0][1]]
        
        
        
    

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
