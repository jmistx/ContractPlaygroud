дома двадцать пять по улице Пушкина, возле магазина Спар
д. 25, ул. Пушкина
25, Пушкина
25, кв 20, улица Пушкина
улица Пушкина, двадцать пять дом
34500
1
25 а Генерала Нахимова
25 Генерала Нахимова
25/4 Генерала Нахимова
25/4, Генерала Нахимова
25/4,,,,,,,, Генерала Нахимова

def UI():
    fieldValue = getString(...)
    home_object = parse(fieldValue)

@require(s is not None)
def parse(s):
    algo = find_appropriate_algo(s)
    if algo.checkHasHouseNumber(s) is None:
        return "Вы не ввели номер дома"
    if algo.checkHasStreet(s) is None:
        return "Вы не ввели улицу"
    return algo.split(s)    

def find_appropriate_algo(a):
    for method in methods:
        if method.Satisfies(a):
            return method
    return {
        "home" : None,
        "street": None
    }


if not methods.Stisfies(a):
    return "not my format"

return method(a)

parse(a)
# require:
#     contains: 'д.'
#     contains: 'ул.'
#     one_of_words_is_int(a)
#     contains: ','
#     a[0] != ','


@require(re.Match("[a-z]*", s))
def all_eating_algo(a):
        "([a-z], street)*([])"
    return {}
