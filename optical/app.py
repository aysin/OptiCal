from sanic import Sanic
from sanic.response import json
from elasticsearch import Elasticsearch


client = Elasticsearch(hosts=['elasticsearch'], http_auth=('elastic', 'changeme',))
app = Sanic()

@app.route("/")
async def test(request):
    return json({"hello": "world"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
