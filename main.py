import phonenumbers
import sys
import requests
from phonenumbers import geocoder, timezone, carrier
from colorama import init, Fore

init()

phone = phonenumbers.parse(input("Enter phone number starting with country code: "))

if phonenumbers.is_possible_number(phone):
    print("Possible number")
else:
    print("The number is incomplete")
    sys.exit()

if phonenumbers.is_valid_number(phone):
    print("Declared as a valid number")
else:
    print("ERROR")
    sys.exit()

time = phonenumbers.timezone.time_zones_for_number(phone)
simcard = carrier.name_for_number(phone, "en")
geocode = geocoder.description_for_number(phone, "en")

print(time)
print(simcard)
print(geocode)

# Assuming you have these attributes to get cell tower location
# You'll need real API keys and ensure these fields are accurate
api_key = "YOUR_OPENCELLID_API_KEY"
phone_country_code = phone.country_code  # Example attribute, replace with actual
phone_national_destination_code = phone.national_number  # Example attribute, replace with actual

# Get the cell tower location using OpenCellID
cell_tower_url = f"https://api.opencellid.org/cell/get?key={api_key}&mcc={phone_country_code}&mnc={phone_national_destination_code}"
response = requests.get(cell_tower_url)
cell_tower_data = response.json()

# Ensure the data contains 'lat' and 'lon' before accessing
if 'lat' in cell_tower_data and 'lon' in cell_tower_data:
    latitude = cell_tower_data["lat"]
    longitude = cell_tower_data["lon"]

    # Use the latitude and longitude to get the live location
    location_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key=YOUR_GOOGLE_MAPS_API_KEY"
    response = requests.get(location_url)
    location_data = response.json()

    # Print the live location of the person
    if location_data['results']:
        print(f"Live location: {location_data['results'][0]['formatted_address']}")
    else:
        print("Location data not found")
else:
    print("Cell tower data not found or incomplete")

