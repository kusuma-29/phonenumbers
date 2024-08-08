# Overview
This Python script utilizes the phonenumbers library to parse, validate, and extract information from a phone number provided by the user. The script provides details such as the time zone, carrier, and country associated with the phone number.

# Prerequasities
Python 3.x
phonenumbers library

To install the phonenumbers library, run: pip install phonenumbers

# Functionality

# User Input
The script prompts the user to input a phone number, including the country code, in the format +xx xxxxxxxxx.

# Parsing Phone Number
The phonenumbers.parse function parses the input phone number, converting it into a standardized format.

# Validation
The script checks if the parsed phone number is valid using phonenumbers.is_valid_number.

# Extracting Information

Time Zone(s): The script uses timezone.time_zones_for_number to find the time zone(s) associated with the phone number.

Carrier: The carrier.name_for_number function retrieves the service provider for the phone number.

Country: The geocoder.description_for_number function determines the country associated with the phone number.

# Output
If the phone number is valid, the script prints the time zone(s), service provider, and country.
If the phone number is invalid, it prompts the user to enter a valid mobile number.

![Screenshot (368)](https://github.com/user-attachments/assets/f31e0283-4488-410b-a630-97762e7c19f5)

![Screenshot (369)](https://github.com/user-attachments/assets/d0a96d47-76ad-47e1-a217-0a45b099bedd)

