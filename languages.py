import pycountry

def list_all_languages():
    all_languages = pycountry.languages
    for language in all_languages:
        print("{}, {}".format(language.alpha_3, language.name))