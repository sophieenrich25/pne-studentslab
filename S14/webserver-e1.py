import http.server
import socketserver
import termcolor

PORT = 8081

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        print("GET received! Request line:")

        termcolor.cprint("  " + self.requestline, 'green')
        print("  Command: " + self.command)
        print("  Path: " + self.path)

        if self.path == "/":
            self.send_response(200)  # OK
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Welcome to my server")
        else:
            # For any other path, respond with an error message
            self.send_response(404)  # Not Found
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Resource not available")
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
