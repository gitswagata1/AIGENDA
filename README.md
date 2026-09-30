# RoboBill

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini_AI-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

AI-powered invoice analyzer built with Google Gemini and Streamlit. Upload an invoice image, ask a question, and get instant AI-extracted insights.

Built for **IEEE WIE x GraVITas '24**.

## Features

- Upload invoice images (JPG, JPEG, PNG)
- Ask natural language questions about the invoice
- AI extracts line items, totals, dates, vendor info, and more
- Powered by Gemini 1.5 Flash for fast multimodal analysis

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

Create a `.env` file or set the environment variable:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

> **Note:** Never hardcode API keys. Use environment variables or a `.env` file.

### Run

```bash
streamlit run streamlit_app.py
```

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Frontend | Streamlit |
| AI Model | Google Gemini 1.5 Flash |
| Image Processing | Pillow |
| Language | Python |

## Project Structure

```
AIGENDA/
  streamlit_app.py   # Main application
  requirements.txt   # Python dependencies
  .streamlit/        # Streamlit config
```

## Author

**Swagata Banerjee** — [GitHub](https://github.com/gitswagata1) | [LinkedIn](https://linkedin.com/in/theswagata1)
