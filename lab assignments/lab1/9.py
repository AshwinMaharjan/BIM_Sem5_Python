# Function to extract districts where headquarter name is the same as the district name
def extract_districts__headquarter(districts_dict):
    result = [district for district, headquarter in districts_dict.items() if district.lower() == headquarter.lower()]
    return result

# Creating a dictionary with districts and their headquarters
districts_dict = {
    "Kathmandu": "Kathmandu",
    "Lailitpur": "Patan",
    "Bhaktapur": "Bhaktapur",
    "Kathmandu": "Kritipur",
    "Sindhupalchowk ": "Shivapuri"
}

# Extract districts where headquarter name is the same as the district name
matching_districts = extract_districts__headquarter(districts_dict)

# Display the result
print("Districts where headquarter name is the same as the district name:")
if matching_districts:
    for district in matching_districts:
        print(district)
else:
    print("No districts found with the same name as their headquarters.")
