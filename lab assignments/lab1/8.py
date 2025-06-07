# Function to extract countries containing a given substring
def extract_countries_with_substring(countries, substring):
    result = [country for country in countries if substring.lower() in country.lower()]
    return result

# Input: List of countries
countries = input("Enter the names of countries separated by commas: ").split(",")
countries = [country.strip() for country in countries]  # Remove extra spaces

# Input: Substring to search for
substring = input("Enter the substring to search for: ")

# Extract countries containing the substring
matching_countries = extract_countries_with_substring(countries, substring)

# Display the results
print("\nCountries containing the substring:")
if matching_countries:
    for country in matching_countries:
        print(country)
else:
    print("No countries found with the given substring.")
