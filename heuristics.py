# =============================
# Student Names: Amanda Misek & Vanshita Uthra
# Group ID: Group 22
# Date: Jan 23, 2023
# =============================
# CISC 352 - W23
# heuristics.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   the propagators

var_ordering == a function with the following template
    var_ordering(csp)
        ==> returns Variable

    csp is a CSP object---the heuristic can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    var_ordering returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.
   '''

def ord_dh(csp):
    ''' return variables according to the Degree Heuristic '''

    # A variable ordering heuristic that chooses the next variable to be assigned according to the Degree
    # heuristic (DH). ord dh returns the variable that is involved in the largest number of constraints,
    # which have other unassigned variables.

    # IMPLEMENT
    mini_val = None
    unassigned_vars = csp.get_all_unasgn_vars()
    var_degree = float("-inf")

    # find the minimum value in the domain
    for i in unassigned_vars:
         curr = len(csp.get_cons_with_var(i))
         if curr > var_degree:
            var_degree = curr
            mini_val = i
    return mini_val 
   

def ord_mrv(csp):
    ''' return variable according to the Minimum Remaining Values heuristic '''

    # A variable ordering heuristic that chooses the next variable to be assigned according to the MinimumRemaining-Value (MRV) heuristic. 
    # ord mrv returns the variable with the most constrained current
    # domain (i.e., the variable with the fewest legal values remaining).
    # IMPLEMENT
    mini_domain = float('inf')  # set the domain to infinity  # minimum value   -->  minimum domain
    mini_val = None
    unassigned_vars = csp.get_all_unasgn_vars()

    # find the minimum value in the domain
    for i in unassigned_vars:
        if i.cur_domain_size() < mini_domain:
            mini_domain = i.cur_domain_size()
            mini_val = i
    return mini_val  
   
    
