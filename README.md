<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!--  AIGENDA — AI-Powered Invoice & Expense Analyzer                         -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

<div align="center">

[![header](https://capsule-render.vercel.app/api?type=waving&color=0:141e30,50:e44d26,100:f7b733&height=200&section=header&text=AIGENDA&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=AI-Powered%20Invoice%20%26%20Expense%20Analyzer&descAlignY=55&descSize=18&descColor=f0e6d3)](https://github.com/gitswagata1/AIGENDA)

**Upload an invoice image, ask a question, and let Google Gemini AI extract the answers instantly.**

<br/>

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/gitswagata1/AIGENDA?style=for-the-badge&color=f7b733)](https://github.com/gitswagata1/AIGENDA/stargazers)
[![Forks](https://img.shields.io/github/forks/gitswagata1/AIGENDA?style=for-the-badge&color=70a5fd)](https://github.com/gitswagata1/AIGENDA/network/members)
[![Issues](https://img.shields.io/github/issues/gitswagata1/AIGENDA?style=for-the-badge&color=e44d26)](https://github.com/gitswagata1/AIGENDA/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)

</div>

---

## What is AIGENDA?

AIGENDA (a.k.a. **RoboBill**) is a Streamlit web app that uses **Google Gemini 1.5 Flash** to analyze invoice and receipt images. Upload a photo of any bill, ask a natural-language question ("What's the total?", "List all line items", "Who is the vendor?"), and get an instant, structured answer powered by multimodal AI.

### Features

- **Multimodal Invoice Analysis** -- Upload JPG/PNG images of invoices, receipts, or bills
- **Natural Language Queries** -- Ask anything about the document in plain English
- **Google Gemini 1.5 Flash** -- Powered by Google's latest multimodal LLM
- **Instant Responses** -- Get structured answers in seconds
- **Zero Config UI** -- Clean Streamlit interface, no frontend code required
- **Docker Ready** -- Ship anywhere with the included Dockerfile

---

## Architecture

```
 User                Streamlit UI             Gemini API
  |                      |                        |
  |-- upload image ----->|                        |
  |-- type question ---->|                        |
  |                      |-- image + prompt ----->|
  |                      |                        |-- multimodal LLM
  |                      |<-- structured text ----|
  |<-- display answer ---|                        |
```

1. User uploads an invoice image and types a question via the Streamlit UI
2. The app encodes the image and sends it alongside the prompt to Google Gemini 1.5 Flash
3. Gemini processes the multimodal input and returns a text response
4. The answer is rendered in the Streamlit interface

---

## Quickstart

### Prerequisites

- Python 3.11+
- A [Google AI Studio](https://aistudio.google.com/apikey) API key

### Installation

```bash
# Clone the repository
git clone https://github.com/gitswagata1/AIGENDA.git
cd AIGENDA

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Set your API key

```bash
# Linux / macOS
export GOOGLE_API_KEY="your-api-key-here"

# Windows (PowerShell)
$env:GOOGLE_API_KEY="your-api-key-here"
```

### Run the app

```bash
streamlit run streamlit_app.py
```

The app opens at `http://localhost:8501`. Upload an invoice image and start asking questions.

### Docker (alternative)

```bash
docker compose up --build
```

---

## Usage Examples

| Question | What Gemini Returns |
|----------|-------------------|
| "What is the total amount?" | Extracts and returns the total from the invoice |
| "List all line items with prices" | Structured breakdown of every item and cost |
| "Who is the vendor and what's their address?" | Vendor name, address, and contact details |
| "Is there any tax applied? How much?" | Tax breakdown with percentages and amounts |
| "Summarize this invoice in 3 bullet points" | Concise summary of the key invoice details |

---

## Project Structure

```
AIGENDA/
├── streamlit_app.py          # Main application (Streamlit + Gemini)
├── requirements.txt          # Production dependencies
├── requirements-dev.txt      # Development dependencies (linting, testing)
├── Dockerfile                # Container image definition
├── docker-compose.yml        # Docker Compose config
├── Makefile                  # Dev commands (lint, test, clean)
├── .github/
│   ├── workflows/            # CI/CD (lint, CodeQL, release, stale)
│   ├── ISSUE_TEMPLATE/       # Bug report & feature request templates
│   └── PULL_REQUEST_TEMPLATE.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE                   # MIT
└── CHANGELOG.md
```

---

## Development

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Lint
make lint

# Test
make test

# Clean caches
make clean
```

---

## Roadmap

- [ ] **Multi-page invoice support** -- Handle PDFs with multiple pages
- [ ] **Expense categorization** -- Auto-classify line items (food, travel, supplies)
- [ ] **Export to CSV/Excel** -- Download structured invoice data
- [ ] **Batch processing** -- Upload multiple invoices at once
- [ ] **Google Calendar integration** -- Auto-schedule payment reminders
- [ ] **Multi-language support** -- Analyze invoices in any language
- [ ] **Invoice templates** -- Pre-built prompts for common invoice types

See the [open issues](https://github.com/gitswagata1/AIGENDA/issues) for community-requested features.

---

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Push and open a Pull Request

---

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgments

- [Google Gemini AI](https://ai.google.dev/) for multimodal intelligence
- [Streamlit](https://streamlit.io/) for the rapid UI framework
- [Pillow](https://python-pillow.org/) for image processing

---

<div align="center">

**Built by [Swagata Banerjee](https://github.com/gitswagata1)**

[![footer](https://capsule-render.vercel.app/api?type=waving&color=0:f7b733,50:e44d26,100:141e30&height=100&section=footer)](https://github.com/gitswagata1/AIGENDA)

</div>
