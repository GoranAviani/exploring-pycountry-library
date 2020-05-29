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

def main():
    list_all()
    list_all_historic_countries()
    searching_by_alpha_2("1SE")
    searching_by_codes("SWE")

def list_all_historic_countries():
    all_countries = list(pycountry.historic_countries)
    for country_no in range(0, len(all_countries)):
        found_country = all_countries[country_no]
        print("{}, {}".format(found_country.alpha_2, found_country.name))

def list_all():
    all_countries = list(pycountry.countries)
    for country_no in range(0, len(all_countries)):
        found_country = all_countries[country_no]
        print("{}, {}" .format(found_country.alpha_2, found_country.name))


if __name__=="__main__":
    main()