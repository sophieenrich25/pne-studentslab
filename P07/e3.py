import http.client
import json
import termcolor

SERVER = "rest.ensembl.org"
ENDPOINT = "sequence/id/"
GENE_ID = "ENSG00000207552"
PARAMS = "?content-type=application/json"
RESOURCE = ENDPOINT + GENE_ID + PARAMS

print()
print(f"SERVER: {SERVER}")
print(f"URL: {SERVER}{RESOURCE}")

conn = http.client.HTTPSConnection(SERVER)
try:
    conn.request("GET", RESOURCE)
    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

if r1.status == 200:
    data = r1.read().decode("utf-8")
    gene_data = json.loads(data)
    termcolor.cprint("Gene:", color="green", end=" ")
    print("MIR633")

    termcolor.cprint("Description:", color="green", end=" ")
    print(gene_data.get("desc"))

    termcolor.cprint("Bases:", color="green", end=" ")
    print(gene_data.get("seq"))

else:
    print(f"Error: {r1.status}")

conn.close()