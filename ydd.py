#coding: utf-8
import os
import subprocess
import requests
import click
import six
from click_default_group import DefaultGroup

API_URL = "http://fanyi.youdao.com/openapi.do?keyfrom=ydd-dict&key=1890264650&type=data&doctype=json&version=1.1"

def show_basic(s):
    basic = s["basic"]
    phonetic = ''
    if "phonetic" in basic:
        if six.PY3:
            phonetic = '发音 {}'.format(basic["phonetic"])
        else:
            phonetic = u'发音 {}'.format(basic["phonetic"])
    if "us-phonetic" in basic:
        if six.PY3:
            phonetic += " 美式发音 {}".format(basic["us-phonetic"])
        else:
            phonetic += u" 美式发音 {}".format(basic["us-phonetic"])
    if phonetic:
        click.secho(phonetic, fg='red')
    for explain in basic["explains"]:
        click.secho(explain, fg='blue')

def show_web(s):
    click.secho("#" * 8, fg="green")
    web = s["web"]
    for item in web:
        if six.PY3:
            click.secho("{} : {}".format(item["key"], '; '.join(item["value"])), fg='green')
        else:
            click.secho(u"{} : {}".format(item["key"], '; '.join(item["value"])), fg='green')

def show_result(s):
    error_code = s["errorCode"]
    if error_code == 0:
        click.secho(' '.join(s["translation"]), fg='red')
        if "basic" in s:
            show_basic(s)
        if "web" in s:
            show_web(s)
        save_history(s)
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

def save_history(s):
    key = s["query"]
    explain = ' '.join(s["translation"])
    line = key + ' ' + explain + '\n'
    with open('history.txt', 'a+') as f:
        if six.PY3:
            f.write(line)
        else:
            f.write(line.encode('utf-8'))

@click.group(cls=DefaultGroup, default='translate')
def cli():
    pass

@cli.command(help='query and translate words')
@click.argument('words', nargs=-1)
def translate(words):
    if not words:
        click.secho("enter words(请输入单词)", fg='red')
        return
    query = ' '.join(words)
    result = get_response_json(query)
    show_result(result)

@cli.command(help='show query history')
@click.option('--d', is_flag=True, help='clear history')
def history(d):
    exist = os.path.exists("history.txt")
    if not exist:
        return
    if d:
        subprocess.call("rm history.txt", shell=True)
        return
    subprocess.call("cat history.txt", shell=True)

if __name__ == '__main__':
    cli()
