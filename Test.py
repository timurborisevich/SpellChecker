import enchant
from enchant.checker import SpellChecker
# Одно слово:
dictionary = enchant.Dict("ru_RU")
# print(dictionary.check("раpчет"))
print(dictionary.check("УТС"))

# С учетом своего словаря
pwl = enchant.request_pwl_dict("NewWords.txt")
dictionary = enchant.DictWithPWL("ru_RU", "NewWords.txt")
print(dictionary.check("УТС"))

# Варианты замены:
# print(dictionary.suggest(u"раpчет"))

# Проверка предложений
checker = SpellChecker("ru_RU")
checker.set_text("рассчет себестоимости")
print([i.word for i in checker])

# С учетом фильтров
from enchant.tokenize import WikiWordFilter
checker = SpellChecker("ru_RU", filters=[WikiWordFilter])
checker.set_text("Разработка по УТС")
print([i.word for i in checker])