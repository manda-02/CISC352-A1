# =============================
# Student Names: Amanda Misek & Vanshita Uthra
# Group ID: Group 22
# Date: Jan 23, 2023
# =============================
# CISC 352 - W23
# cagey_csp.py
# desc:
#

#Look for #IMPLEMENT tags in this file.
'''
All models need to return a CSP object, and a list of lists of Variable objects
representing the board. The returned list of lists is used to access the
solution.

For example, after these three lines of code

    csp, var_array = binary_ne_grid(board)
    solver = BT(csp)
    solver.bt_search(prop_FC, var_ord)

var_array is a list of all variables in the given csp. If you are returning an entire grid's worth of variables
they should be arranged in a linearly, where index 0 represents the top left grid cell, index n-1 represents
the top right grid cell, and index (n^2)-1 represents the bottom right grid cell. Any additional variables you use
should fall after that (i.e., the cage operand variables, if required).

1. binary_ne_grid (worth 10/100 marks)
    - A model of a Cagey grid (without cage constraints) built using only
      binary not-equal constraints for both the row and column constraints.

2. nary_ad_grid (worth 10/100 marks)
    - A model of a Cagey grid (without cage constraints) built using only n-ary
      all-different constraints for both the row and column constraints.

3. cagey_csp_model (worth 20/100 marks)
    - a model of a Cagey grid built using your choice of (1) binary not-equal, or
      (2) n-ary all-different constraints for the grid, together with Cagey cage
      constraints.


Cagey Grids are addressed as follows (top number represents how the grid cells are adressed in grid definition tuple);
(bottom number represents where the cell would fall in the var_array):
+-------+-------+-------+-------+
|  1,1  |  1,2  |  ...  |  1,n  |
|       |       |       |       |
|   0   |   1   |       |  n-1  |
+-------+-------+-------+-------+
|  2,1  |  2,2  |  ...  |  2,n  |
|       |       |       |       |
|   n   |  n+1  |       | 2n-1  |
+-------+-------+-------+-------+
|  ...  |  ...  |  ...  |  ...  |
|       |       |       |       |
|       |       |       |       |
+-------+-------+-------+-------+
|  n,1  |  n,2  |  ...  |  n,n  |
|       |       |       |       |
|n^2-n-1| n^2-n |       | n^2-1 |
+-------+-------+-------+-------+

Boards are given in the following format:
(n, [cages])

n - is the size of the grid,
cages - is a list of tuples defining all cage constraints on a given grid.


each cage has the following structure
(v, [c1, c2, ..., cm], op)

v - the value of the cage.
[c1, c2, ..., cm] - is a list containing the address of each grid-cell which goes into the cage (e.g [(1,2), (1,1)])
op - a flag containing the operation used in the cage (None if unknown)
      - '+' for addition
      - '-' for subtraction
      - '*' for multiplication
      - '/' for division
      - '?' for unknown/no operation given

An example of a 3x3 puzzle would be defined as:
(3, [(3,[(1,1), (2,1)],"+"),(1, [(1,2)], '?'), (8, [(1,3), (2,3), (2,2)], "+"), (3, [(3,1)], '?'), (3, [(3,2), (3,3)], "+")])

'''

from cspbase import *

def binary_ne_grid(cagey_grid):
    # A model of a Cagey grid (without cage constraints) built using only binary not-equal constraints for
    # both the row and column constraints.
    ##IMPLEMENT

    grid = cagey_grid[0]
    queue = []
    constraints = []
    num = []
    tuples = []
    for i in range(grid):
        vals = []
        for j in range(grid):
            domain = list(range(1, grid + 1))
            vals.append(Variable("%d%d"%(i, j), domain))
        queue.append(vals)
    for r in queue:
        for v in r:
            num.append(v)
    csp = CSP("binary_ne_grid", num)

    # check the total possible tuples
    list_of_perms =[]
    for i in range(1, grid + 1):
        for j in range(1, grid + 1):
            if i != j:
                list_of_perms.append((i,j))
                
    for t in list_of_perms:
        tuples.append(t)

    for i in range(grid):
        for j in range(grid):
            for k in range(j + 1, grid):
                # check the rows
                cons = Constraint("r%d%d%d"%(i,j,k), [queue[i][j], queue[i][k]])
                cons.add_satisfying_tuples(tuples)
                constraints.append(cons)

                # check the cols
                cons = Constraint("c%d%d%d"%(i,j,k), [queue[j][i], queue[k][i]])
                cons.add_satisfying_tuples(tuples)
                constraints.append(cons)
    for constraint in constraints:
        csp.add_constraint(constraint)

    return csp, queue


def nary_ad_grid(cagey_grid):
    # A model of a Cagey grid (without cage constraints) built using only n-ary all-different constraints
    # for both the row and column constraints.
    ## IMPLEMENT
    pass

def cagey_csp_model(cagey_grid):
    # A model built using your choice of (1) binary binary not-equal, or (2) n-ary all-different constraints
    # for the grid, together with (3) cage constraints. That is, you will choose one of the previous two grid
    # models and expand it to include cage constraints.
    ##IMPLEMENT
    pass
