from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
import bz2
import joblib

app = Flask(__name__)

# 1. Load the trained pipeline

with bz2.open("best_fraud_detection_pipeline1.1.pkl.bz2", "rb") as f:
    pipeline = joblib.load(f)
# 2. Category options (for dropdown in index.html)
categories = [
    "entertainment", "food_dining", "gas_transport", "grocery_net", "grocery_pos",
    "health_fitness", "home", "kids_pets", "misc_net", "misc_pos",
    "personal_care", "shopping_net", "shopping_pos", "travel"
]

def get_recommendation(probability):
    """
    A simple AI-based recommendation function based on the fraud probability.
    You can expand this logic to reflect more sophisticated decision-making
    or business rules (e.g., contacting the bank, extra verification, etc.).
    """
    if probability > 0.8:
        return "High risk. Immediately verify the transaction or block the card."
    elif probability > 0.5:
        return "Medium risk. Consider additional authentication or user verification."
    else:
        return "Low risk. Transaction seems normal, but continue monitoring."

@app.route('/')
def index():
    # Render the HTML template, passing the category list for the dropdown
    return render_template("index.html", categories=categories)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # 3. Collect data from form (if submitted via HTML) or JSON (if submitted via API)
        data = request.form if request.form else request.get_json()

        # Extract features from the data
        amt = float(data['amt'])
        city_pop = float(data['city_pop'])
        lat = float(data['lat'])
        long = float(data['long'])
        merch_lat = float(data['merch_lat'])
        merch_long = float(data['merch_long'])
        unix_time = float(data['unix_time'])
        category = data['category']

        # 4. Create a DataFrame matching the model's input format
        input_data = pd.DataFrame([[amt, city_pop, lat, long, merch_lat, merch_long, unix_time, category]],
                                  columns=['amt', 'city_pop', 'lat', 'long', 'merch_lat', 'merch_long', 'unix_time', 'category'])

        # 5. Make prediction using the loaded pipeline
        prediction = pipeline.predict(input_data)[0]
        probability = pipeline.predict_proba(input_data)[0][1]

        # 6. Generate an AI-based recommendation
        recommendation = get_recommendation(probability)

        # 7. Return response (JSON)
        return jsonify({
            "prediction": "Fraudulent" if prediction >= 0.8 else "Non-Fraudulent",
            "probability": round(probability, 2),
            "recommendation": recommendation
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=True)
