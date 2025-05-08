
## Tugas Kelompok PJAR

Anggota:

1. **Alfian Ananda** – **50421111**
2. **Abubakar Haziq Alaydrus** – **50421017**
3. **Mikael Agung Dwi Saputra Djawa** – **50421814**
4. **Muhammad Azra Davis** - **50421926**
5. **Muhammad Rizqi Fajri** – **51421069**

---

## 📦 File Sharing, Video Streaming, & Chat App (Python GUI)

Proyek ini berisi tiga aplikasi GUI berbeda:

1. **Video Streaming App** – Streaming video dari server ke client.
2. **Chat App** – Chat dua arah berbasis socket.
3. **File Share App** – Kirim dan terima file antar client.

---

## 🛠️ Setup

### 1. Buat Virtual Environment

```bash
python -m venv myenv
```

### 2. Aktifkan Virtual Environment

- **Windows:**

```bash
myenv\Scripts\activate
```

- **macOS/Linux:**

```bash
source myenv/bin/activate
```

### 3. Install Dependensi

> Pastikan ada file `requirements.txt` berisi semua dependensi yang dibutuhkan. Misalnya:

```
tk
```

Install:

```bash
pip install -r requirements.txt
```

---

## ▶️ Cara Menjalankan

### 1. 📽️ Video Streaming App

**Struktur:**

```
video_streaming/
├── client.py      # GUI pemutar video
├── server.py      # Server HTTP yang menyajikan file video
└── videos/
    └── video.mp4  # Video yang ingin di-stream
```

**Langkah:**

- Jalankan server:

```bash
cd video_streaming
python server.py
```

- Di terminal lain, jalankan client:

```bash
python client.py
```

- Client akan menampilkan GUI dan menampilkan daftar video dari folder `videos`.

---

### 2. 💬 Chat App

**Struktur:**

```
chat_app/
├── client.py
└── server.py
```

**Langkah:**

- Jalankan server:

```bash
cd chat_app
python server.py
```

- Jalankan 2 instance `client.py` (dua terminal terpisah) untuk dua pengguna:

```bash
python client.py
```

- Mulai chat antar pengguna.

---

### 3. 📁 File Share App

**Struktur:**

```
file_share/
├── client.py
└── server.py
```

**Langkah:**

- Jalankan server untuk menerima file:

```bash
cd file_share
python server.py
```

- Jalankan client untuk memilih dan mengirim file:

```bash
python client.py
```

---
