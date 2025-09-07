import torch
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification


tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

my_model = AutoModelForSequenceClassification.from_pretrained("im-tsr/distilbert-finetuned-youtube_sentiment_analysis")

def analyze_sentiment(text):
    try:
        # Tokenize the input text
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
        
        # Run the model inference
        with torch.no_grad():
            outputs = my_model(**inputs)
        
        # Get logits and convert to probabilities using softmax
        logits = outputs.logits
        probabilities = torch.nn.functional.softmax(logits, dim=-1)
        
        # Get the predicted class and its probability
        predicted_class_id = logits.argmax().item()
        confidence_score = probabilities[0][predicted_class_id].item()
        
        # Get the label name from the model's config
        sentiment_label = my_model.config.id2label[predicted_class_id]
        
        # Map to lowercase for consistency
        label_mapping = {
            "POSITIVE": "positive",
            "NEGATIVE": "negative",
            "NEUTRAL": "neutral"
        }
        
        return {
            "label": label_mapping.get(sentiment_label),
            "score": confidence_score
        }
    
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")