# import the http.server module
import http.server
import socketserver

#  defining a handler class that will handle incoming requests and respond with "Hello World".
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Hello World")


PORT = 8000
handler = MyHandler
with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()