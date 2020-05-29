import pycountry

def main():
    list_all()

def list_all():
    all_countries = pycountry.countries
    for country_no in range[0, len(pycountry.countries)]:
        print(all_countries[country_no])


if __name__=="__main__":
    main()