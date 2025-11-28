# 🎬 Movie Review Analysis (Streamlit Integrated)

A machine learning project for analyzing movie reviews and predicting sentiment (positive/negative).  
This project demonstrates an end‑to‑end NLP pipeline: dataset download from Kaggle, preprocessing, model training, evaluation, and interactive visualization via Streamlit.

---

## 📌 Features
- Automated Kaggle dataset download (IMDB 50k Movie Reviews)
- Text preprocessing: tokenization, stopword removal, lemmatization
- Vectorization using TF‑IDF
- Sentiment classification using Logistic Regression
- Evaluation metrics: accuracy, precision, recall, F1‑score
- Interactive Streamlit app for running the workflow and testing predictions

---

## 🛠️ Tech Stack
- **Python 3.9+**
- **Libraries**:  
  - `numpy`, `pandas` for data handling  
  - `scikit-learn` for ML models  
  - `kaggle` for dataset download  
  - `streamlit` for interactive UI

---

## 🔑 Kaggle API Setup

This project uses datasets hosted on Kaggle. To access them, you’ll need to configure the Kaggle API:

1. **Get your Kaggle API key**
   - Go to [Kaggle](https://www.kaggle.com/) and log in.
   - Click on your profile picture → *Account*.
   - Scroll down to the **API** section and click **Create New API Token**.
   - This will download a file called `kaggle.json`.

2. **Place the file in the project folder**
   - Move the downloaded `kaggle.json` file into the root of this project (`movie_review_analysis/`).

3. **Install Kaggle CLI**
   ```bash
   pip install kaggle
   ```
## 🚀 Getting Starte
   
1. **Clone the repository**
   
   ```bash
   git clone https://github.com/your-username/movie_review_analysis.git
   cd movie_review_analysis
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit app**
   ```bash
   streamlit run src/app.py
   ```  
📊 Example Output
- Accuracy: ~87%
- Precision: ~0.85
- Recall: ~0.88
- F1‑score: ~0.86
   
📈 Future Improvements
- Incorporate transformer models (BERT, DistilBERT)
- Deploy as a REST API using Django/Flask
- Add visualization dashboards
- Expand dataset for multilingual sentiment analysis
   




