import http.server
import socketserver
import termcolor

PORT = 8081
main_page = "index.html"
error_page = "error.html"

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        print("GET received! Request line:")

        termcolor.cprint("  " + self.requestline, 'green')
        print("  Command: " + self.command)
        print("  Path: " + self.path)

        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)  # OK
            self.send_header("Content-type", "text/html")  # Content-type HTML
            self.end_headers()
            try:
                with open(main_page, 'rb') as file:
                    self.wfile.write(file.read())  # Escribe el contenido de index.html
            except FileNotFoundError:
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"index.html not found")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            try:
                with open(error_page, 'rb') as file:
                    self.wfile.write(file.read())
            except FileNotFoundError:
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"error.html not found")
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