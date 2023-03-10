# =============================
# Student Names: Amanda Misek & Vanshita Uthra
# Group ID: Group 22
# Date: Jan 23, 2023
# =============================
# CISC 352 - W23
# propagators.py
# desc:
#


#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete problem solution.

'''This file will contain different constraint propagators to be used within
   bt_search.

   propagator == a function with the following template
      propagator(csp, newly_instantiated_variable=None)
           ==> returns (True/False, [(Variable, Value), (Variable, Value) ...]

      csp is a CSP object---the propagator can use this to get access
      to the variables and constraints of the problem. The assigned variables
      can be accessed via methods, the values assigned can also be accessed.

      newly_instaniated_variable is an optional argument.
      if newly_instantiated_variable is not None:
          then newly_instantiated_variable is the most
           recently assigned variable of the search.
      else:
          progator is called before any assignments are made
          in which case it must decide what processing to do
           prior to any variables being assigned. SEE BELOW

       The propagator returns True/False and a list of (Variable, Value) pairs.
       Return is False if a deadend has been detected by the propagator.
       in this case bt_search will backtrack
       return is true if we can continue.

      The list of variable values pairs are all of the values
      the propagator pruned (using the variable's prune_value method).
      bt_search NEEDS to know this in order to correctly restore these
      values when it undoes a variable assignment.

      NOTE propagator SHOULD NOT prune a value that has already been
      pruned! Nor should it prune a value twice

      PROPAGATOR called with newly_instantiated_variable = None
      PROCESSING REQUIRED:
        for plain backtracking (where we only check fully instantiated
        constraints)
        we do nothing...return true, []

        for forward checking (where we only check constraints with one
        remaining variable)
        we look for unary constraints of the csp (constraints whose scope
        contains only one variable) and we forward_check these constraints.

        for gac we establish initial GAC by initializing the GAC queue
        with all constaints of the csp


      PROPAGATOR called with newly_instantiated_variable = a variable V
      PROCESSING REQUIRED:
         for plain backtracking we check all constraints with V (see csp method
         get_cons_with_var) that are fully assigned.

         for forward checking we forward check all constraints with V
         that have one unassigned variable left

         for gac we initialize the GAC queue with all constraints containing V.
   '''

def prop_BT(csp, newVar=None):
    '''Do plain backtracking propagation. That is, do no
    propagation at all. Just check fully instantiated constraints'''

    if not newVar:
        return True, []
    for c in csp.get_cons_with_var(newVar):
        if c.get_n_unasgn() == 0:
            vals = []
            vars = c.get_scope()
            for var in vars:
                vals.append(var.get_assigned_value())
            if not c.check_tuple(vals):
                return False, []
    return True, []

def prop_FC(csp, newVar=None):
    '''Do forward checking. That is check constraints with
       only one uninstantiated variable. Remember to keep
       track of all pruned variable,value pairs and return '''
    #IMPLEMENT

    # If newVar is None, forward check all constraints. 
    # Otherwise only check constraints containing newVar.
    
    
    fc_constraints = []
    pruned = []

    if (newVar != None):
        fc_constraints = csp.get_cons_with_var(newVar)
    else:
        fc_constraints = csp.get_all_cons()


    for i in fc_constraints:
        if i.get_n_unasgn() == 1:
            # first element of the list
            un_assigned = i.get_unasgn_vars()[0]
            for j in un_assigned.cur_domain():
                if not i.check_var_val(un_assigned, j):
                    tuple = (un_assigned, j)
                    if(tuple not in pruned):
                        pruned.append(tuple)
                        un_assigned.prune_value(j)
                        
            if un_assigned.cur_domain_size() == 0:
                return False, pruned
            
    return True, pruned

def prop_GAC(csp, newVar=None):
    '''Do GAC propagation. If newVar is None we do initial GAC enforce
       processing all constraints. Otherwise we do GAC enforce with
       constraints containing newVar on GAC Queue'''

    # A propagator function that propagates according to the GAC algorithm, as covered in lecture. If
    # newVar is None, run GAC on all constraints. Otherwise, only check constraints containing
    # newVar.

    #IMPLEMENT
    pruned = []
    queue = []
    
    if (newVar != None):
        gac_constraints = csp.get_cons_with_var(newVar)
    else:
        gac_constraints = csp.get_all_cons()
   
    
    for q in gac_constraints:
        queue.append(q)
    
    while len(queue) != 0:
        q = queue.pop(0)
        # elements in the constraint
        for elem in q.get_scope():
            # values in the current domain
            for j in elem.cur_domain():
                if not q.check_var_val(elem, j):     
                    tuple = (elem, j)
                    # tuple is not pruned
                    if(tuple not in pruned):
                        # prune the tuple
                        pruned.append(tuple)
                        elem.prune_value(j)
                    if elem.cur_domain_size() == 0:   
                        queue.clear()
                        return False, pruned
                    else:   # if removed
                        for k in csp.get_cons_with_var(elem):
                            if (k not in queue):
                                queue.append(k)
    return True, pruned

