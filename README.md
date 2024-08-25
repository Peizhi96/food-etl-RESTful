# food-etl-RESTful

## Project Overview

This project focuses on gathering, processing, and analyzing data on Asian restaurants located in downtown Los Angeles. The project involves the following steps:

1. **Data Collection (ETL)**:
    - Utilized the Google Places API to gather detailed information about Asian restaurants in downtown Los Angeles.
    - Converted the collected data into a CSV file.

2. **Data Processing**:
    - Split the restaurant data into three distinct tables:
        - `restaurant`: Contains restaurant-specific information such as type and opening hours.
        - `review`: Stores customer reviews and ratings.
        - `location`: Contains information about the restaurant’s location.
    - Loaded these tables into a PostgreSQL database.

3. **Cloud Deployment**:
    - Deployed the project on Azure, using Azure Data Factory for data processing.
    - Created a CI/CD pipeline with Azure DevOps to automate cloud deployment.
   - Uploaded the data files to Databricks for further processing.
