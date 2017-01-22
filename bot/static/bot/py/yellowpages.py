import json
import http.client

def query_yp(query):

    conn = http.client.HTTPConnection("hackaton.ypcloud.io")

    payload = "  { \"search\":[{\r\n   \"searchType\":\"PROXIMITY\",\r\n   \"collection\":\"MERCHANT\",\r\n   \"what\": \"" + query + "\",\r\n   \"where\":{\r\n   \"type\":\"GEO\",\r\n   \"value\":\"45.4754418,-73.5863705\" }\r\n   }]}"

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "07235209-1a3f-8e1c-a02e-505e42f2e5f9"
        }

    conn.request("POST", "/search", payload, headers)

    res = conn.getresponse()
    data = res.read()
    jobject = json.loads(data.decode("utf-8"))

    # TODO: So far, it only returns the intent. Escalate when the model is more capable
    return jobject['searchResult'][0]['merchants']

#print(json.dumps(query_yp("car"), sort_keys=True, indent=4, separators=(',', ': ')))