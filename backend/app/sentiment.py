import transformers

transformers.logging.set_verbosity_error()

from transformers import pipeline
analyzer = pipeline(task="sentiment-analysis", model = "finiteautomata/bertweet-base-sentiment-analysis")

def analyze_sentiment(text):
    try:
        if not text or not text.strip():
            return {"label": "neutral", "score": 0.0}
            
        score = analyzer(text)
        
        label_mapping = {
            "POS": "positive",
            "NEG": "negative",
            "NEU": "neutral"
        }
        
        return {
            "label": label_mapping.get(score[0]["label"], "neutral"),
            "score": score[0]["score"]
        }
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return {"label": "neutral", "score": 0.0}
