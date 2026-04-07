from pathlib import Path
import http.server
import socketserver
import termcolor

PORT = 8081
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

        file_path = Path(self.path.lstrip('/'))

        # Check if the file exists in the current directory
        if file_path.is_file():
            self.send_response(200)  # OK
            self.send_header("Content-type", "text/html")  # Assuming HTML files for now
            self.end_headers()
            try:
                with file_path.open('rb') as file:
                    self.wfile.write(file.read())  # Serve the requested file
            except FileNotFoundError:
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"File not found")
        else:
            # If the file doesn't exist, serve error.html
            self.send_response(404)  # Not Found
            self.send_header("Content-type", "text/html")  # Serve error.html with HTML content type
            self.end_headers()
            try:
                with open(error_page, 'rb') as file:
                    self.wfile.write(file.read())  # Serve error.html
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