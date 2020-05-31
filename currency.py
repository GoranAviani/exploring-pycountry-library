import pycountry

def list_all_currencies():
    all_currencies = pycountry.currencies
    for currency in all_currencies:
        print(str(currency))
        #print("{}, {}".format(found_country.alpha_2, found_country.name))

