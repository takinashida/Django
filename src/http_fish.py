from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

from config import ROOT_DIR

class FishHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path.lstrip("/")
        file_path = Path(ROOT_DIR, path)

        if file_path.exists() and file_path.is_file():
            if file_path.suffix == ".css":
                content_type = "text/css"
            elif file_path.suffix == ".js":
                content_type = "application/javascript"
            elif file_path.suffix in [".png", ".jpg", ".jpeg", ".gif"]:
                content_type = f"image/{file_path.suffix[1:]}"
                mode = "rb"
            else:
                content_type = "text/html"
                mode = "r"

            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.end_headers()

            with open(file_path, mode if 'mode' in locals() else 'r', encoding="utf-8" if file_path.suffix in [".html", ".css", ".js"] else None) as f:
                content = f.read()
                if isinstance(content, str):
                    content = content.encode("utf-8")
                self.wfile.write(content)

        else:
            contacts = Path(ROOT_DIR, "html", "contact_page.html")
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            with open(contacts, "r", encoding="utf-8") as f:
                self.wfile.write(f.read().encode("utf-8"))

    def do_POST(self):
        print(self.headers)
        contacts = Path(ROOT_DIR, "html", "contact_page.html")
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        answer_len = int(self.headers.get("Content-Length", 0))
        contact_form = parse_qs(self.rfile.read(answer_len).decode("utf-8"))
        with open(contacts, "r", encoding="utf-8") as f:
            self.wfile.write(f.read().encode("utf-8"))
        print(contact_form)



serv = HTTPServer(("localhost", 8000), FishHandler)
serv.serve_forever()
serv.server_close()