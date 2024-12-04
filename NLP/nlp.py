
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

texts = [
 "This product is amazing! I absolutely love it.",
 "I'm very disappointed with the service. It was terrible.",
 "The experience was okay, not too great but not bad either."
]

results = sentiment_analyzer(texts)

for text, result in zip(texts, results):
 print(f"Metin: {text}")
 print(f"Sonuç: {result['label']} (Skor: {result['score']:.2f})")
 print("-" * 50)