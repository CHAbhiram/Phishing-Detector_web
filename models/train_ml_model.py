import os
print("Current Working Directory:", os.getcwd())
print("Attempting to save to:", os.path.abspath('../detector'))
# models/train_ml_model.py
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Create a sample dataset (in real use: load from CSV)
data = [
    # (email_text, label)
    ("URGENT: Verify your account now! Click here to avoid suspension.", "phishing"),
    ("Your PayPal login was detected from a new device.", "phishing"),
    ("Confirm your identity to prevent account lock.", "phishing"),
    ("Click this link to claim your prize money.", "phishing"),
    ("Dear user, update your password immediately.", "phishing"),

    ("Meeting scheduled for tomorrow at 10 AM.", "safe"),
    ("Here is your monthly Netflix billing statement.", "safe"),
    ("Your package has been shipped.", "safe"),
    ("Project update: Q2 goals and deadlines.", "safe"),
    ("Weekly team sync notes and action items.", "safe"),

    # Add more examples to improve accuracy
    ("Login alert: New session from California.", "phishing"),
    ("Amazon order #12345 has shipped.", "safe"),
    ("Your Apple ID was used to sign in.", "phishing"),
    ("Password reset confirmation.", "safe"),
    ("You've won $1,000,000! Click now!", "phishing"),
    ("Internal HR policy update - please read.", "safe"),
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=['text', 'label'])

print("Dataset loaded:")
print(df['label'].value_counts())

# Step 2: Split data
X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 3: Create Pipeline (Vectorizer + Model)
model = Pipeline([
    ('tfidf', TfidfVectorizer(
        lowercase=True,
        stop_words='english',
        ngram_range=(1, 2),      # Use bigrams
        max_features=5000,       # Limit vocabulary
        token_pattern=r'\b[a-zA-Z]{2,}\b'  # Remove short tokens
    )),
    ('classifier', MultinomialNB(alpha=0.5))
])

# Step 4: Train
model.fit(X_train, y_train)

# Step 5: Evaluate
y_pred = model.predict(X_test)
print("\n✅ Model Evaluation:")
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 6: Save model and vectorizer
joblib.dump(model, '../detector/ml_model.pkl')
print("\n✅ Model saved to detector/ml_model.pkl")

# Optional: Save vectorizer separately (if not using Pipeline)
# The vectorizer is inside the pipeline, but you can extract it:
vectorizer = model.named_steps['tfidf']
joblib.dump(vectorizer, '../detector/vectorizer.pkl')
print("✅ Vectorizer saved to detector/vectorizer.pkl")