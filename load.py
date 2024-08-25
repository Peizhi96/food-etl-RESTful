import sqlite3

def load_data(transformed_data, db_name='google_map_food.db'):
    conn = sqlite3.connect(db_name)
    transformed_data.to_sql('restaurants', conn, if_exists='replace', index=False)
    conn.close()
    
    
   