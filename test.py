import sqlite3

from ai_models import SimpleTextAI


def analyze_sentiment():
    """
    Analyzes the sentiment of a text using a SimpleTextAI model and stores the response in a database.

    Returns:
        None
    """
    conn = sqlite3.connect("data.db")
    c = conn.cursor()

    c.execute("SELECT text, label FROM training_data")
    data = c.fetchall()

    train_texts = [row[0] for row in data]
    train_labels = [row[1] for row in data]

    ai = SimpleTextAI()
    ai.train(train_texts, train_labels, show_summary=True, show_training_logs=True)

    user_text = input("Enter a text to analyze its sentiment (positive or negative sentence): ")
    prediction = ai.predict([user_text])
    sentiment = "positive" if prediction > 0.5 else "negative"
    print(f"The sentiment of the text is: {sentiment}\nPrediction: {prediction}")

    store_response = input(
        "Do you want to store your response in the database? (yes/no [make sure the response is correct first]): "
    )
    if store_response.lower() == "yes":
        c.execute(
            "INSERT INTO training_data (text, label) VALUES (?, ?)",
            (user_text, 1 if sentiment == "positive" else 0),
        )
        conn.commit()
        print("Response stored in the database.")

    conn.close()


analyze_sentiment()
