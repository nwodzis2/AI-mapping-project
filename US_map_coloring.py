from Constrain_Solution_Class import ConstraintSolution

if __name__ == "__main__":
    #define all our variables (the states)
    states = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO",
    "MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY", "Pacific", "Atlantic", "Gulf"]
    
    #define our constraints (where they border one another)
    constraints = {
    "AL": ["MS", "TN", "FL", "GA"],
    "AZ" : ["NV", "NM", "UT", "CO", "CA"],
    "AR" : ["LA", "OK", "TX", "MO", "TN", "MS"],
    "CA" : ["NV", "OR" , "AZ"],
    "CO" : ["WY", "UT", "NE", "KS", "OK", "NM", "AZ"],
    "CT" : ["NY", "RI", "MA"],
    "DE" : ["NJ", "PA", "MD"],
    "FL" : ["AL", "GA"],
    "GA" : ["FL", "SC", "NC", "TN", "AL"],
    "ID" : ["OR", "WA", "MT", "WY", "UT", "NV"],
    "IL" : ["IA", "WI", "IN", "KY", "MO", "MI"],
    "IN" : ["MI", "OH", "KY", "IL"],
    "IA" : ["NE", "SD", "MN", "WI", "IL", "MO"],
    "KS" : ["CO", "NE", "MO", "OK"],
    "KY" : ["IL", "IN", "OH", "WV", "VA", "TN", "MO"],
    "LA" : ["TX", "AR", "MS"],
    "ME" : ["NH"],
    "MD" : ["VA", "WV", "DE", "PA"],
    "MA" : ["NY", "RI", "VT", "CT", "NH"],
    "MI" : ["OH", "WI", "IL", "IN", "MN"],
    "MN" : ["ND", "SD", "IA", "WI", "MI"],
    "MS" : ["LA", "AR", "TN", "AL"],
    "MO" : ["NE", "IA", "IL", "KY", "TN", "AR", "OK", "KS"],
    "MT" : ["ID", "WY", "SD", "ND"],
    "NE" : ["MO", "IA", "SD", "WY", "CO", "KS"],
    "NV" : ["ID", "UT", "AZ", "CA", "OR"],
    "NH" : ["VT", "ME", "MA"],
    "NJ" : ["PA", "DE", "NY"],
    "NM" : ["OK", "TX", "UT", "AZ", "CO"],
    "NY" : ["PA", "RI", "VT", "CT", "MA", "NJ"],
    "NC" : ["VA", "SC", "GA", "TN"],
    "ND" : ["SD", "MN", "MT"],
    "OH" : ["MI", "PA", "WV", "KY", "IN"],
    "OK" : ["TX", "AR", "MO", "KS", "CO", "NM"],
    "OR" : ["NV", "WA", "ID", "CA"],
    "PA" : ["NY", "OH", "WV", "DE", "MD", "NJ"],
    "RI" : ["MA", "NY", "CT"],
    "SC" : ["GA", "NC"],
    "SD" : ["ND", "MN", "IA", "NE", "WY", "MT"],
    "TN" : ["MO", "AR", "MS", "AL", "GA", "NC", "VA", "KY"],
    "TX" : ["NM", "OK", "AR", "LA"],
    "UT" : ["NV", "ID", "WY", "CO", "NM", "AZ"],
    "VT" : ["NH", "NY", "MA"],
    "VA" : ["NC", "TN", "WV", "KY", "MD"],
    "WA" : ["OR", "ID"],
    "WV" : ["PA", "VA", "OH", "KY", "MD"],
    "WI" : ["MI", "IL", "IA", "MN"],
    "WY" : ["NE", "SD", "UT", "CO", "ID", "MT"],
    }
    #set colors to the user input
    colors = ["", "", "", "", "", ""]
    #Get input for choosen colors (5 for states and one for oceans)
    colors[0], colors[1], colors[2], colors[3], colors[4] = input("enter colors for STATES followed by a space (use rgb in format xxx,xxx,xxx)").split(" ")
    colors[5] = input("Please enter the color for the OCEANS").split()

    doms = {} #defines what color each state or ocean can be assigned to (added for the oceans having a different domain)
    for state in states:
        if(state == "Pacific" or state == "Atlantic" or state == "Gulf"): #case not a state but an ocean
            doms[state] = colors[5]
        else:
            doms[state] = [colors[0], colors[1], colors[2], colors[3], colors[4]] #A state
    #initialize our constraint solution class with our values
    CS = ConstraintSolution(states, doms, constraints)
    #find our solution
    result = CS.findSolution()
    #map our solution
    print(result)







