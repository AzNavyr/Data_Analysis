import gettext
import pycountry

russian = gettext.translation("iso3166-2", pycountry.LOCALES_DIR, languages=["en"])
russian.install()
_ = russian.gettext

def get_country(code):
    ru = pycountry.countries.get(alpha_2=code)
    return _(ru.name)

print(get_country("RU"))
print(get_country("US"))
print(get_country("DE"))
print(get_country("CA"))
print(get_country("FR"))

