from transformers import pipeline

summarizer = pipeline("summarization")

def summarize(text: str):
    return summarizer(text, min_length=30, max_length=100)[0]['summary_text']
