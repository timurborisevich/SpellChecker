import enchant
from enchant.checker import SpellChecker

checker = SpellChecker('ru_RU')
pwl = enchant.request_pwl_dict('NewWords.txt')
new_dictionary = enchant.DictWithPWL('ru_RU', 'NewWords.txt')

def CheckText(text):
    checker.set_text(text)
    answer = ''
    for i in checker:
        word = i.word
        if not new_dictionary.check(word):
            if answer == '':
                answer = answer + word
            else:
                answer = answer + ', ' + word
    return answer

def AddNewWord(word):
    with open('NewWords.txt', 'a', encoding='utf-8') as file:
        if not new_dictionary.check(word):
            file.write('\n' + word)
            return "Добавлено!"
        else:
            return "Слово уже есть в словаре!"