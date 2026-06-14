# 🛡️ SafeApply - Fake Job Detection System

**SafeApply** is a Machine Learning-powered web application designed to identify fraudulent or fake job postings. Using Natural Language Processing (NLP) and a balanced Random Forest Classifier, the system analyzes text descriptions of job openings to protect job seekers from employment scams.

Live Link: https://fakejobdetection-vdxwxpw9odjvty43jirjdk

---

## 🚀 Features
- **Real-Time Analysis:** Paste any job description and instantly verify its legitimacy.
- **Smart NLP Processing:** Combines titles, company profiles, requirements, and benefits to analyze the complete context of a job posting.
- **Handling Data Imbalance:** Trained using `class_weight='balanced'` to ensure high accuracy for both rare fake jobs and majority real jobs.
- **Beautiful UI/UX:** Built with Streamlit, featuring a modern glassmorphic look, real-time debugging terminal logs, and a **Dark Mode** toggle.

---

## 🛠️ Tech Stack & Libraries
- **Frontend:** Streamlit, HTML5, Custom CSS
- **Machine Learning:** Scikit-Learn (Random Forest Classifier)
- **Natural Language Processing:** TF-IDF Vectorizer
- **Data Manipulation:** Pandas, NumPy
- **Model Serialization:** Pickle

---

## 📂 Project Structure
```text
├── images/
│   ├── lock.jpg          # App Logo
│   ├── real.jpg          # Static Side UI Image
│   ├── fake.jpg          # Static Side UI Image
│   ├── happy.jpg         # Result Success Image
│   └── sad.jpg           # Result Fraud Image
├── app.py                # Main Streamlit Web Application
├── main.ipynb            # Jupyter Notebook (Model Training Script)
├── model.pkl             # Trained Random Forest Model
├── vectorizer.pkl        # Fitted TF-IDF Vectorizer
└── requirements.txt      # Python Dependencies for Deployment
