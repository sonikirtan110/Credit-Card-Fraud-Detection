# 💳 Credit Card Fraud Detection

🔍 **About the Project**  
This project leverages **Machine Learning** for real-time fraud detection and **Power BI** for dynamic visualizations. It aims to help financial institutions reduce losses and enhance trust by quickly identifying fraudulent transactions.

---

## 🚀 Features

- 🔗 Real-time fraud detection with ML models  
- 📊 Interactive Power BI dashboards for fraud analytics  
- 🧠 Pretrained ML model with pipeline and hyperparameter tuning  
- 🌐 Web UI hosted with **Render** for user interaction  
- 📂 Organized project structure for reproducibility

---

## 🗂️ File Structure

```
credit-card-fraud-detection/
│
├── images
│   ├── 1.png                     # UI homepage
│   ├── 2.png                     # UI about page
│   ├── index.png
│   ├── transaction_overview.png
│   ├── demographic_insights.png
│   ├── geographic_analysis.png
│   ├── merchant_category.png
│   └── temporal_analysis.png
│
├── models
│   ├── best_fraud_detection_model.pkl
│   ├── best_fraud_detection_modell.pkl
│   └── best_fraud_detection_pipeline1.1.pkl.bz2
│
├── notebooks
│   ├── Test.ipynb
│   ├── TryFinal.ipynb
│   ├── TryFinal - Copy.ipynb
│   └── TryFinalTunning.ipynb
│
├── templates
│   └── index.html
│
├── app.py
├── LICENSE
├── Projectppt.pptx
├── README.md
└── requirements.txt
```

---

## 📊 Live Dashboard

- 🔗 **NovyPro**: [Power BI NovyPro Dashboard](https://project.novypro.com/oSlNml)  
- 🔗 **Power BI Live**: [Live Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZjhkMTVmMzUtNDJkOC00OGVlLTkzMDYtYzFiYWM4OWExMzI2IiwidCI6ImRhYTU5MmNhLWRlN2ItNGM1NC04ODM2LTkxYTY2OTBmZTE5NyJ9&pageName=227861ced3fd2f726a2c)  
- 🌐 **Render UI**: [Live Web App on Render](https://credit-card-fraud-detection-gnkn.onrender.com)

---

## 🗂️ Workflow

1. 🧹 **Data Preprocessing**  
   - Cleaning and preparing the dataset (handling missing values, standardization, encoding).

2. 🔍 **Exploratory Data Analysis (EDA)**  
   - Analyzing transaction trends, locations, and categories.

3. 🤖 **Model Training**  
   - Implementing and evaluating various ML algorithms such as Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, etc.  
   - Model selection is based on key metrics like F1 Score, Precision, and Recall.

4. 🌐 **Web Application**  
   - Built using Flask (with HTML/CSS for UI).  
   - The model pipeline is deployed as a web service for real-time predictions.

5. 📊 **Visualization**  
   - Power BI dashboards for interactive analysis and reporting of fraudulent versus legitimate transactions.

---

## 📄 Dataset

- **Source**: [Kaggle - Fraud Detection Dataset](https://www.kaggle.com/datasets/kartik2112/fraud-detection/data)  
- **Details**:  
  - 1,296,675 transactions from 1,000 customers (2019–2020)  
  - Transactions are labeled as fraudulent or legitimate  
  - Features include transaction amount, location, category, timestamp, etc.

---

## 💻 How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/sonikirtan110/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the ML Model
- **Jupyter Notebook**: Open and run the provided notebooks to train/test the model.
- **Script**: You can also run the web service with:
  ```bash
  python app.py
  ```

### 4. Explore the Dashboard  
- Open the provided `.pbix` file in Power BI, or  
- View the hosted dashboards using the links above.

---

## 🖼️ Project Visualizations

### UI Preview
| Home Page | About Page |
|-----------|------------|
| ![1.png](images/1.png) | ![2.png](images/2.png) |

### Power BI Visuals
- **Home Page**:  
  ![Home Page](images/index.png)

- **Transaction Overview**:  
  ![Transaction Overview](images/transaction_overview.png)

- **Demographic Insights**:  
  ![Demographic Insights](images/demographic_insights.png)

- **Geographic Analysis**:  
  ![Geographic Analysis](images/geographic_analysis.png)

- **Merchant & Category Analysis**:  
  ![Merchant Category Analysis](images/merchant_category.png)

- **Temporal Analysis**:  
  ![Temporal Analysis](images/temporal_analysis.png)

---

## 📈 Best Model Performance (Random Forest)

| Metric      | Score    |
|-------------|----------|
| Accuracy    | 0.9959   |
| ROC-AUC     | 0.9920   |
| Precision   | 0.9990   |
| Recall      | 0.9969   |
| F1-Score    | **0.9979** |

---

## 📜 License

This project is licensed under the Apache License.

---

## 🤝 Contributions

- Contributions, suggestions, and PRs are welcome!
- Please open issues for bugs or feature requests.

---

## 📬 Contact

**Kirtan Soni**  
- Email: [sonikirtan2004@gmail.com](mailto:sonikirtan2004@gmail.com)  
- LinkedIn: [linkedin.com/in/kirtansoni02](https://www.linkedin.com/in/kirtansoni02)

---

⭐ **If you like this project, please give it a star on GitHub!**
```
