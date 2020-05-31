import pycountry

def list_all_currencies():
    all_currencies = pycountry.currencies
    for currency in all_currencies:
        print("{}, {}".format(currency.alpha_3, currency.name))

