<div align="center">

# RoboBill

**AI-powered invoice analyzer — upload, ask, get instant insights.**

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_AI-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

*Built for **IEEE WIE x GraVITas '24***

</div>

---

## How it works

```
Upload invoice image (JPG/PNG)
        │
        ▼
  Ask a question ──► Gemini 1.5 Flash (multimodal)
        │
        ▼
  Extracted insights: line items, totals, dates, vendor info
```

Upload any invoice image, ask a natural language question about it, and RoboBill uses Google's Gemini 1.5 Flash to extract and analyze the data instantly.

## Features

- Upload invoice images (JPG, JPEG, PNG)
- Ask natural language questions about the invoice
- AI extracts line items, totals, dates, vendor info, and more
- Powered by Gemini 1.5 Flash for fast multimodal analysis

<!-- 📸 Add a screenshot: take a screenshot of the app and save it as docs/screenshot.png
![RoboBill Screenshot](docs/screenshot.png)
-->

## Quick Start

### Prerequisites

- Python 3.9+
- A [Google AI Studio](https://aistudio.google.com/app/apikey) API key

### Setup

```bash
git clone https://github.com/gitswagata1/AIGENDA.git
cd AIGENDA
pip install -r requirements.txt
```

Set your API key as an environment variable:

```bash
# Linux / macOS
export GOOGLE_API_KEY="your-api-key-here"

# Windows PowerShell
$env:GOOGLE_API_KEY="your-api-key-here"
```

### Run

```bash
streamlit run streamlit_app.py
```

Open [localhost:8501](http://localhost:8501) in your browser.

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| AI Model | Google Gemini 1.5 Flash |
| Image Processing | Pillow |
| Language | Python 3.9+ |

## Project Structure

```
AIGENDA/
├── streamlit_app.py   # Main application
├── requirements.txt   # Pinned Python dependencies
├── .gitignore         # Python artifacts + secrets
├── LICENSE            # MIT
└── README.md
```

## License

[MIT](LICENSE)

---

Built by [Swagata Banerjee](https://github.com/gitswagata1) · [LinkedIn](https://linkedin.com/in/theswagata1)
