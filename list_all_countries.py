import pycountry

def main():
    list_all()
    list_all_historic_countries()

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