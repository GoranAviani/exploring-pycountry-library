from list_all_countries import (
    list_all,
    list_all_historic_countries,
)
from search_countries import (
    searching_by_alpha_2,
    searching_by_alpha_codes
)


def main():
    list_all()
    list_all_historic_countries()
    searching_by_alpha_2("1SE")
    searching_by_alpha_codes("SWE")

if __name__=="__main__":
    main()