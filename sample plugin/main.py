import json
from urllib.parse import urlsplit, parse_qs
import quart
import quart_cors
from quart import request
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

app = quart_cors.cors(quart.Quart(__name__), allow_origin=config.get("ORIGIN"))

@app.get("/search")
async def search():
    query = urlsplit(quart.request.url).query
    params = parse_qs(query)
    question = params["query"][0]
    url = config.get("OPENAI_URL")
    myobj = {'dataSources': [{'type':'AzureCognitiveSearch','parameters':{'endpoint':config.get("COGSEARCH_ENDPOINT"), 'key':config.get("COGSEARCH_APIKEY"), 'indexName':config.get("COGSEARCH_INDEX")}}],
            'messages':[{'role':'user', 'content':question}]}
    headers = {'ContentType':'application/json','api-key':config.get("OPENAI_URL")}
    x = requests.post(url, json = myobj, headers=headers)
    response = json.loads(x.content)
    
    return quart.Response(response=json.dumps({'response':response}), status=200)


@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
