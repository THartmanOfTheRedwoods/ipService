import http.server
import socketserver
import urllib.request


class ProxyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        client_ip = self.client_address[0]
        headers = {
            "User-Agent": "MyCustomAgent/1.0",
            "Content-Type": "application/json",
            "X-Forwarded-For": client_ip
        }
        url = 'http://127.0.0.1:8091'

        req = urllib.request.Request(url, headers=headers, method='GET')
        self.copyfile(urllib.request.urlopen(req), self.wfile)

if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), ProxyRequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()