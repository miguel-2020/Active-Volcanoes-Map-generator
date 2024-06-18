import os
import webbrowser
import folium
from loggers import logger,error_logger

def gen_map_marker_html(volcano_name,threat_level,image_url,link,message):
    color = ""
    if threat_level and  "high" in threat_level.lower():
        color = "#ff5470"
    elif threat_level and "low" in threat_level.lower():
        color = "#078080"
    elif threat_level and "moderate" in threat_level.lower():
        color ="#ff8e3c"

    return """
        <h1 style="color:#1f1235;padding:1.5rem; text-transform:capitalize;">{volcano_name}</h1><br>
        <img style="object-fit:center" src="{image_url}" alt="No image available for this mountain." width="300" height="300">
        <p style="color:{threat_level_color}; font-size:1.8rem; font-weight:bolder; text-transform:capitalize;">
            <b> {threat_level}</b>
        </p>

        <p style="font-size:1.5rem;">{message}</p>
        <p style="font-size:1.5rem;">
            <a href="{link}" target="_blank" rel="noreferrer">Read more...</a>
        </p>


    """.format(volcano_name=volcano_name,
               threat_level=threat_level,
               threat_level_color=color,
               image_url=image_url,link=link,
               message=message)

def gen_map_markers(map,records):

    for volcano in records:
        name = volcano["volcano_name"]
        threat_level = volcano[ "nvewsthreat"]
        image_url = volcano[ "image"]
        link = volcano["gvplink"]
        message = volcano["status"]
        latitude = volcano["latitude"]
        longitude = volcano[ "longitude"]
        
        # generate the markers html template
        html = gen_map_marker_html(name,threat_level,image_url,link,message)


        folium.Marker(location=[latitude, longitude],tooltip=f"{name}",popup=html,lazy=True,icon=folium.Icon(color="green")).add_to(map)

def generateMap(records):
    file_name = "index.html"
    logger.info(f"Generating map {file_name} file")

    # default location: Los Angeles, California, United States of America
    latitude = 34.0536909
    longitude = -118.242766
    map = folium.Map((latitude, longitude), zoom_start=5)
    
      

    gen_map_markers(map,records)
    
            
    logger.info("map generated")

    map.save(file_name)

    # Display map
    filename = 'file:///'+os.getcwd()+'/' + 'index.html'
    webbrowser.open_new_tab(filename) 