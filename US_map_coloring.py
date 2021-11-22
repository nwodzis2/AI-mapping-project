from typing import Generic, TypeVar, Dict, List, Optional
#define all our variable (the states)
variables = ["AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO",
"MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]
#define our constraints (where they border one another)
constraints = [["AL","GA"],["AL","MS"],["AL","FL"],["AL","TN"],["AZ","NM"],["AZ","CO"],["AZ","UT"],["AZ","NV"],["AZ","CA"],
["AR","MO"],["AR","OK"],["AR", "TX"],["AR","LA"],["AR","MS"],["AR","TN"],["CA","OR"],["CA","NV"],
["CO","NM"],["CO","UT"],["CO","WY"],["CO","NE"],["CO","KS"],["CO","OK"],["CT","RI"],["CT","NY"],["CT","MA"],["DE","MD"],["DE","NJ"],["DE","PA"],
["FL","GA"],["GA","NC"],["GA","SC"],["GA","TN"],["ID","MT"],["ID","NV"],["ID","OR"],["ID","UT"],["ID","WA"],["ID","WY"],
["IL","IN"],["IL","IA"]["IL","MI"],["IL","KY"],["IL","MO"],["IL","WI"],["IN","KY"],["IN","MI"],["IN","OH"],
["IA","MN"],["IA","MO"],["IA","NE"],["IA","SD"],["IA","WI"],["KS","MO"],["KS","NE"],["KS","OK"],
["KY","MO"],["KY","OH"],["KY","TN"],["KY","VA"],["KY","WV"],["LA","MI"],["LA","TX"],["ME","NH"],["MD","PA"],["MD","VA"],["MD","WV"],
["MA","NH"],["MA","NY"],["MA","RI"],["MA","VT"],["MI","MN"],["MI","OH"],["MI","WI"],["MN","ND"],["MN","SD"],["MN","WI"],["MS","TN"],
["MO","NE"],["MO","OK"],["MO","TN"],["MT","ND"],["MT","SD"],["MT","WY"],["NE","SD"],["NE","WY"],["NV","OR"],["NV","UT"],["NH","VT"],
["NJ","NY"],["NJ","PA"],["NM","OK"],["NM","TX"],["NM","UT"],["NY","PA"],["NY","RI"],["NY","VT"],["NC","SC"],["NC","TN"],["NC","VA"],
["ND","SD"],["OH","PA"],["OH","WV"],["OK","TX"],["OR","WA"],["PA","WV"],["SD","WY"],["TN","VA"],["UT","WY"],["VA","WV"]]
#set domains to the user inut
domains = ["", "", "", "", ""]
#define Constraint solution class
#define our satisfactory test
#define backwards propigation


