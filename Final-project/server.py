import http.client
import urllib.parse
import termcolor
import http.server
import socketserver
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import json
import jinja2 as j
from textdistance import Length

from SeqClass import Seq

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
        conn = http.client.HTTPSConnection("rest.ensembl.org")
        try:
            conn.request("GET", endpoint + PARAMS)
            r = conn.getresponse()
            if r.status == 200:
                data = r.read().decode("utf-8")
                conn.close()
                return json.loads(data)
            else:
                print(f"Error ensembl: {r.status}")
        except ConnectionRefusedError:
            return "ERROR! Cannot connect to the Server"
        return None

    def get_ensembl_json_overlap(self, endpoint):
        PARAMS = "&content-type=application/json"
        conn = http.client.HTTPSConnection("rest.ensembl.org")
        try:
            conn.request("GET", endpoint + PARAMS)
            r = conn.getresponse()
            if r.status == 200:
                data = r.read().decode("utf-8")
                conn.close()
                return json.loads(data)
            else:
                print(f"Error ensembl: {r.status}")
        except ConnectionRefusedError:
            return "ERROR! Cannot connect to the Server"
        return None

    def send_html_response(self, contents):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(contents.encode())

    def html_lists(self, items):
        html_str = ""
        for i in items:
            html_str += f"<li>{i}</li>"
        return html_str

    def send_json_response(self, result):
        json_str = json.dumps(result)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json_str.encode())

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)
        path = url_path.path.rstrip("/")
        arguments = parse_qs(url_path.query)

        if path == "":
            contents = Path('html/main_page.html').read_text()
            self.send_html_response(contents)
        elif path == "/listSpecies":
            self.listSpecies(arguments)
        elif path == "/karyotype":
            self.karyotype(arguments)
        elif path == "/chromosomeLength":
            self.chromosomeLength(arguments)
        elif path == "/geneLookup":
            self.geneLookup(arguments)
        elif path == "/geneSeq":
            self.geneSeq(arguments)
        elif path == "/geneInfo":
            self.geneInfo(arguments)
        elif path == "/geneCalc":
            self.geneCalc(arguments)
        elif path == "/geneList":
            self.geneList(arguments)
        else:
            self.error()

    def error(self):
        contents = Path('html/error.html').read_text()
        print("Error")
        return self.send_html_response(contents)

    def listSpecies(self, arguments):
        data = self.get_ensembl_json("/info/species")
        is_json = arguments.get("json", ["0"])[0] == "1"
        if data:
            all_species = data["species"]

            limit = arguments.get("limit", [None])[0]
            if limit and limit.isdigit():
                limit = int(limit)
                selected_species = all_species[:limit]
            else:
                limit = len(all_species)
                selected_species = all_species

            names_list = [s["display_name"] for s in selected_species]

            context_result = {
                "total_species" : len(all_species),
                "limit_value" : limit,
                "species_list" : names_list
            }
            if is_json:
                self.send_json_response(context_result)
            else:
                template = self.read_html_file("listSpecies.html")
                result = template.render(context=context_result)
                self.send_html_response(result)
        else:
            self.error()
            print("Error: Ensembl data could not be obtained")

    def karyotype(self, arguments):
        specie_selected = arguments.get("species", [None])[0]
        if specie_selected:
            specie_selected = urllib.parse.quote(specie_selected)
        is_json = arguments.get("json", ["0"])[0] == "1"
        data = self.get_ensembl_json(f"/info/assembly/{specie_selected}")
        if data:
            regions = data["top_level_region"]
            names_list = [
                region["name"]
                for region in regions
                if region["coord_system"] == "chromosome"
            ]

            if is_json:
                context_result = {
                    "names_list": names_list
                }
                self.send_json_response(context_result)
            else:
                names_html = self.html_lists(names_list)
                context_result = {
                    "names_list": names_html
                }
                template = self.read_html_file("karyotype.html")
                result = template.render(context=context_result)
                self.send_html_response(result)

        else:
            self.error()
            print("Error: Ensembl data could not be obtained")

    def chromosomeLength(self, arguments):
        specie_selected = arguments.get("species", [None])[0]
        if specie_selected:
            specie_selected = urllib.parse.quote(specie_selected)
        is_json = arguments.get("json", ["0"])[0] == "1"
        chromosome_selected = arguments.get("chromo", [None])[0]

        data = self.get_ensembl_json(f"/info/assembly/{specie_selected}")

        if data:
            regions = data["top_level_region"]
            length = None

            for region in regions:
                if str(region["name"]).strip() == str(chromosome_selected).strip():
                    length = region["length"]
                    break

            if length:
                context_result = {
                    "length_chromosome": length
                }
            else:
                self.error()

            if is_json:
                self.send_json_response(context_result)
            else:
                template = self.read_html_file("chromosomeLength.html")
                result = template.render(context=context_result)
                self.send_html_response(result)

        else:
            self.error()

    def geneLookup(self, arguments):
        gene_selected = arguments.get("gene", [None])[0].strip().upper()
        is_json = arguments.get("json", ["0"])[0] == "1"
        data = self.get_ensembl_json(f"/lookup/symbol/homo_sapiens/{gene_selected}")

        if data:
            id = data["id"]
            context_result = {
                "stable_id": id
            }
            if is_json:
                self.send_json_response(context_result)
            else:
                template = self.read_html_file("geneLookup.html")
                result = template.render(context=context_result)
                self.send_html_response(result)
        else:
            self.error()


    def geneSeq(self, arguments):
        gene_selected = arguments.get("gene", [None])[0].strip().upper()
        is_json = arguments.get("json", ["0"])[0] == "1"
        data = self.get_ensembl_json(f"/lookup/symbol/homo_sapiens/{gene_selected}")

        if data:
            id = data["id"]
            seq_data = self.get_ensembl_json(f"/sequence/id/{id}")
            if seq_data:
                seq = seq_data["seq"]
                context_result = {
                    "sequence": seq
                }
            if is_json:
                self.send_json_response(context_result)
            else:
                template = self.read_html_file("geneSeq.html")
                result = template.render(context=context_result)
                self.send_html_response(result)
        else:
            self.error()

    def geneInfo(self, arguments):
        gene_selected = arguments.get("gene", [None])[0].strip().upper()
        is_json = arguments.get("json", ["0"])[0] == "1"
        data = self.get_ensembl_json(f"/lookup/symbol/homo_sapiens/{gene_selected}")
        if data:
            id = data["id"]
            start = data["start"]
            end = data["end"]
            length = int(end) - int(start)
            chrom = data["seq_region_name"]

            context_result = {
                "id" : id,
                "start" : start,
                "end" : end,
                "length" : length,
                "name" : chrom
            }
            if is_json:
                self.send_json_response(context_result)
            else:
                template = self.read_html_file("geneInfo.html")
                result = template.render(context=context_result)
                self.send_html_response(result)
        else:
            self.error()

    def geneCalc(self, arguments):
        gene_selected = arguments.get("gene", [None])[0].strip().upper()
        if not gene_selected:
            return self.error()
        is_json = arguments.get("json", ["0"])[0] == "1"
        data = self.get_ensembl_json(f"/lookup/symbol/homo_sapiens/{gene_selected}")
        if not data or "id" not in data:
            return self.error()

        gene_id = data["id"]

        seq_data = self.get_ensembl_json(f"/sequence/id/{gene_id}")
        if not seq_data or "seq" not in seq_data:
            return self.error()

        seq = seq_data["seq"]
        sequence = Seq(seq)
        length = sequence.len()
        dic_bases = sequence.count()

        p_A = (dic_bases["A"] / length) * 100
        p_T = (dic_bases["T"] / length) * 100
        p_G = (dic_bases["G"] / length) * 100
        p_C = (dic_bases["C"] / length) * 100

        context_result = {
            "length": length,
            "p_A": round(p_A, 2),
            "p_T": round(p_T, 2),
            "p_G": round(p_G, 2),
            "p_C": round(p_C, 2)
        }
        if is_json:
            self.send_json_response(context_result)
        else:
            template = self.read_html_file("geneCalc.html")
            result = template.render(context=context_result)
            self.send_html_response(result)

    def geneList(self, arguments):
        chromo = arguments.get("chromo", [None])[0]
        start = arguments.get("start", [None])[0]
        if start.isdigit():
            start = int(start)
        end = arguments.get("end", [None])[0]
        if end.isdigit():
            end = int(end)
        is_json = arguments.get("json", ["0"])[0] == "1"
        region = f"{chromo}:{start}-{end}"
        endpoint = f"/overlap/region/human/{region}?feature=gene"
        data = self.get_ensembl_json_overlap(endpoint)
        if data:
            names = []
            for gene in data:
                name = gene.get("external_name")
                if name:
                    names.append(name)
            if not names:
                names = "No genes overlapping in this region were found"

            names_html = self.html_lists(names)


            if is_json:
                context_result = {
                    "chromo": chromo,
                    "start": start,
                    "end": end,
                    "genes": names
                    }
                self.send_json_response(context_result)
            else:
                context_result = {
                    "chromo": chromo,
                    "start": start,
                    "end": end,
                    "genes": names_html
                }
                template = self.read_html_file("geneList.html")
                result = template.render(context=context_result)
                self.send_html_response(result)
        else:
            self.error()


Handler = TestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()