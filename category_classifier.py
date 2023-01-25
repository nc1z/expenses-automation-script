import nltk
from nltk.classify import NaiveBayesClassifier
import json


class CategoryClassifier:
    def __init__(self):
        with open('dataset.json', 'r') as f:
            loaded_list = json.load(f)
        self.dataset = loaded_list

        self.classifier = self.train_classifier()

    def extract_features(self, text):
        return {word: True for word in text.split()}

    def train_classifier(self):
        training_data = [(self.extract_features(text), label)
                         for text, label in self.dataset]
        return NaiveBayesClassifier.train(training_data)

    def classify(self, expense):
        return self.classifier.classify(self.extract_features(expense))
