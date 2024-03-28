import pandas as pd
from uszipcode import SearchEngine


def find_zipcodes_within_radius(latitude, longitude, radius_miles):
    search = SearchEngine()
    nearby_zipcodes = search.by_coordinates(latitude, longitude, radius=radius_miles, returns=100)
    return [zipcode.zipcode for zipcode in nearby_zipcodes]


# Read latitude and longitude coordinates from Excel file
data = pd.read_excel("C://Users/SINDHU/Downloads/zipcodes.xlsx")

# Radius options
radius_options = [5, 10, 15, 20]  # Radius in miles

# Create an empty dictionary to store dataframes for each radius
radius_dataframes = {}

# Iterate over radius options
for radius in radius_options:
    # Create an empty list to store results for this radius
    output_data = []

    # Iterate over each record
    for index, row in data.iterrows():
        latitude = row['Latitude']  # Assuming 'Latitude' is the column name for latitude
        longitude = row['Longitude']  # Assuming 'Longitude' is the column name for longitude

        # Find ZIP codes within the current radius
        zipcodes_within_radius = find_zipcodes_within_radius(latitude, longitude, radius)

        # Append the data to the output list
        output_data.append(
            {'Latitude': latitude, 'Longitude': longitude, 'Radius': radius, 'ZIP Codes': zipcodes_within_radius})

    # Convert the list to a DataFrame
    radius_df = pd.DataFrame(output_data)

    # Store the DataFrame in the dictionary with the radius as the key
    radius_dataframes[radius] = radius_df

# Save each DataFrame to a separate Excel sheet
with pd.ExcelWriter("C://Users/SINDHU/Downloads/output_sorted_by_radius.xlsx") as writer:
    for radius, df in radius_dataframes.items():
        df.to_excel(writer, sheet_name=f"Radius_{radius}", index=False)