from http.server import BaseHTTPRequestHandler
from datetime import datetime
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        # Set headers
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        # Fetch the data
        dn42_roas = requests.get(
            "https://dn42.burble.com/roa/dn42_roa_bird2_6.conf")

        # Write bird-style ROA data
        data = "# Cached by roa.va3zza.com on " + \
            datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        data += dn42_roas
        self.wfile.write(data.encode())
