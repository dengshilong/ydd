import requests
import json
import click
API_URL = "http://fanyi.youdao.com/openapi.do?keyfrom=ydd-dict&key=1890264650&type=data&doctype=json&version=1.1"

s = """{"basic": {"explains": ["[试验] test", "measurement"], "phonetic": "cè shì"}, "query": "测试", "web": [{"key": "测试",
"value": ["Test", "test", "TST test"]}, {"key": "集成测试", "value": ["Integration testing", "Test d'intégration", "통합 시험"]},
{"key": "ANOVA测试", "value": ["Gage R&amp;R", "ANOVA gauge R&amp;R"]}], "translation": ["test"], "errorCode": 0}"""
s = json.loads(s)
print(s)
def show_result(s):
    error_code = s["errorCode"]
    if error_code == 0:
        print(s["basic"])
        # click.secho('Hello %s!' % "test", fg='red', underline=True)
    elif error_code == 20:
        print('too long text(要翻译的文本过长)')
    elif error_code == 30:
        print("can't tranlate text(无法进行有效的翻译)")
    elif error_code == 40:
        print("unsupport language(不支持的语言类型)")
    elif error_code == 50:
        print("useless api key(无效的key)")
    else:
        print("no result(无词典结果)")

show_result(s)
# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name', help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)

# if __name__ == '__main__':
#     hello()

def get_response_json(query):
    params = {"q": query}
    response = requests.get(API_URL, params=params)
    data = response.json()
    return data

@click.command()
@click.argument('words', nargs=-1)
def tranlate(words):
    query = ' '.join(words)
    print(query)
    """Simple program that greets NAME for a total of COUNT times."""
    result = get_response_json(query)
    show_result(result)

if __name__ == '__main__':
    tranlate()
