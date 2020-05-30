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

