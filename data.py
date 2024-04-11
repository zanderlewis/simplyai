import sqlite3
import os

positive = [
    ("Amazing product!", 1),
    ("Very good.", 1),
    ("The. Best. EVER!", 1),
    ("Never in my life had something better than this!", 1),
    ("Programming is super fun", 1),
    ("That was mind-blowing", 1),
    ("That concert was awesome!", 1),
    ("Nothing beats this.", 1),
    ("We should do this more often.", 1),
    ("This is not bad.", 1),
    ("Good", 1),
    ("I am so happy with this.", 1),
    ("This is excellent!", 1),
    ("I am loving it.", 1),
    ("This is just perfect!", 1),
    ("This is a dream come true.", 1),
    ("I am so satisfied.", 1),
    ("This is exactly what I wanted.", 1),
    ("I am so grateful for this.", 1),
    ("This is better than I expected.", 1),
    ("The Badlands is an amazing place", 1),
    ("You are a nice person, Mr. Goodman.", 1),
    ("You are super nice.", 1),
    ("You are extremely positive", 1),
    ("Mrs. Negative is a positive figure, despite her name.", 1),
]

negative = [
    ("Terrible product!", 0),
    ("Very annoying.", 0),
    ("meh.", 0),
    ("Never in my life had something been so boring.", 0),
    ("Programming is super hard and not worth it.", 0),
    ("You suck.", 0),
    ("Idiot", 0),
    ("Nothing beats this. Actually, maybe dirt in your eyes is better, loser.", 0),
    ("When are we leaving? This sucks.", 0),
    ("This is bad.", 0),
    ("Loser", 0),
    ("I am so disappointed with this.", 0),
    ("This is awful!", 0),
    ("I am hating it.", 0),
    ("This is just terrible!", 0),
    ("This is a nightmare.", 0),
    ("I am so unsatisfied.", 0),
    ("This is not what I wanted.", 0),
    ("I am so ungrateful for this.", 0),
    ("This is worse than I expected.", 0),
    ("You are very annoying, Mr. Goodman.", 0),
    ("The Badlands is a terrible place.", 0),
    ("You are a very negative person", 0),
    ("I think you are an idiot.", 0),
    ("Mr. Positive is a negative figure.", 0),
]

items = positive + negative

open("data.db", "w").close()
os.remove("data.db")

conn = sqlite3.connect("data.db")
c = conn.cursor()

c.execute(
    """
    CREATE TABLE IF NOT EXISTS training_data (
        id INTEGER PRIMARY KEY,
        text TEXT NOT NULL,
        label INTEGER NOT NULL
    )
"""
)

c.executemany("INSERT INTO training_data (text, label) VALUES (?, ?)", items)
conn.commit()
conn.close()