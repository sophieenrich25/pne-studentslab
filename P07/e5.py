import http.client
import json
import termcolor
from P01.Seq1 import Seq
genes = {
    "FRAT1": "ENSG00000165879.9",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6-269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

for gene in genes:
    GENE_ID = genes[gene].split('.')[0]

    SERVER = "rest.ensembl.org"
    ENDPOINT = "sequence/id/"
    PARAMS = "?content-type=application/json"
    RESOURCE = ENDPOINT + GENE_ID + PARAMS
    URL = f"https://{SERVER}/{RESOURCE}"


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
        print(gene)

        termcolor.cprint("Description:", color="green", end=" ")
        print(gene_data.get("desc"))

        sequence = Seq(gene_data.get("seq"))
        termcolor.cprint("Total length:", color="green", end=" ")
        print(sequence.len())

        most_frequent_base = None
        most_frequent_count = 0

        base_counts = sequence.count()
        for base, count in base_counts.items():
            termcolor.cprint(f"{base}:", color= "blue", end=" ")
            percentage = (count / sum(base_counts.values())) * 100
            print(f"{count} ({percentage:.2f}%)")

            if count > most_frequent_count:
                most_frequent_count = count
                most_frequent_base = base
        termcolor.cprint(f"Most frecuent base:", color="green",  end="")
        print(most_frequent_base)


    else:
        print(f"Error: {r1.status}")

    conn.close()