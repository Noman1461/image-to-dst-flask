# Image to DST Embroidery Converter (PoC)

A Flask-based web application that converts raster images (PNG/JPG) into machine-readable DST embroidery files using classical computer vision techniques.

This project is built as a **proof of concept** for automated embroidery digitization, focusing on simple logo-style images.

---

## 🚀 Features

- Upload a single image (PNG/JPG, max 10 MB)
- Convert image into DST embroidery format
- Download generated DST file
- Minimal web interface
- Modular Flask architecture
- Uses classical CV (no ML)

---

## 🧠 How It Works (High-Level)

1. Image is uploaded via Flask UI
2. Image preprocessing (grayscale, blur, threshold)
3. Contour extraction using OpenCV
4. Contours converted into stitch paths
5. Stitch paths written into DST format using PyEmbroidery

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Image Processing:** OpenCV, NumPy
- **Embroidery Format:** PyEmbroidery (DST)
- **Frontend:** HTML (minimal)
- **Deployment Target:** Render

---

## 📁 Project Structure

embroidery-project/
├── app/
│ ├── init.py
│ ├── routes.py
│ ├── services/
│ │ ├── image_processing.py
│ │ ├── stitch_generator.py
│ │ └── dst_writer.py
│ ├── static/
│ │ └── uploads/
│ └── templates/
│ └── index.html
├── run.py
├── requirements.txt
├── .gitignore
└── README.md

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/<your-username>/image-to-dst-flask.git
cd image-to-dst-flask
```

### 2. Create Virtual Environment
python -m venv venv

### 3. Activate Environment
#### Windows
venv\Scripts\activate

#### macOS / Linux
source venv/bin/activate

### 4. Install Dependencies
pip install -r requirements.txt

### Open browser at:

http://127.0.0.1:5000