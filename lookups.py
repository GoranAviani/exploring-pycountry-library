import pycountry

def lookup_a_country(word):
    found_data = pycountry.countries.lookup(word)
    print(found_data)

def lookup_a_language(word):
    found_data = pycountry.languages.lookup(word)
    print(found_data)