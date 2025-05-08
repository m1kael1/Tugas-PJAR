# chat_client.py
import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

HOST = '127.0.0.1'
PORT = 12345

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Client Chat")

        self.text_area = scrolledtext.ScrolledText(master, state='disabled', wrap='word')
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(master)
        self.entry.pack(fill=tk.X, padx=10)
        self.entry.bind("<Return>", self.send_msg)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((HOST, PORT))
        except:
            self.append_text("Tidak bisa terhubung ke server.")
            return

        self.username = simpledialog.askstring("Nama", "Masukkan nama Anda:", parent=master)
        if not self.username:
            self.username = "Anonim"

        self.append_text(f"[TERHUBUNG sebagai {self.username}]")

        threading.Thread(target=self.receive_messages, daemon=True).start()

    def send_msg(self, event=None):
        msg = self.entry.get()
        if msg:
            full_msg = f"{self.username}: {msg}"
            try:
                self.sock.send(full_msg.encode('utf-8'))
                self.append_text(full_msg)  # Tampilkan juga pesan sendiri
            except:
                self.append_text("[Gagal mengirim pesan]")
            self.entry.delete(0, tk.END)

    def receive_messages(self):
        while True:
            try:
                msg = self.sock.recv(1024).decode('utf-8')
                if msg:
                    self.append_text(msg)
            except:
                break

    def append_text(self, msg):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, msg + '\n')
        self.text_area.yview(tk.END)
        self.text_area.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()