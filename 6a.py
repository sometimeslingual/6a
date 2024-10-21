import re

def validate_phone_number(phone_number):
    # Phone number pattern: (xxx) xxx-xxxx or xxx-xxx-xxxx
    phone_pattern = r"^\(?\d{3}\)?[- ]?\d{3}[- ]?\d{4}$"
    return bool(re.match(phone_pattern, phone_number))

def validate_ssn(ssn):
    # SSN pattern: xxx-xx-xxxx
    ssn_pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(ssn_pattern, ssn))

def validate_zip_code(zip_code):
    # Zip code pattern: 5 digits, optionally followed by a hyphen and 4 more digits
    zip_pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(zip_pattern, zip_code))

def main():
    # Ask the user for inputs
    phone_number = input("Enter phone number (e.g., 123-456-7890 or (123) 456-7890): ")
    ssn = input("Enter Social Security Number (e.g., 123-45-6789): ")
    zip_code = input("Enter ZIP code (e.g., 12345 or 12345-6789): ")

    # Validate phone number
    if validate_phone_number(phone_number):
        print(f"Phone number {phone_number} is valid.")
    else:
        print(f"Phone number {phone_number} is invalid.")

    # Validate SSN
    if validate_ssn(ssn):
        print(f"Social Security Number {ssn} is valid.")
    else:
        print(f"Social Security Number {ssn} is invalid.")

    # Validate ZIP code
    if validate_zip_code(zip_code):
        print(f"ZIP code {zip_code} is valid.")
    else:
        print(f"ZIP code {zip_code} is invalid.")

if __name__ == "__main__":
    main()
