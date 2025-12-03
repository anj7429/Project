# Accident Severity Prediction System

The **Accident Severity Prediction System** is a machine learning–based project designed to predict the severity level of road accidents using key factors such as weather, traffic conditions, road features, and environmental attributes. The goal is to support traffic authorities, emergency responders, and smart city planners in making faster and more informed decisions.

---

## 🚦 Features
- Predicts accident severity (low(1), medium(2), high(3), very_high(4)).
- Uses machine learning algorithms for classification.
- Accepts multiple input factors (road conditions, weather, distance, etc.).
- Provides quick and reliable predictions for safety and planning.
- Can be integrated into web applications using Flask or other frameworks.

---

## 📁 Project Structure
```
project-folder/
│-- app.py             # Flask backend (if applicable)
|-- Data/
│-- templates/         # HTML templates
│-- static/            # CSS/JS files
│-- data/              # Dataset used for training
│-- README.md          # Project documentation
```

---

## 🧠 Machine Learning Model
The system is trained on the **US Accident Dataset**, which contains real-world accident records with various features such as:
- Weather conditions
- Visibility
- Traffic signals
- Road type
- Distance

Model used: **Random Forest / XGBoost / Gradient Boosting / Adaptive Boosting / Decision Tree** (based on your project).

---

## 🛠 Technologies Used
- **Python**
- **Pandas, NumPy, Scikit-learn, XGBoost**
- **Flask (for web app)**
- **HTML, CSS ** (optional)

---

## ▶️ How to Run the Project
1. Install dependencies:
```
pip install -r requirements.txt
```
2. Run the Flask app:
```
python app.py
```
3. Open your browser at:
```
http://localhost:5000
```

---

## 📊 Use Cases
- Smart city traffic management
- Accident risk analysis
- Emergency response planning
- Road safety assessment

---

## 📈 Results
The model provides severity prediction with good accuracy and helps identify high-risk accident scenarios.

---

## 🤝 Contributing
Feel free to submit issues or pull requests to improve the system.

---

## 📜 License
This project is licensed under the **MIT License**.
