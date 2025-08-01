from transformers import pipeline

summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    if not text.strip():
        return "No description available."

    try:
        input_length = len(text.split())
        max_len = min(50, max(15, input_length))  # Adjust dynamically
        min_len = max(5, int(max_len / 3))

        summary = summarizer(
            text,
            max_length=max_len,
            min_length=min_len,
            do_sample=False
        )
        return summary[0]['summary_text']
    except Exception as e:
        print("Summarization error:", e)
        return text
