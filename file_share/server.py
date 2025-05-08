# file_server.py
import socket
import threading
import os

HOST = '127.0.0.1'
PORT = 5001
SAVE_DIR = 'received_files'

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def handle_client(conn, addr):
    print(f"[TERHUBUNG] {addr}")
    try:
        filename = conn.recv(1024).decode()
        conn.send(b"OK")
        filesize = int(conn.recv(1024).decode())
        conn.send(b"OK")
        
        filepath = os.path.join(SAVE_DIR, os.path.basename(filename))
        with open(filepath, 'wb') as f:
            bytes_read = 0
            while bytes_read < filesize:
                data = conn.recv(4096)
                if not data:
                    break
                f.write(data)
                bytes_read += len(data)
        print(f"[TERIMA] File disimpan: {filepath}")
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        conn.close()

def start_server():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()
    print(f"[SERVER] Menunggu file di {HOST}:{PORT}...")

    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    start_server()
