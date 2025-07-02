# Research Paper Summarizer 📄

A modern, user-friendly app to summarize research papers and academic texts with beautiful, topic-aware output. Built with Gradio and Hugging Face Transformers.

---

## ✨ Features
- **PDF Upload:** Upload a research paper PDF and extract its text for summarization.
- **Text Input:** Paste any academic text or abstract to get a concise summary.
- **Decorated Output:** Summaries are presented in a visually appealing Markdown format, with each section automatically titled using key topics from the content.
- **Automatic Topic Extraction:** Each summary section is given a general, data-driven heading based on the main topics detected in the text.
- **Fast & Simple UI:** Built with Gradio for easy, interactive use.
- **GPU Acceleration:** Automatically uses GPU for summarization if available, for faster results.
- **State-of-the-art Model:** Uses the DistilBART model fine-tuned for summarization.

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone <repo-url>
cd Research_Summary
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python app.py
```
This will launch a Gradio web interface in your browser. You can also share a public link if you wish.

---

## 🖥️ How to Use
- **Summarize a PDF:** Click "Upload PDF" and select your research paper. The app will extract and summarize the content.
- **Summarize text:** Paste your abstract or any academic text in the textbox and click submit.
- **Read the Output:** The summary will be shown in a decorated Markdown format, with each section titled by its main topics (e.g., "Transformer / Architecture / Attention").

---

## 🛠️ Requirements
- Python 3.7+
- See `requirements.txt` for all Python package dependencies.

---

## 📋 Example Output

```
# 📄 Research Paper Summary

### Transformer / Architecture / Attention
> We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely ...

### Results / BLEU / Training
> Our model achieves 28.4 BLEU on the WMT 2014 English-to-German translation task, improving over the existing best results ...
```

---

## 🤝 Contributing
Feel free to open issues or submit pull requests for improvements!

---

## 📚 Model Info
- [DistilBART for Summarization (Hugging Face)](https://huggingface.co/sshleifer/distilbart-cnn-12-6)

---

## 📃 License
MIT License
