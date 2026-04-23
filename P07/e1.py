import http.client
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"SERVER: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPSConnection(SERVER)
try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()
r1 = conn.getresponse()

print(f"Response received!: {r1.status} {r1.reason}\n")

data1 = r1.read().decode("utf-8")

response = json.loads(data1)

if response.get("ping") == 1:
    print("PING OK! The database is running!")
else:
    print("Error: not database response")

conn.close()