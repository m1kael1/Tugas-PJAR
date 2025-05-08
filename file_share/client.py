# file_client.py
import socket
import os
import tkinter as tk
from tkinter import filedialog, messagebox

HOST = '127.0.0.1'
PORT = 5001

class FileSenderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("File Sender")

        self.label = tk.Label(master, text="Pilih file untuk dikirim:")
        self.label.pack(pady=5)

        self.select_button = tk.Button(master, text="Pilih File", command=self.select_file)
        self.select_button.pack(pady=5)

        self.send_button = tk.Button(master, text="Kirim", command=self.send_file, state=tk.DISABLED)
        self.send_button.pack(pady=10)

        self.status_label = tk.Label(master, text="", fg="green")
        self.status_label.pack()

        self.filepath = ""

    def select_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.filepath = path
            self.status_label.config(text=f"File dipilih: {os.path.basename(path)}", fg="blue")
            self.send_button.config(state=tk.NORMAL)

    def send_file(self):
        if not self.filepath:
            return

        try:
            filesize = os.path.getsize(self.filepath)
            s = socket.socket()
            s.connect((HOST, PORT))

            # Kirim nama file
            s.send(os.path.basename(self.filepath).encode())
            s.recv(1024)

            # Kirim ukuran file
            s.send(str(filesize).encode())
            s.recv(1024)

            # Kirim isi file
            with open(self.filepath, 'rb') as f:
                while (chunk := f.read(4096)):
                    s.sendall(chunk)

            s.close()
            self.status_label.config(text="File berhasil dikirim!", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Gagal mengirim: {e}", fg="red")

if __name__ == '__main__':
    root = tk.Tk()
    app = FileSenderApp(root)
    root.mainloop()
