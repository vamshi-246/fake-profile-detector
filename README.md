# 🕵️‍♂️ Fake Profile Detector

A machine learning-based system designed to detect fake social media profiles by analyzing user attributes such as name, number of followers, account activity, and profile patterns. The goal is to provide an intelligent, data-driven way to classify suspicious accounts.

---

## 🚀 Features

- ✅ Classifies profiles as **Real** or **Fake**
- 📊 Uses a trained **ML classification model** (Random Forest)
- 🧹 Preprocessing pipeline for cleaning and encoding profile data
- 📁 Dataset includes features like followers, following, post count, profile completeness, etc.
- 🔍 Evaluation metrics include **accuracy**, **precision**, **recall**, and **confusion matrix**

---

## 🧠 Tech Stack

- Python 3.x  
- Pandas  
- NumPy  
- Scikit-learn  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  

---

## 📂 Project Structure

```
fake-profile-detector/
├── model/model.ipynb      # Main notebook for training and evaluation
├── model/dataset                       # Dataset containing profile features
├── requirements.txt                  # List of dependencies
└── README.md                         # Project overview
```

---

## 📝 Usage

1. 📦 Clone this repo:
   ```bash
   git clone https://github.com/vamshi-246/fake-profile-detector
   ```

2. 📥 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. ▶️ Run the notebook:
   Open `model.ipynb` in Jupyter Notebook or any IDE and run all cells step-by-step.

4. ▶️ Run the web application:
   ```bash
   python app.py
   ```

---

## 📈 Sample Output

- Model: **Random Forest Classifier**
- Accuracy: **94.2%**
- Confusion Matrix:
  - True Positives ✅  
  - False Positives ⚠️  
  - True Negatives ✅  
  - False Negatives ⚠️  

---

## ✅ Future Improvements

- 🔗 Integration with social media APIs (e.g., Instagram, Twitter)
- 🧠 Add deep learning-based feature extraction (image, bio, etc.)
- 🌐 Deploy as a real-time web app using Streamlit or Flask

---

## 👨‍💻 Author

Made with ❤️ by [Sai Vamshi Gundoju](https://github.com/vamshi-246)
