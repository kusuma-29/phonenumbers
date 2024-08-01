import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# Get phone number input from the user
mobile_no = input("Enter Phone number with country code (+xx xxxxxxxxx): ")

# Parse the phone number
parsed_number = phonenumbers.parse(mobile_no)

# Check if the phone number is valid
if phonenumbers.is_valid_number(parsed_number):
    # Get the time zone(s) associated with the phone number
    time_zones = timezone.time_zones_for_number(parsed_number)
    print('Phone Number belongs to region:', time_zones)

    # Get the service provider (carrier) of the phone number
    service_provider = carrier.name_for_number(parsed_number,"en")
    print('Service Provider:', service_provider)

    # Get the country associated with the phone number
    country = geocoder.description_for_number(parsed_number, "en")
    print('Phone number belongs to country:', country)
else:
    print("Please enter a valid mobile number.")
