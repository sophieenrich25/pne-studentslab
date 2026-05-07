import http.client
import termcolor
import http.server
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json
import jinja2 as j
from jinja2 import Template

PORT = 8080
class TestHandler(http.server.BaseHTTPRequestHandler):

    def read_html_file(self, filename):
        try:
            path = Path("html/" + filename)
            contents = path.read_text()
            return j.Template(contents)
        except FileNotFoundError:
            print("Error: File not found.")
            return None

    def render_template(self, filename, context):
        template = self.read_html_file(filename)
        if template:
            result = template.render(context=context)
            self.send_html_response(result)
        else:
            self.error()

    def get_ensembl_json(self, endpoint):
        PARAMS = "?content-type=application/json"
        RESOURCE = endpoint + PARAMS
        conn = http.client.HTTPSConnection("rest.ensembl.org")
        try:
            conn.request("GET", RESOURCE)
            r = conn.getresponse()
            if r.status == 200:
                response = r.read().decode("utf-8")
                data = json.loads(response)
                return data
        except ConnectionRefusedError:
            return "ERROR! Cannot connect to the Server"
        return None

    def send_html_response(self, contents, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())

    def html_lists(self, items):
        html_str = ""
        for i in items:
            html_str += f"<li>{i}</li>"
        return html_str

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)

        if path == "/":
            contents = Path('html/main_page.html').read_text()
            self.send_html_response(contents)
        elif path == "/listSpecies":
            self.listSpecies(arguments)
        elif path == "/karyotype":
            self.karyotype(arguments)
        elif path == "/chromosomeLength":
            self.chromosomeLength(arguments)
        else:
            self.error()

    def error(self):
        contents = Path('html/error.html').read_text()
        print("Error")
        return self.send_html_response(contents)

    def listSpecies(self, arguments):
        data = self.get_ensembl_json("/info/species")

        if data:
            all_species = data["species"]

            limit = arguments.get("limit")
            if limit and str(limit).isdigit():
                limit = int(limit)
                selected_species = all_species[:limit]
            else:
                limit = len(all_species)
                selected_species = all_species

            names_list = [s["display_name"] for s in selected_species]

            template = Template(self.read_html_file("listSpecies.html"))
            result = template.render(context={
                "total_species" : len(all_species),
                "limit_value" : limit,
                "species_list" : names_list
            })
            self.send_html_response(result)
        else:
            self.error()
            print("Error: Ensembl data could not be obtained")

    def karyotype(self, arguments):
        specie_selected = arguments.get("species", [None])[0]
        data = self.get_ensembl_json(f"/info/assembly/{specie_selected}")
        if data:
            regions = data["top_level_region"]
            names_list = [region["name"] for region in regions]

            names_html = self.html_lists(names_list)

            template = self.read_html_file("karyotype.html")
            result = template.render(context={
                "names_list" : names_html,
            })

            self.send_html_response(result)

        else:
            self.error()
            print("Error: Ensembl data could not be obtained")


    def chromosomeLength(self, arguments):
        specie_selected = arguments.get("species", [None])[0]
        chromosome_selected = arguments.get("chromosome", [None])[0]
        data = self.get_ensembl_json(f"/info/assembly/{specie_selected}")

        if data:
            regions = data["top_level_region"]
            length = None

            for region in regions:
                if str(region["name"]).strip() == str(chromosome_selected).strip():
                    length = region["length"]
                break

            if length:
                template = self.read_html_file("chromosomeLength.html")
                result = template.render(context={
                    "length_chromosome": length,
                })

                self.send_html_response(result)
                print(f"{length}")
            else:
                self.error()
        else:
            self.error()
            print("Error: Ensembl data could not be obtained")



Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()