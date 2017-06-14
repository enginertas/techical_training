#!/usr/bin/env python

'''
Example Input:
13 22
2 12
0 10
0 1
6 10
3 10
2 7
4 11
0 8
7 10
9 12
7 11
1 9
5 11
5 7
2 11
4 8
2 8
5 9
2 4
2 5
1 7
10 11

Example Output:
287
'''

Variable_Count = 0
Requirement_Count = 0
Smaller_List = []
Bigger_List = []
Variable_Group_Map = {}
Last_Group_Id = 0
Cur_Variable_Values = []


def placeVarPairIntoGroup(small, big):   
    global Variable_Group_Map, Last_Group_Id

    if Variable_Group_Map.has_key(small) and Variable_Group_Map.has_key(big):
        if Variable_Group_Map[small] != Variable_Group_Map[big]:
            small_group_id = min(Variable_Group_Map[small], Variable_Group_Map[big])
            big_group_id = max(Variable_Group_Map[small], Variable_Group_Map[big])
            for key in Variable_Group_Map:
                if Variable_Group_Map[key] == big_group_id:
                    Variable_Group_Map[key] = small_group_id
    elif Variable_Group_Map.has_key(small):
        Variable_Group_Map[big] = Variable_Group_Map[small]
    elif Variable_Group_Map.has_key(big):
        Variable_Group_Map[small] = Variable_Group_Map[big]
    else:
        Variable_Group_Map[small] = Last_Group_Id
        Variable_Group_Map[big] = Last_Group_Id 
        Last_Group_Id = Last_Group_Id + 1
            
            
def readInput():
    global Variable_Count, Requirement_Count, Smaller_List, Bigger_List, Cur_Variable_Values
    
    # Read variable and build smaller & bigger & value lists
    Variable_Count, Requirement_Count = map(int, raw_input().split())
    for i in xrange(Variable_Count):
        Smaller_List.append([])
        Bigger_List.append([])
        Cur_Variable_Values.append(-1)
 
    # For each requirement, fill smaller & bigger lists
    #    and place the variable pairs into groups with regards to relativity 
    for i in xrange(Requirement_Count):
        small, big = map(int, raw_input().split())
        Smaller_List[big].append(small)
        Bigger_List[small].append(big)
        placeVarPairIntoGroup(small, big)


def orderByHeuristic(var_list):
    # Sort the list according to their total constraint count (max -> min)
    s_list = sorted(var_list, key=lambda i : len(Smaller_List[i]) + len(Bigger_List[i]), reverse=True)   
    return s_list

    
def getVariablesInGroups():
    # Separate variables into groups according to assignment dictionary that is set before
    grouped_vars = {}
    for var_index in Variable_Group_Map:
        if not grouped_vars.has_key(Variable_Group_Map[var_index]):
            grouped_vars[Variable_Group_Map[var_index]] = []
        grouped_vars[Variable_Group_Map[var_index]].append(var_index)

    # Derive the groups as list from dictionaries. Apply heuristics to list for much more efficient search.
    grouped_var_list = []
    for gr in grouped_vars:
        ordered_group = orderByHeuristic(grouped_vars[gr])
        grouped_var_list.append(ordered_group)
        
    # Append variables without constraints into another group. This is the most efficiently calculated group
    vars_without_constr = []
    for i in xrange(Variable_Count):
        if (not Smaller_List[i]) and (not Bigger_List[i]):
            vars_without_constr.append(i)
    grouped_var_list.append(vars_without_constr)
    
    return grouped_var_list
   

def determineAllowedRange(cur_index):
    constraints_completed = True
    
    max_small = 0
    for small in Smaller_List[cur_index]:
        if Cur_Variable_Values[small] == -1:
            constraints_completed = False
        else:
            if Cur_Variable_Values[small] > max_small:
                max_small = Cur_Variable_Values[small]
    
    min_big = 9
    for big in Bigger_List[cur_index]:
        if Cur_Variable_Values[big] == -1:
            constraints_completed = False
        else:
            if Cur_Variable_Values[big] < min_big:
                min_big = Cur_Variable_Values[big]
    
    return (range(max_small, min_big + 1), constraints_completed)


def backtrackOnVariables(depth):
    global Cur_Variable_Values

    # Base case
    if depth == Cur_Variable_Length:
        return 1
    
    # Get the actual index in current depth. Get possible values and the constraint complete status
    actual_index = Cur_Variable_List[depth]
    poss_values, constraints_completed = determineAllowedRange(actual_index)

    # If constraints are completed, pass into another variable (but multiply it)
    if constraints_completed:
        return (len(poss_values) * backtrackOnVariables(depth + 1)) % 1007
    
    # Loop over possible values. Pass into another variable if they are satisfied
    prob_count = 0
    for value in poss_values:
        Cur_Variable_Values[actual_index] = value
        prob_count = (prob_count + backtrackOnVariables(depth + 1)) % 1007
    
    # Clear the variable itself not to confuse by higher hierarchy variables
    Cur_Variable_Values[actual_index] = -1
    
    return prob_count

    
if __name__ == "__main__":   
    readInput()
    
    # Get variables in grouped manner (A group contains only linked variables)
    var_groups = getVariablesInGroups()

    # Backtrack over all variable groups separately and get the product as result
    total_count = 1
    for gr_list in var_groups:
        Cur_Variable_List = gr_list
        Cur_Variable_Length = len(gr_list)
        total_count = (total_count * backtrackOnVariables(0)) % 1007
        
    print total_count
