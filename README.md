# QR Code Generator — Web App

A simple Flask web application that generates a QR code from any link or text entered by the user. Built with a clean, glassmorphism-style UI.

## Features

- Paste any link or text and generate a QR code instantly
- QR code is generated in memory (no files saved to disk)
- Download the generated QR code as a PNG
- Modern frosted-glass UI with a custom background image

## Tech Stack

- **Backend:** Python, Flask
- **QR Generation:** `qrcode` + `Pillow`
- **Frontend:** HTML, CSS (Jinja2 templating)

## Project Structure

```
qr-web-app/
├── app.py
├── requirements.txt
├── static/
│   └── background.jpg
└── templates/
    └── index.html
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Machagiri09/QR-CODE-GENERATION.git
cd QR-CODE-GENERATION
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the Flask app:

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

Paste a link or text into the input box and click **Generate**. The QR code will appear below the input, with an option to download it as a PNG.

## How It Works

1. The user submits a link through the form on the homepage.
2. Flask redirects to the same page with the link passed as a query parameter.
3. The `/qrcode` route generates a QR code in memory using the `qrcode` library.
4. The image is streamed directly to the browser as a PNG — no files are written to disk.
5. The frontend displays the QR code inside a glass-style card, with a download link.

## Routes

| Route | Method | Description |
|-------|--------|--------------|
| `/` | GET, POST | Renders the homepage and handles link submission |
| `/qrcode?link=...` | GET | Returns the generated QR code as a PNG image |

## Possible Improvements

- Add input validation for malformed URLs
- Add a "copy link" button
- Support custom QR colors or logos
- Deploy to a platform like Render, Railway, or PythonAnywhere

## License

This project is open source and available for personal or educational use.
