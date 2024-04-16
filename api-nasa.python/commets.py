import requests
import os

def get_coments_data (api_key) :
    print ("Getting coments data")
    api_url= f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        print ("Coment name:", data [ "name"])
        print ("apsolute magnitude: ", data ["absolute_magnitude_h"])
        print ("Estimated diameter max (km): ", data["estimated_diameter"] ["kilometers"] ["estimated_diameter_max"])
        print("Estimated diameter min (km): ", data["estimated_diameter"] ["kilometers"] ["estimated_diameter_min"])
        print("Estimated diameter max (ft): ", data["estimated_diameter"]["feet"] ["estimated_diameter_max"])
        print("Estimated diameter min (ft): ", data["estimated_diameter"]["feet"] ["estimated_diameter_min"])
        print ("Last observation date: ", data["orbital_data"] ["last_observation_date"])
    except requests.exceptions.RequestException as e:
        print (f"API ERROR{e}")

api_key_nasa = "eEqVBWUM3eotzuCJ1jTkKpWsx0wZfjz45yhVvKfG"
get_coments_data(api_key_nasa)