import http.client
import termcolor
import http.server
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json

PORT = 8080
class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        SERVER = "rest.ensembl.org"
        PARAMS = "?content-type=application/json"


        if path == "/":
            contents = Path('main_page.html').read_text()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
            self.wfile.write(contents.encode())

        elif path == "/listSpecies":
            conn = http.client.HTTPSConnection(SERVER)
            endpoint = "/info/species"
            RESOURCE = endpoint + PARAMS
            try:
                conn.request("GET", RESOURCE)
                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            if r1.status == 200:
                response = r1.read().decode("utf-8")
                data = json.loads(response)
                species = data["species"]

                limit = arguments.get("limit", [None])[0]
                if limit and limit.isdigit():
                    species = species[:int(limit)]
                else:
                    limit = len(species)

                species_list = data["species"][:int(limit)]
                names_list = []
                for i in species_list:
                    name = i["display_name"]
                    names_list.append(name)
                for name in names_list:
                    names_list += f"<li>{name}</li>"

                contents = Path('listSpecies.html').read_text()
                result = contents.format(
                    total_species=len(data["species"]),
                    limit_value=limit,
                    species_list=names_list
                )
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(result.encode()))
                self.end_headers()
                self.wfile.write(result.encode())

        elif path == "/karyotype":
            conn = http.client.HTTPSConnection(SERVER)
            endpoint = "/info/assembly
            RESOURCE = endpoint + PARAMS
            try:
                conn.request("GET", RESOURCE)
                r1 = conn.getresponse()
                print(f"Response received!: {r1.status} {r1.reason}\n")
            except ConnectionRefusedError:
                print("ERROR! Cannot connect to the Server")
                exit()

            if r1.status == 200:
                response = r1.read().decode("utf-8")
                data = json.loads(response)
                species = data["species"]

                limit = arguments.get("limit", [None])[0]
                if limit and limit.isdigit():
                    species = species[:int(limit)]
                else:
                    limit = len(species)

                species_list = data["species"][:int(limit)]
                names_list = []
                for i in species_list:
                    name = i["display_name"]
                    names_list.append(name)
                for name in names_list:
                    names_list += f"<li>{name}</li>"

                contents = Path('listSpecies.html').read_text()
                result = contents.format(
                    total_species=len(data["species"]),
                    limit_value=limit,
                    species_list=names_list
                )
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.send_header('Content-Length', len(result.encode()))
                self.end_headers()
                self.wfile.write(result.encode())


        else:
            contents = Path('error.html').read_text()

            self.send_response(404)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
            self.wfile.write(contents.encode())
        return

Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()