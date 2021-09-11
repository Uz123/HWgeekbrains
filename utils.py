import requests as rew
from decimal import Decimal

response = rew.get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = rew.utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)


def currency_rates(char_code):
    currency_str = content.split("<Valute ID=")
    for idx in currency_str:
        if char_code.upper() in idx:
            return Decimal(idx.replace("/", "").split("<Value>")[-2].replace(",", "."))


if __name__ == "__name__":
    print(currency_rates("USD"))
    print(currency_rates("usd"))
    print(currency_rates("usdk"))
