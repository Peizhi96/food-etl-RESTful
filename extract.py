import requests
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()
API_KEY = os.getenv("API_KEY")
# Google text API Key
URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

def extract_data(location, radius=100000, keywords=["Chinese Restaurant", "Bubble Tea", 'Dumpling', 'Dim Sum', 'Hot Pot', 'Noodle']):
    data = []
    for keyword in keywords:
        params = {
            "location": location,
            "radius": radius,
            "keyword": keyword,
            "key": API_KEY
        }

        
        while True:
            response = requests.get(URL, params=params)
            if response.status_code != 200:
                print("API Error")
                return None
            result = response.json()
            for place in result.get("results", []):
                place['search_keyword'] = keyword
            data.extend(result.get("results", []))
            
            next_page_token = result.get("next_page_token", None)
            if not next_page_token:
                break
            params["pagetoken"] = result["next_page_token"]
            import time
            time.sleep(2)
        
    return data

location = "34.0549, -118.2426"
data = extract_data(location)
print(data)