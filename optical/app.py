from sanic import Sanic
from sanic.response import json, html, text
from elasticsearch import Elasticsearch
from jinja2 import Environment, PackageLoader


client = Elasticsearch(hosts=['elasticsearch'], http_auth=('elastic', 'changeme',))
env = Environment(loader=PackageLoader('app', 'templates'))

app = application = Sanic(__name__)

@app.route('/')
async def test(request):
    data = {'name': 'Aysin'}

    template = env.get_template('index.html')
    html_content = template.render(name=data["name"])
    # content=template.render(title='Sanic',people='David')
    return html(html_content)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
