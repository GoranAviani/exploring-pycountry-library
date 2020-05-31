from list_all_countries import (
    list_all,
    list_all_historic_countries,
)
from searching_countries import (
    searching_by_alpha_2,
    searching_by_alpha_codes
)

from searching_subdivisions import (
    search_by_subdivision
)


def main():
    list_all()
    list_all_historic_countries()
    searching_by_alpha_2("1SE")
    searching_by_alpha_codes("SWE")
    search_by_subdivision("England")
    search_by_subdivision("Cote")


if __name__=="__main__":
    main()