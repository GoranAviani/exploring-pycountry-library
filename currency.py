import pycountry

def list_all_currencies():
    all_currencies = pycountry.currencies
    for currency in all_currencies:
        print("{}, {}".format(currency.alpha_3, currency.name))

def searching_by_alpha_3(alpha_3_code):
    currency = pycountry.currencies.get(alpha_3=alpha_3_code)
    if currency == None:
        print("No Alpha 3 code found")
    else:
        print(currency.name)

