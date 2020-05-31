from list_all_countries import (
    list_all,
    list_all_historic_countries,
)
from searching_countries import (
    searching_by_alpha_2,
    searching_by_alpha_codes
)

from currency import list_all_currencies, searching_by_alpha_3

def main():
    list_all()
    list_all_historic_countries()
    searching_by_alpha_2("1SE")
    searching_by_alpha_codes("SWE")

    list_all_currencies()
    searching_by_alpha_3("HRK")

if __name__=="__main__":
    main()