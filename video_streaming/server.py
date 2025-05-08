import http.server
import socketserver
import os

PORT = 8000
DIRECTORY = "videos"

# Pastikan folder ada
if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)
    print(f"Folder '{DIRECTORY}' dibuat.")

# Ubah direktori ke folder video
os.chdir(DIRECTORY)

# Buat server HTTP sederhana
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server berjalan di http://localhost:{PORT}")
    print("Tekan Ctrl+C untuk keluar")
    httpd.serve_forever()