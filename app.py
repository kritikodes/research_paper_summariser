from transformers import pipeline, AutoTokenizer
import gradio as gr
import fitz  # PyMuPDF
import re
import torch
import collections
import string

# Load summarization pipeline and tokenizer, use GPU if available
model_name = "sshleifer/distilbart-cnn-12-6"
device = 0 if torch.cuda.is_available() else -1
summarizer = pipeline("summarization", model=model_name, device=device)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def clean_text(text):
    text = re.sub(r"<n>", " ", text)
    text = re.sub(r"\( s \)", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def chunk_text(text, max_token_length=900):
    tokens = tokenizer.tokenize(text)
    chunks = []
    current_chunk = []
    for token in tokens:
        current_chunk.append(token)
        if len(current_chunk) >= max_token_length:
            chunk_text = tokenizer.convert_tokens_to_string(current_chunk)
            chunks.append(chunk_text)
            current_chunk = []
    if current_chunk:
        chunk_text = tokenizer.convert_tokens_to_string(current_chunk)
        chunks.append(chunk_text)
    return chunks

def infer_section_title(summary):
    # Extract capitalized words and nouns as general topics
    words = summary.split()
    # Remove punctuation and filter for capitalized words (not at sentence start)
    keywords = [w.strip(string.punctuation) for w in words if w[0].isupper() and not w[0].isdigit() and len(w) > 2]
    # Remove duplicates, keep order
    seen = set()
    unique_keywords = [x for x in keywords if not (x in seen or seen.add(x))]
    # Join top 2-3 keywords as the section title
    if unique_keywords:
        return " / ".join(unique_keywords[:3])
    else:
        return "Summary Section"

def summarize_text(text):
    text = clean_text(text)
    if len(text.strip()) < 50:
        return "**⚠️ Please enter more content (at least 50 characters) or upload a valid PDF.**"
    try:
        chunks = chunk_text(text, max_token_length=900)
        summaries = [
            summarizer(chunk, max_length=120, min_length=40, do_sample=False)[0]['summary_text']
            for chunk in chunks
        ]
        decorated = [
            f"### {infer_section_title(s)}\n> {s.strip()}" for s in summaries
        ]
        return f"# 📄 Research Paper Summary\n\n" + "\n\n".join(decorated)
    except Exception as e:
        return f"**⚠️ Error during summarization:**\\n```\n{str(e)}\\n```"

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(pdf_file.name)
    return "".join([page.get_text() for page in doc])

def process(input_pdf, input_text):
    if input_pdf:
        text = extract_text_from_pdf(input_pdf)
    else:
        text = input_text
    return summarize_text(text)

demo = gr.Interface(
    fn=process,
    inputs=[
        gr.File(file_types=[".pdf"], label="Upload PDF"),
        gr.Textbox(lines=10, placeholder="Or paste your research paper text here"),
    ],
    outputs=gr.Markdown(label="Decorated Summary"),
    title="📄 Research Paper Summarizer",
    description="Paste text or upload a research paper PDF. Get a clean, beautifully formatted summary using a transformer model. Runs on GPU if available.",
)

demo.launch(share=True)
