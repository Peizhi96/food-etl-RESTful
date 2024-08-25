from extract import extract_data
from transform import transform_data
from load import load_data

def main():
    location = "34.0549, -118.2426"
    raw_data = extract_data(location)
    transformed_data = transform_data(raw_data)
    load_data(transformed_data)
    
if __name__ == "__main__":
    main()