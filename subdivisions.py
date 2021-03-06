import pycountry

def search_by_subdivision(subdivision):
    """
   There’s also a “fuzzy” search to help people discover “proper” countries
    for names that might only actually be subdivisions. The fuzziness also
    includes normalizing unicode accents. There’s also a bit of prioritization
     included to prefer matches on country names before subdivision names
     and have countries with more matches be listed before ones with fewer
      matches:
    :param subdivision: String containing a subdivision country name
    :return: n/a
    """
    country_info = pycountry.countries.search_fuzzy(subdivision)
    for country in country_info:
        print("{}, {},{}" .format(country.alpha_2, country.name, country.official_name))
