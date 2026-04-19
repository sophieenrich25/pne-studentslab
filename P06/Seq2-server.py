import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from P01.Seq1 import Seq
PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

def sequence_info(seq):
    length = len(seq)
    a = seq.count('A')
    t = seq.count('T')
    c = seq.count('C')
    g = seq.count('G')
    if length == 0:
        return "Empty sequence"

    pa = round((a / length) * 100, 2)
    pt = round((t / length) * 100, 2)
    pc = round((c / length) * 100, 2)
    pg = round((g / length) * 100, 2)

    return f"""
    Length: {length}<br>
    A: {a} ({pa}%)<br>
    T: {t} ({pt}%)<br>
    C: {c} ({pc}%)<br>
    G: {g} ({pg}%)
    """
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        termcolor.cprint(self.requestline, 'green')

        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        sequences = ["AAATGCATGCC", "TTCCGACGAT", "GAGACATGA", "TCTCTCGCATGACT", "GATTCAAACTGAAAA"]
        genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]

        if path == "/":
            contents = Path('html/index.html').read_text()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
            self.wfile.write(contents.encode())

        elif path == "/ping":
            contents = Path('html/ping.html').read_text()
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
            self.wfile.write(contents.encode())

        elif path == "/GET":
            if "n" in arguments:
                n = int(arguments.get('n')[0])
                seq = sequences[n]
                template = Path('html/get.html').read_text()
                contents = template.format(n=n, sequence=seq)
            else:
                contents = "<h1>Error: Sequence not found</h1>"
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
            self.wfile.write(contents.encode())

        elif path == "/GENE":
            if "gene" in arguments:
                gene = arguments.get('gene')[0]

                if gene in genes:
                    FOLDER = "../S04/sequences/"
                    filename = FOLDER + gene + ".txt"

                    s = Seq()
                    gen = s.read_fasta(filename)

                    template = Path('html/GENE.html').read_text()
                    contents = template.format(gene=gene, gen=gen)
                else:
                    contents = "<h1>Error: Gene not found</h1>"
            else:
                contents = "<h1>Error: No gene provided</h1>"

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
            self.wfile.write(contents.encode())

        elif path == "/OPERATION":
            seq = arguments.get("sequence", [""])[0].upper()
            operation = arguments.get("operation", [""])[0]
            sequence = Seq(seq)
            sequence_str = seq
            if operation == "Info":
                result = sequence_info(seq)
            elif operation == "Comp":
                result = sequence.complement()
            elif operation == "Rev":
                result = sequence.reverse()
            else:
                result = "Invalid operation"
            template = Path('html/operation.html').read_text()
            contents = template.format(sequence=sequence_str, operation=operation, result=result)

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(contents.encode()))
            self.end_headers()
            self.wfile.write(contents.encode())
        else:
            contents = Path('html/error.html').read_text()

            self.send_response(200)
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