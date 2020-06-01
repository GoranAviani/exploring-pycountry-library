import pycountry

def list_all_languages():
    all_languages = pycountry.languages
    for language in all_languages:
        print("{}, {}".format(language.alpha_3, language.name))


def search_by_name(language_name):
    language = pycountry.languages.get(name=language_name)
    if language == None:
        print("No language code found")
    else:
        print(language.alpha_3)

