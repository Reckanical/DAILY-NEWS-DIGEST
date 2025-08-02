from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    if not text.strip():
        return "No description available."
    # Ensure the text is not too long for the model
    max_input_length = 1024
    text = text[:max_input_length]

    try:
        summary = summarizer(
            text,
            max_length=120,   
            min_length=40,    
            do_sample=False
        )
        return summary[0]['summary_text'].replace("\n", " ").strip()
    except Exception as e:
        print("Summarization error:", e)
        return text
