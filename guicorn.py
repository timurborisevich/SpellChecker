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
        return [bytes(answer, encoding="unicode")]
    if params_dic['wordexc'] != '':
        answer = AddNewWord(params_dic['wordexc'])
        return [bytes(answer, encoding="unicode")]