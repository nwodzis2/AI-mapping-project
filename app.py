from flask import Flask, render_template, request
from flask.helpers import make_response
from Constrain_Solution_Class import ConstraintSolution
versionNum = 0
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_map', methods=['POST'])
def generate_map():
    #get choosen colors
    colors = ["", "", "", "", "", ""]
    colors[0] = request.form['ColorInput0']
    colors[1] = request.form['ColorInput1']
    colors[2] = request.form['ColorInput2']
    colors[3] = request.form['ColorInput3']
    colors[4] = request.form['ColorInput4']
    colors[5] = request.form['ColorInput5']
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
    mainSettings ='var simplemaps_usmap_mapdata={ main_settings: { width: "responsive", background_color: "#FFFFFF", background_transparent: "yes", popups: "detect", state_description: "State description", state_color: "#88A4BC", state_hover_color: "#3B729F", state_url: "https://simplemaps.com", border_size: 1.5, border_color: "#ffffff", all_states_inactive: "no", all_states_zoomable: "no", location_description: "Location description", location_color: "#FF0067", location_opacity: 0.8, location_hover_opacity: 1, location_url: "", location_size: 25, location_type: "square", location_border_color: "#FFFFFF", location_border: 2, location_hover_border: 2.5, all_locations_inactive: "no", all_locations_hidden: "no", label_color: "#ffffff", label_hover_color: "#ffffff", label_size: 22, label_font: "Arial", hide_labels: "no", manual_zoom: "yes", back_image: "no", arrow_box: "no", navigation_size: "40", navigation_color: "#f7f7f7", navigation_border_color: "#636363", initial_back: "no", initial_zoom: -1, initial_zoom_solo: "no", region_opacity: 1, region_hover_opacity: 0.6, zoom_out_incrementally: "yes", zoom_percentage: 0.99, zoom_time: 0.5, popup_color: "white", popup_opacity: 0.9, popup_shadow: 1, popup_corners: 5, popup_font: "12px/1.5 Verdana, Arial, Helvetica, sans-serif", popup_nocss: "no", div: "map", auto_load: "yes", rotate: "0", url_new_tab: "yes", images_directory: "default", import_labels: "no", fade_time: 0.1, link_text: "View Website"}, '
    state_info = 'state_specific: {HI: { name: "Hawaii", description: "default", color: "default", hover_color: "default", url: "default" }, AK: { name: "Alaska", description: "default", color: "default", hover_color: "default", url: "default" }, FL: { name: "Florida", description: "default", color: "default", hover_color: "default", url: "default", inactive: "no" }, NH: { name: "New Hampshire", description: "default", color: "default", hover_color: "default", url: "default" }, VT: { name: "Vermont", description: "default", color: "default", hover_color: "default", url: "default" }, ME: { name: "Maine", description: "default", color: "default", hover_color: "default", url: "default" }, RI: { name: "Rhode Island", description: "default", color: "default", hover_color: "default", url: "default" }, NY: { name: "New York", description: "default", color: "default", hover_color: "default", url: "default" }, PA: { name: "Pennsylvania", description: "default", color: "default", hover_color: "default", url: "default" }, NJ: { name: "New Jersey", description: "default", color: "default", hover_color: "default", url: "default" }, DE: { name: "Delaware", description: "default", color: "default", hover_color: "default", url: "default" }, MD: { name: "Maryland", description: "default", color: "default", hover_color: "default", url: "default" }, VA: { name: "Virginia", description: "default", color: "default", hover_color: "default", url: "default" }, WV: { name: "West Virginia", description: "default", color: "default", hover_color: "default", url: "default" }, OH: { name: "Ohio", description: "default", color: "default", hover_color: "default", url: "default" }, IN: { name: "Indiana", description: "default", color: "default", hover_color: "default", url: "default" }, IL: { name: "Illinois", description: "default", color: "default", hover_color: "default", url: "default" }, CT: { name: "Connecticut", description: "default", color: "default", hover_color: "default", url: "default" }, WI: { name: "Wisconsin", description: "default", color: "default", hover_color: "default", url: "default" }, NC: { name: "North Carolina", description: "default", color: "default", hover_color: "default", url: "default" }, DC: { name: "District of Columbia", description: "default", color: "default", hover_color: "default", url: "default" }, MA: { name: "Massachusetts", description: "default", color: "default", hover_color: "default", url: "default" }, TN: { name: "Tennessee", description: "default", color: "default", hover_color: "default", url: "default" }, AR: { name: "Arkansas", description: "default", color: "default", hover_color: "default", url: "default" }, MO: { name: "Missouri", description: "default", color: "default", hover_color: "default", url: "default" }, GA: { name: "Georgia", description: "default", color: "default", hover_color: "default", url: "default" }, SC: { name: "South Carolina", description: "default", color: "default", hover_color: "default", url: "default" }, KY: { name: "Kentucky", description: "default", color: "default", zoomable: "no", hover_color: "default", url: "default" }, AL: { name: "Alabama", description: "default", color: "default", hover_color: "default", url: "default" }, LA: { name: "Louisiana", description: "default", color: "default", hover_color: "default", url: "default" }, MS: { name: "Mississippi", description: "default", color: "default", hover_color: "default", url: "default" }, IA: { name: "Iowa", description: "default", color: "default", hover_color: "default", url: "default" }, MN: { name: "Minnesota", description: "default", color: "default", hover_color: "default", url: "default" }, OK: { name: "Oklahoma", description: "default", color: "default", hover_color: "default", url: "default" }, TX: { name: "Texas", description: "default", color: "default", hover_color: "default", url: "default" }, NM: { name: "New Mexico", description: "default", color: "default", hover_color: "default", url: "default" }, KS: { name: "Kansas", description: "default", color: "default", hover_color: "default", url: "default" }, NE: { name: "Nebraska", description: "default", color: "default", hover_color: "default", url: "default" }, SD: { name: "South Dakota", description: "default", color: "default", hover_color: "default", url: "default" }, ND: { name: "North Dakota", description: "default", color: "default", hover_color: "default", url: "default" }, WY: { name: "Wyoming", description: "default", color: "default", hover_color: "default", url: "default" }, MT: { name: "Montana", description: "default", color: "default", hover_color: "default", url: "default" }, CO: { name: "Colorado", description: "default", color: "default", hover_color: "default", url: "default" }, UT: { name: "Utah", description: "default", color: "default", hover_color: "default", url: "default" }, AZ: { name: "Arizona", description: "default", color: "default", hover_color: "default", url: "default" }, NV: { name: "Nevada", description: "default", color: "default", hover_color: "default", url: "default" }, OR: { name: "Oregon", description: "default", color: "default", hover_color: "default", url: "default" }, WA: { name: "Washington", description: "default", color: "default", hover_color: "default", url: "default" }, CA: { name: "California", description: "default", color: "default", hover_color: "default", url: "default" }, MI: { name: "Michigan", description: "default", color: "default", hover_color: "default", url: "default" }, ID: { name: "Idaho", description: "default", color: "default", hover_color: "default", url: "default" }, GU: { name: "Guam", description: "default", color: "default", hover_color: "default", url: "default", hide: "yes" }, VI: { name: "Virgin Islands", description: "default", color: "default", hover_color: "default", url: "default", hide: "yes" }, PR: { name: "Puerto Rico", description: "default", color: "default", hover_color: "default", url: "default", hide: "yes" }, AS: { name: "American Samoa", description: "default", color: "default", hover_color: "default", url: "default", hide: "yes" }, MP: { name: "Northern Mariana Islands", description: "default", color: "default", hover_color: "default", url: "default", hide: "yes" } }, '
    labels = 'labels: { NH: { parent_id: "NH", x: "932", y: "183", pill: "yes", width: 45, display: "all" }, VT: { parent_id: "VT", x: "883", y: "243", pill: "yes", width: 45, display: "all" }, RI: { parent_id: "RI", x: "932", y: "273", pill: "yes", width: 45, display: "all" }, NJ: { parent_id: "NJ", x: "883", y: "273", pill: "yes", width: 45, display: "all" }, DE: { parent_id: "DE", x: "883", y: "303", pill: "yes", width: 45, display: "all" }, MD: { parent_id: "MD", x: "932", y: "303", pill: "yes", width: 45, display: "all" }, DC: { parent_id: "DC", x: "884", y: "332", pill: "yes", width: 45, display: "all" }, MA: { parent_id: "MA", x: "932", y: "213", pill: "yes", width: 45, display: "all" }, CT: { parent_id: "CT", x: "932", y: "243", pill: "yes", width: 45, display: "all" }, HI: { parent_id: "HI", x: 305, y: 565, pill: "yes" }, AK: { parent_id: "AK", x: "113", y: "495" }, FL: { parent_id: "FL", x: "773", y: "510" }, ME: { parent_id: "ME", x: "893", y: "85" }, NY: { parent_id: "NY", x: "815", y: "158" }, PA: { parent_id: "PA", x: "786", y: "210" }, VA: { parent_id: "VA", x: "790", y: "282" }, WV: { parent_id: "WV", x: "744", y: "270" }, OH: { parent_id: "OH", x: "700", y: "240" }, IN: { parent_id: "IN", x: "650", y: "250" }, IL: { parent_id: "IL", x: "600", y: "250" }, WI: { parent_id: "WI", x: "575", y: "155" }, NC: { parent_id: "NC", x: "784", y: "326" }, TN: { parent_id: "TN", x: "655", y: "340" }, AR: { parent_id: "AR", x: "548", y: "368" }, MO: { parent_id: "MO", x: "548", y: "293" }, GA: { parent_id: "GA", x: "718", y: "405" }, SC: { parent_id: "SC", x: "760", y: "371" }, KY: { parent_id: "KY", x: "680", y: "300" }, AL: { parent_id: "AL", x: "655", y: "405" }, LA: { parent_id: "LA", x: "550", y: "435" }, MS: { parent_id: "MS", x: "600", y: "405" }, IA: { parent_id: "IA", x: "525", y: "210" }, MN: { parent_id: "MN", x: "506", y: "124" }, OK: { parent_id: "OK", x: "460", y: "360" }, TX: { parent_id: "TX", x: "425", y: "435" }, NM: { parent_id: "NM", x: "305", y: "365" }, KS: { parent_id: "KS", x: "445", y: "290" }, NE: { parent_id: "NE", x: "420", y: "225" }, SD: { parent_id: "SD", x: "413", y: "160" }, ND: { parent_id: "ND", x: "416", y: "96" }, WY: { parent_id: "WY", x: "300", y: "180" }, MT: { parent_id: "MT", x: "280", y: "95" }, CO: { parent_id: "CO", x: "320", y: "275" }, UT: { parent_id: "UT", x: "223", y: "260" }, AZ: { parent_id: "AZ", x: "205", y: "360" }, NV: { parent_id: "NV", x: "140", y: "235" }, OR: { parent_id: "OR", x: "100", y: "120" }, WA: { parent_id: "WA", x: "130", y: "55" }, ID: { parent_id: "ID", x: "200", y: "150" }, CA: { parent_id: "CA", x: "79", y: "285" }, MI: { parent_id: "MI", x: "663", y: "185" }, PR: { parent_id: "PR", x: "620", y: "545" }, GU: { parent_id: "GU", x: "550", y: "540" }, VI: { parent_id: "VI", x: "680", y: "519" }, MP: { parent_id: "MP", x: "570", y: "575" }, AS: { parent_id: "AS", x: "665", y: "580" } } }'
    temp_state_info = 'state_specific :{'
    for key, value in result.items():
        temp_state_info = temp_state_info + key + ': { name: "' + key + '", description: "' + value + '", color : "' + value + '", hover_color: "default", url: "default" },'
    temp_state_info = temp_state_info + "}, "
    state_info = temp_state_info
    mapData = mainSettings + state_info + labels
    with open("./static/mapdata.js", "w") as mapdataFile:
        mapdataFile.write(mapData)
    response = make_response(render_template("index.html"))
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate" # HTTP 1.1.
    response.headers["Pragma"] = "no-cache" # HTTP 1.0.
    response.headers["Expires"] = "0" # Proxies.
    return response
