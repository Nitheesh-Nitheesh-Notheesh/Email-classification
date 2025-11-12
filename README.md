# 📧 Email Category Prediction using Machine Learning & Streamlit

## 🧩 Project Overview
This project is a **Machine Learning-based Email Classification System** that predicts the **category of an email** (e.g., *Spam, Promotional, Social Media, Study, Healthcare*).  
It takes the **subject** and **body** of an email as input and uses trained models to classify it into the correct category.  
A **Streamlit web interface** is used to make predictions easily accessible to users.

---

## 🎯 Objective
The main goal of this project is to **automatically categorize emails** using **text processing and machine learning**, reducing manual effort in sorting emails.

---

## ⚙️ Technologies Used
- **Python** 🐍  
- **Streamlit** (for UI)
- **scikit-learn** (ML algorithms)
- **NLTK** (text preprocessing)
- **TF-IDF Vectorization** (feature extraction)
- **Pickle** (model saving/loading)

---

## 🧠 Machine Learning Model
- **Algorithms Used:**
  - K-Nearest Neighbors (KNN)
  - Support Vector Classifier (SVC)
  - Decision Tree
- **Final Model:** Voting Classifier (Ensemble)
- **Evaluation Metric:** Accuracy Score and Classification Report

The model was trained using cleaned email datasets and achieved accurate predictions for multiple categories.

---

## 🔍 Text Preprocessing Steps
1. Converted text to lowercase  
2. Removed stopwords using **NLTK corpus**  
3. Tokenized words using **TweetTokenizer**  
4. Applied **Stemming** with SnowballStemmer  
5. Transformed text data using **TF-IDF Vectorizer**

---

## 💻 Streamlit Application
### Features:
- Simple and clean UI  
- Two input fields:
  - **Subject**
  - **Body**
- **Predict** button to display the email category  
- Real-time prediction using the saved model  

---

## 🚀 How to Run the Project

### Step 1: Activate Virtual Environment
```bash
.env\Scriptsctivate
```

### Step 2: Install Dependencies
```bash
pip install -r requrment.txt
```

### Step 3: Run Streamlit App
```bash
streamlit run app.py
```

Then open the given URL in your browser (usually `http://localhost:8501`).

---

## 🗂️ Project Files
| File Name | Description |
|------------|--------------|
| **app.py** | Streamlit application code |
| **voting_model.pkl** | Saved machine learning model |
| **tfidf_vectorizer.pkl** | Saved TF-IDF vectorizer |
| **requirements.txt** | Python dependencies |
| **README.md** | Project overview and guide |

---

## 📊 Output Example
**Input:**
```
Subject: Your free course is now available
Body: Learn Python easily with this limited-time offer
```
**Predicted Category:** Promotional

---

## 📈 Future Enhancements
- Add deep learning (LSTM/BERT) models  
- Include more categories  
- Add email sender & timestamp analysis  
- Deploy app online using Streamlit Cloud or Heroku  

---

## 🧑‍💻 Developer
**Name:** [Your Name Here]  
**Project:** Email Category Prediction  
**Tools:** Python, Streamlit, scikit-learn, NLTK  
