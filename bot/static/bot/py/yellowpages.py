import http.client

def query_yp(concept, location):
    conn = http.client.HTTPConnection("hackaton.ypcloud.io")

    payload = "  { \"search\":[{\r\n   \"searchType\":\"PROXIMITY\",\r\n   \"collection\":\"MERCHANT\",\r\n   \"what\": \"" + concept + "\",\r\n   \"where\":{\r\n   \"type\":\"GEO\",\r\n   \"value\":\"" + location + "\" }\r\n   }]}"

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
        'postman-token': "07235209-1a3f-8e1c-a02e-505e42f2e5f9"
    }

    conn.request("POST", "/search", payload, headers)

    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))