import pandas as pd
from extract import extract_data

def transform_data(raw_data):
    restaurants = raw_data
    data = []
    
    for res in restaurants:
        name = res.get('name', None)
        address = res.get('vicinity', None)
        longitude = res.get('geometry', {}).get('location', {}).get('lng', None)
        latitude = res.get('geometry', {}).get('location', {}).get('lat', None)
        rating = res.get('rating', None)
        price_level = res.get('price_level', None)
        user_ratings_total = res.get('user_ratings_total', None)
        open_now = res.get('opening_hours', {}).get('open_now', None)
        types_list = res.get('types', [])
        types = ', '.join(types_list)
        
        keyword = res.get('search_keyword', None)
        
        print(f"Processing: {name}, Types: {types_list}, Keyword: {keyword}")

        if "restaurant" in types:
            category = "restaurant"
        elif keyword == "Bubble Tea":
            category = "drinking"
        elif keyword in ["Chinese Restaurant", "Dumpling", "Dim Sum", "Hot Pot", "Noodle"]:
            category = "restaurant"
        else:
            category = "other"
                

        
        data.append({
            "name": name,
            "address": address,
            'longitude': longitude,
            'latitude': latitude,
            "rating": rating,
            "price_level": price_level,
            "user_ratings_total": user_ratings_total,
            "open_now": open_now,
            "types": types,
            "category": category
        })
        
    df = pd.DataFrame(data)
    #save the data to a csv file
    df.to_csv("restaurants.csv", index=False)
        
    return df

        