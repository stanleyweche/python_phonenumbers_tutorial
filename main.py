import phonenumbers, sys, argparse, os
from phonenumbers import geocoder, timezone, carrier
from colorama import init, Fore
import requests

init()

phone = phonenumbers.parse(input("Enter phone number starting with countries code:  "))
if phonenumbers.is_possible_number(phone):
    print("")
else:
    print("The number is incomplete")
    sys.exit()

if phonenumbers.is_valid_number(phone):
    print("Declared as a valid number")
else:
    print("ERROR")
    sys.exit()

time =  phonenumbers.timezone.time_zones_for_number(phone)
simcard = carrier.name_for_number(phone,"en")
geocode = geocoder.description_for_number(phone, "en")

print(time)
print(simcard)
print(geocode)

# Get the cell tower location using OpenCellID
api_key = "YOUR_OPENCELLID_API_KEY"
cell_tower_url = f"https://api.opencellid.org/cell/get?key={api_key}&mcc={phone.country_code}&mnc={phone.national_destination_code}&lac={phone.location_area_code}&cellid={phone.cell_id}"
response = requests.get(cell_tower_url)
cell_tower_data = response.json()

# Get the latitude and longitude of the cell tower
latitude = cell_tower_data["lat"]
longitude = cell_tower_data["lon"]

# Use the latitude and longitude to get the live location of the person
location_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key=YOUR_GOOGLE_MAPS_API_KEY"
response = requests.get(location_url)
location_data = response.json()

# Print the live location of the person
print(f"Live location: {location_data['results'][0]['formatted_address']}")
