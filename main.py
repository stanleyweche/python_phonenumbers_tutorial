import phonenumbers, folium, sys, argparse, os,pycountry
from phonenumbers import geocoder, timezone, carrier
from colorama import init, Fore

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
