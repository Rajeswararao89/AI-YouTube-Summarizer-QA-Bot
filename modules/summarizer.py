from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    # Limit text to 1024 tokens at once (BART limit)
    if len(text.split()) > 800:
        text = " ".join(text.split()[:800])  # Simple truncate for now

    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]['summary_text']
