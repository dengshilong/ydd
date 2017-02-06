import requests
import click
API_URL = "http://fanyi.youdao.com/openapi.do?keyfrom=ydd-dict&key=1890264650&type=data&doctype=json&version=1.1"

def show_basic(s):
    basic = s["basic"]
    phonetic = ''
    if "phonetic" in basic:
        phonetic = '发音 {}'.format(basic["phonetic"])
    if "us-phonetic" in basic:
        phonetic += " 美式发音 {}".format(basic["us-phonetic"])
    if phonetic:
        click.secho(phonetic, fg='red')
    for explain in basic["explains"]:
        click.secho(explain, fg='blue')

def show_web(s):
    click.secho("#" * 8, fg="green")
    click.secho("短语", fg="green")
    web = s["web"]
    for item in web:
        click.secho("{} : {}".format(item["key"], '; '.join(item["value"])), fg='green')

def show_result(s):
    error_code = s["errorCode"]
    if error_code == 0:
        click.secho(' '.join(s["translation"]), fg='red')
        if "basic" in s:
            show_basic(s)
        if "web" in s:
            show_web(s)
    elif error_code == 20:
        click.secho('too long text(要翻译的文本过长)', fg='red')
    elif error_code == 30:
        click.secho("can't tranlate text(无法进行有效的翻译)", fg='red')
    elif error_code == 40:
        click.secho("unsupport language(不支持的语言类型)", fg='red')
    elif error_code == 50:
        click.secho("useless api key(无效的key)", fg='red')
    else:
        click.secho("no result(无词典结果)", fg='red')

def get_response_json(query):
    params = {"q": query}
    response = requests.get(API_URL, params=params)
    data = response.json()
    return data

@click.command()
@click.argument('words', nargs=-1)
def translate(words):
    query = ' '.join(words)
    result = get_response_json(query)
    show_result(result)

if __name__ == '__main__':
    translate()
