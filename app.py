import streamlit as st
import pickle
import nltk
from nltk.corpus import stopwords

# Load saved model and TF-IDF vectorizer
model = pickle.load(open("voting_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Download stopwords (only first time)
nltk.download("stopwords")

# Title
st.title("📧 Email Category Prediction App")

# Input fields
subject = st.text_input("Enter Email Subject:")
body = st.text_area("Enter Email Body:")
submit = st.button("🔍 Predict")

if submit:
    if not subject and not body:
        st.warning("Please enter at least a subject or body to predict.")
    else:
       if submit:
    # Combine subject and body
        text = subject + " " + body
        text = text.lower().split()

    # Remove stopwords
        stp = stopwords.words('english')
        text = [word for word in text if word not in stp]
        clean_text = " ".join(text)

    # Transform and predict
        vector = tfidf.transform([clean_text])
        prediction = model.predict(vector)[0]

    # Decode numeric label
        category_map = {
            0: 'Healthcare',
            1: 'Promotional',
            2: 'Social Media',
            3: 'Spam',
            4: 'Study'
    }

        category_name = category_map.get(prediction, "Unknown")

    # Display result
        st.write("### 🧾 Predicted Category:")
        st.success(category_name)