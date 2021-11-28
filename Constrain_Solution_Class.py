from typing import Dict, List
#define Constraint solution class for general solution, unspecialized
class ConstraintSolution:
    #constructor - initialize all variables
    def __init__(self, vars, doms, constraints):
        self.vars = vars # our states that will be constrained
        self.doms = doms # domain of each variable
        self.constraints = constraints #constraints for states with constraints (borders)
        self.assignedVars = {} #list of assigned varibles to colors, empty to start
        self.unvars = [variable for variable in self.vars]
    
    #checks to see if given two states, their assigned matches are consistent, helper for consistent. True or false.
    def goodSolution(self, index1, index2):
        if index1 not in self.assignedVars or index2 not in self.assignedVars: #if either isn't assignedVars, immediatly true
            return True
        else:
            mybool = self.assignedVars[index1] != self.assignedVars[index2] #since they are both already assigned, if the colors match then is false otherwise true
            return  mybool 
    
    #this is backtracking search to get our answers, will return a dict with assigned specific domain (color) for each variable (state or ocean)
    def backProp(self):
        # We are done!, last recursion. Every variable has been assigned a specific domain (color)
        lenAssigned = len(self.assignedVars)
        lenVars = len(self.vars)
        if lenAssigned == lenVars:
            return self.assignedVars
        #Get our unassigned variable to work with
        self.unvar = self.unvars[0]
        #remove the front that will soon go into assigned
        self.unvars.pop(0)
        #be able to check every possible combination if necessary, iterate and recurse
        for specDom in self.doms[self.unvar]:
            self.assignedVars[self.unvar] = specDom
            if self.consistent(self.unvar): #check and see if with a given specific domain (value) we are still consistent we continue he recursion
                final = self.backProp()
                # This is coming on the way out of the recursion
                if final is not None:
                    return final #Return our final result if it was found (which should come from final recursion)
        return None #if no solution is found return None
    
    #instead of calling backProp, a getter to get the solution and reset self vars
    def findSolution(self):
        solution = self.backProp()
        #reset asssigned and unassigned vars
        self.assignedVars = {}
        self.unvars = [var for var in self.vars]

        return solution #return what was returned in backProp()

    #check if our new value is consistent
    def consistent(self, var):
        if var not in self.constraints: #has no constraints then any color will work
            return True
        for constr in self.constraints[var]: #Make sure each constriant is satisfied
            if not self.goodSolution(var, constr):
                return False #if any bad solution retrn false
        return True #if all checks out return true