from urllib.parse import unquote
from Main import CheckText
from Main import AddNewWord

def pars_environ(environ):
    params = environ.split('&')
    params_dic = {}
    for param in params:
        cur_par = param.split('=')
        params_dic[cur_par[0]] = cur_par[1]
    return params_dic

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    environ = unquote(environ['QUERY_STRING'])
    params_dic = pars_environ(environ)
    if params_dic['text'] != '':
        answer = CheckText(params_dic['text'])
        return [bytes(str(answer), encoding="utf8")]
    if params_dic['wordexc'] != '':
        answer = AddNewWord(params_dic['wordexc'])
        return [bytes(str(answer), encoding="utf8")]

bind = "0.0.0.0:5556"


print(AddNewWord('ОВиК'))
print(CheckText('ОВиК'))