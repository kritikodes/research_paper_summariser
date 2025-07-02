# Research Paper Summarizer 🧪📄

This app uses a Hugging Face model (`google/pegasus-arxiv`) to summarize academic texts or research paper content. Built using Gradio.

Paste your abstract or full paragraph, and get a short summary instantly.

Model: https://huggingface.co/google/pegasus-arxiv

---

## Features
- 📄 **PDF Upload:** Upload a research paper PDF and extract its text for summarization.
- 📝 **Text Input:** Paste any academic text or abstract to get a concise summary.
- 🤗 **State-of-the-art Model:** Uses the Pegasus model fine-tuned for scientific papers.
- ⚡ **Fast & Simple UI:** Built with Gradio for easy interaction.

## Installation
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd Research_Summary
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the app with:
```bash
python app.py
```
This will launch a Gradio web interface in your browser.

## How to Use
- **To summarize a PDF:** Click "Upload Research Paper PDF" and select your file. The app will extract and summarize the content.
- **To summarize text:** Paste your abstract or any academic text in the textbox and click submit.

## Requirements
- Python 3.7+
- See `requirements.txt` for Python package dependencies.

## Notes
- For best results, use academic or research-oriented texts.
- The summarizer works best with content longer than 50 characters.

---

Feel free to contribute or open issues for improvements!
