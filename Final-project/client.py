import http.client
import json

PORT = 8080
SERVER = "localhost"

def client(endpoint):
    conn =http.client.HTTPConnection("localhost", 8080)
    conn.request("GET", endpoint)

    r = conn.getresponse()
    data = r.read().decode()

    if r.status == 200:
        print(f"/URL{endpoint}")
        print(json.loads(data))
    else:
        print(f"Error: {r.status}")
    conn.close()

client("/geneLookup?gene=FRAT1&json=1")
client("/chromosomeLength?species=mouse&chromo=18&json=1")
client("/karyotype?species=mouse&json=1")
client("/listSpecies?limit=10&json=1")
client("/geneCalc?gene=FRAT1&json=1")
client("/geneInfo?gene=FRAT1&json=1")