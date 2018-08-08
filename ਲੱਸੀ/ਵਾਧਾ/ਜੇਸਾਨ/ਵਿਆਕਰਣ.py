import pprint

from ਲੱਸੀ.ਵਿਆਕਰਣ.ਭਾਸ਼ਾ import ਵਿਆਕਰਣ_ਵਾਧਾ


class GrammaireJSON(ਵਿਆਕਰਣ_ਵਾਧਾ):
    ਵਿਆ = 'ਜੇਸਾਨ.lark'
    ਵਾਧਾ = '.json'
    ਸਰੋਤ_ਭਾ = 'en'

    def ਬਾਅਦ_ਕਾਰਵਾਈ(ਖੁਦ, ਦਸਤ):
        return pprint.pformat(ਦਸਤ)

if __name__ == '__main__':
    g = GrammaireJSON()
    g.ਦਸਤ_ਸਰੋਤ_ਅਨੁ_ਬੲਾਉ()
    g.ਦਸਤ_ਅਨੁ_ਵਿਆ_ਬੲਾਉ(['த', 'ગુ', 'हिं', 'fr', 'kaq'])
