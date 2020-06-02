import pycountry

def list_all_historic_countries():
    """
    Historical countries are accessible through a database object
     that is already configured upon import of pycountry and works
      as an iterable.
    The historic_countries database contains former countries
    that have been removed from the standard and are now included
     in ISO 3166-3, excluding existing ones:
    :return: n/a
    """
    all_countries = list(pycountry.historic_countries)
    for country_no in range(0, len(all_countries)):
        found_country = all_countries[country_no]
        print("{}, {}".format(found_country.alpha_2, found_country.name))

def list_all():
    """
    Countries are accessible through a database object that is already
     configured upon import of pycountry and works as an iterable
    :return: n/a
    """
    all_countries = list(pycountry.countries)
    for country_no in range(0, len(all_countries)):
        found_country = all_countries[country_no]
        print("{}, {}" .format(found_country.alpha_2, found_country.name))

def searching_by_alpha_codes(code):
    """
    Specific countries can be looked up by their various codes
    and provide the information included in the standard as attributes:
    :param code: String containing a two letter or three letter uppercase country code
    :return: n/a
    """

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
    """
    Specific countries can be looked up by their various codes
    and provide the information included in the standard as attributes:
    :param alpha_2_code: String containing a two letter uppercase alpha country code
    :return: n/a
    """
    country_info = pycountry.countries.get(alpha_2=alpha_2_code)
    if country_info == None:
        print("No Alpha 2 code found")
    else:
        print(country_info.name)
