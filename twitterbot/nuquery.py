import json
import http.client
# Acces keys import
from keys import keysN

def query_nuance(query):
    # API's url
    url = "nim-rd.nuance.mobi:9443"
    extension = "/nina-webapi/NinaDoNLU"
    # Headers data
    nluEngine = 'NLE'
    companyName = keysN[0]
    appName = keysN[1]
    cloudModelVersion = '1.0.14'
    user = keysN[2]
    # connection data
    contentType = 'application/json'
    nmaid = keysN[3]
    nmaidkey = keysN[4]
    postman_token = keysN[5]

    print("I'm doing it")
    # Create a connection
    conn = http.client.HTTPSConnection(url)
    # Generate request's body
    payload = "{ \"text\":\"" + query + "\",\n\"nlu_engine\":\"NLE\",\n\"companyName\":\"" + companyName + "\",\n\"appName\":\"" + appName + "\",\n\"cloudModelVersion\":\"1.0\",\n\"user\":\"" + user + "\"\n}"
    # Establish the request's headers
    headers = {
        'content-type': "application/json",
        'nmaid': nmaid,
        'nmaidkey': nmaidkey,
        'cache-control': "no-cache",
        'postman-token': postman_token
    }

    # Make the request
    conn.request("POST", extension, payload, headers)

    # Gather the results
    res = conn.getresponse()
    data = res.read()
    jobject = json.loads(data.decode("utf-8"))

    return ( jobject['QueryResult']['results'][0]['intent'] )

# print(query_nuance("I'm sick"))
