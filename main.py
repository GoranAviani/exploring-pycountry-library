from list_all_countries import (
    list_all,
    list_all_historic_countries,
)
from searching_countries import (
    searching_by_alpha_2,
    searching_by_alpha_codes
)

from lookups import lookup_a_country

from currency import list_all_currencies, searching_by_alpha_3

from searching_subdivisions import (
    search_by_subdivision
)

from languages import list_all_languages, search_by_name

def main():
    list_all()
    list_all_historic_countries()
    searching_by_alpha_2("1SE")
    searching_by_alpha_codes("SWE")
    search_by_subdivision("England")
    search_by_subdivision("Cote")


    list_all_currencies()
    searching_by_alpha_3("HRK")

    list_all_languages()
    search_by_name("English")
    search_by_name("Klingon")
    search_by_name("Gibberish")

    lookup_a_country("de")
    
if __name__=="__main__":
    main()