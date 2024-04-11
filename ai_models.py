import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from tensorflow.keras.preprocessing.text import Tokenizer  # type: ignore
from tensorflow.keras.preprocessing.sequence import pad_sequences  # type: ignore
from tensorflow.keras.models import Sequential  # type: ignore
from tensorflow.keras.layers import Embedding, LSTM, Dense  # type: ignore
import numpy as np


class SimpleTextAI:
    def __init__(self, vocab_size=10000, embedding_dim=16, num_classes=8):
        self.vocab_size = vocab_size
        self.embedding_dim = embedding_dim
        self.num_classes = num_classes
        self.tokenizer = Tokenizer(num_words=vocab_size, oov_token="<OOV>")
        self.model = self.build_model()

    def build_model(self):
        model = Sequential(
            [
                Embedding(self.vocab_size, self.embedding_dim),
                LSTM(128),
                Dense(self.num_classes, activation="softmax"),
            ]
        )
        model.compile(
            loss="sparse_categorical_crossentropy",
            optimizer="adam",
            metrics=["accuracy"],
        )
        return model

    def preprocess_texts(self, texts):
        self.tokenizer.fit_on_texts(texts)
        sequences = self.tokenizer.texts_to_sequences(texts)
        padded_sequences = pad_sequences(sequences)
        return padded_sequences

    def train(
        self,
        train_texts,
        train_labels,
        epochs=500,
        show_summary=False,
        show_training_logs=False,
    ):
        if not train_texts:
            raise ValueError("No texts to train on")
        if not train_labels:
            raise ValueError("No labels to train on")
        if len(train_texts) != len(train_labels):
            raise ValueError("Number of texts and labels should be the same")
        train_sequences = self.preprocess_texts(train_texts)
        train_labels = np.array(train_labels)
        verbose = 0 if not show_training_logs else 2
        history = self.model.fit(
            train_sequences, train_labels, epochs=epochs, verbose=verbose
        )
        if show_summary:
            print(f"Final epoch's accuracy: {history.history['accuracy'][-1]}")
            print(f"Final epoch's loss: {history.history['loss'][-1]}")

    def evaluate(self, test_texts, test_labels):
        if not test_texts:
            raise ValueError("No texts to evaluate")
        if not test_labels:
            raise ValueError("No labels to evaluate")
        if len(test_texts) != len(test_labels):
            raise ValueError("Number of texts and labels should be the same")
        test_sequences = self.preprocess_texts(test_texts)
        test_labels = np.array(test_labels)
        return self.model.evaluate(test_sequences, test_labels)

    def predict(self, texts):
        if not texts:
            raise ValueError("No texts to predict")
        sequences = self.preprocess_texts(texts)
        predictions = self.model.predict(sequences)
        predicted_classes = np.argmax(predictions, axis=-1)
        return predicted_classes
