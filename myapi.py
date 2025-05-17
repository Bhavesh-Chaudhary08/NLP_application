from transformers import pipeline
from langdetect import detect

class API:

    def sentiment_analysis(self, text):
        sentiment_pipeline = pipeline("sentiment-analysis")
        response = sentiment_pipeline(text)
        return response[0]['label']

    def ner(self, text):
        ner_pipeline = pipeline("ner",model="dslim/bert-base-NER",  grouped_entities=True)
        response = ner_pipeline(text)
        return response

    def detect_language(self, text):
        return detect(text)
