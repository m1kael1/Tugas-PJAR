import tkinter as tk
from tkinter import ttk
import urllib.request
import threading
import cv2
from PIL import Image, ImageTk

class VideoStreamClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Streaming Client")
        self.root.geometry("800x600")

        self.server_url = "http://localhost:8000"
        self.stop_flag = False

        self.create_ui()

    def create_ui(self):
        top = ttk.Frame(self.root)
        top.pack(pady=5, fill=tk.X)

        ttk.Label(top, text="Server URL:").pack(side=tk.LEFT)
        self.url_entry = ttk.Entry(top, width=50)
        self.url_entry.insert(0, self.server_url)
        self.url_entry.pack(side=tk.LEFT, padx=5)
        ttk.Button(top, text="Refresh", command=self.refresh_video_list).pack(side=tk.LEFT)

        content = ttk.Frame(self.root)
        content.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        left = ttk.Frame(content)
        left.pack(side=tk.LEFT, fill=tk.Y)

        ttk.Label(left, text="Daftar Video").pack()
        self.video_list = tk.Listbox(left, width=30)
        self.video_list.pack(fill=tk.Y)
        self.video_list.bind('<Double-Button-1>', self.on_select)

        right = ttk.Frame(content)
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.video_label = ttk.Label(right)
        self.video_label.pack(fill=tk.BOTH, expand=True)

        ttk.Button(right, text="Stop", command=self.stop_video).pack(pady=10)

    def refresh_video_list(self):
        self.server_url = self.url_entry.get().strip()
        self.video_list.delete(0, tk.END)
        try:
            with urllib.request.urlopen(self.server_url) as response:
                html = response.read().decode("utf-8", errors="ignore")
                for line in html.splitlines():
                    if ".mp4" in line.lower():
                        start = line.find('<a href="') + 9
                        end = line.find('"', start)
                        filename = line[start:end]
                        self.video_list.insert(tk.END, filename)
        except Exception as e:
            self.video_list.insert(tk.END, f"Error: {e}")

    def on_select(self, event):
        self.stop_video()
        idx = self.video_list.curselection()
        if not idx:
            return
        filename = self.video_list.get(idx[0])
        full_url = f"{self.server_url.rstrip('/')}/{filename}"
        self.start_stream(full_url)

    def start_stream(self, url):
        def play():
            cap = cv2.VideoCapture(url)
            if not cap.isOpened():
                print("Tidak bisa membuka stream.")
                return
            self.stop_flag = False
            while not self.stop_flag:
                ret, frame = cap.read()
                if not ret:
                    break
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image=image)
                self.video_label.imgtk = photo
                self.video_label.config(image=photo)
                self.video_label.update()
            cap.release()

        threading.Thread(target=play, daemon=True).start()

    def stop_video(self):
        self.stop_flag = True
        self.video_label.config(image='')

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoStreamClient(root)
    root.mainloop()