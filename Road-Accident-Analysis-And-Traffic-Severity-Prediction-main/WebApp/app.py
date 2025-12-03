from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import xgboost as xgb

app = Flask(__name__)

# Load your trained model
model = xgb.XGBClassifier()
model.load_model("../Models/xgb_model_.json")

# List of categorical columns
cat_cols = ['Street', 'City', 'County', 'State', 'Airport_Code',
            'Wind_Direction', 'Weather_Condition', 'Sunrise_Sunset']


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Gather input data from the form
        data = {
            'Year': int(request.form['Year']),
            'Start_Lat': float(request.form['Start_Lat']),
            'Start_Lng': float(request.form['Start_Lng']),
            'Distance(mi)': float(request.form['Distance(mi)']),
            'Street': request.form['Street'],
            'City': request.form['City'],
            'County': request.form['County'],
            'State': request.form['State'],
            'Airport_Code': request.form['Airport_Code'],
            'Temperature(F)': float(request.form['Temperature(F)']),
            'Wind_Chill(F)': float(request.form['Wind_Chill(F)']),
            'Visibility(mi)': float(request.form['Visibility(mi)']),
            'Wind_Direction': request.form['Wind_Direction'],
            'Weather_Condition': request.form['Weather_Condition'],
            'Traffic_Signal': int(request.form['Traffic_Signal']),
            'Sunrise_Sunset': int(request.form['Sunrise_Sunset']),
            'TimeDiff': float(request.form['TimeDiff'])
        }

        df = pd.DataFrame([data])

        # Make categorical columns
        for col in cat_cols:
            df[col] = df[col].astype('category')

        # Predict probabilities
        pred_prob = model.predict_proba(df)[0]
        pred_class = np.argmax(pred_prob) + 1

        # Prepare probabilities for display
        probabilities = {i + 1: round(p * 100, 2) for i, p in enumerate(pred_prob)}

        # Render result.html and pass prediction info
        return render_template("result.html",
                               prediction=pred_class,
                               probabilities=probabilities)

    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

