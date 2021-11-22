from typing import Dict, List
#define Constraint solution class
class CSC:
    def __init__(self) -> None:
        pass
    def goodSolution(index1, index2, assigned):
        if index1 not in assigned or index2 not in assigned:
            return True
        return assigned[index1] != assigned[index2]
    def backProp():
        

#define backwards propigation