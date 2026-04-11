from pathlib import Path
import http.server
import socketserver
import termcolor

PORT = 8080
error_page = "error.html"

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print("GET received! Request line:")
        termcolor.cprint("  " + self.requestline, 'green')
        print("  Command: " + self.command)
        path = self.path

        if path == "/" or path == "/index.html":
            file_path = Path("html/index.html")

        elif path.startswith("/info/"):
            file_path = Path("html" + path)

        else:
            file_path = Path("html" + path)

        if file_path.is_file():
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            try:
                with file_path.open('rb') as file:
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"File not found")
        else:
            error_path = Path("html/error.html")
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            try:
                with open(error_path, 'rb') as file:
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Error page not found")

        return


Handler = TestHandler

with socketserver.TCPServer(("localhost", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()