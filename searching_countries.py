import pycountry

def searching_by_codes(code):

    code_length = len(code)
    if code_length == 2:
        country_info = pycountry.countries.get(alpha_2=code)
        print(country_info.name)
    elif code_length == 3:
        country_info = pycountry.countries.get(alpha_3=code)
        print(country_info.name)
    else:
        print("This is not a alpha 2 or 3 country code")

def searching_by_alpha_2(alpha_2_code):

    country_info = pycountry.countries.get(alpha_2=alpha_2_code)
    if country_info == None:
        print("No Alpha 2 code found")
    else:
        print(country_info.name)

