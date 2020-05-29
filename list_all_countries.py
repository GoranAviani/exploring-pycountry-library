import pycountry

def main():
    list_all()

def list_all():
    all_countries = list(pycountry.countries)
    for country_no in range(0, len(all_countries)):
        print(str(all_countries[country_no]))


if __name__=="__main__":
    main()