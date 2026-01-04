# 🚀 SpaceX Falcon 9 Landing Success Prediction

End-to-end **Data Science & Machine Learning project** focused on analyzing SpaceX Falcon 9 launch data to **predict first-stage landing success**.

The project covers the complete data lifecycle — from **data collection and cleaning**, through **exploratory and geospatial analysis**, to **machine learning modeling** and an **interactive dashboard** deployed live.

This repository is part of my professional portfolio and demonstrates applied skills in **Python, SQL, data visualization, and machine learning**, using real-world aerospace data.

---

## 📌 Project Motivation

SpaceX dramatically reduces launch costs by **reusing the first stage** of Falcon 9 rockets.  
Accurately predicting whether a booster will land successfully is critical for:

- Estimating launch and refurbishment costs  
- Improving operational planning  
- Supporting data-driven decision-making in competitive aerospace contexts  

The objective of this project is to **analyze historical launch data** and **build predictive models** that estimate the probability of a successful first-stage landing.

---

## 🧠 Key Questions Addressed

- Which launch sites and rocket configurations have the highest landing success rates?
- How has landing success evolved over time?
- Can landing success be reliably predicted using historical data?
- Which machine learning model performs best for this task?

---

## 🧱 Tech Stack

- **Python 3.10**
- **Pandas, NumPy**
- **SQL (SQLite)**
- **Scikit-learn**
- **Plotly & Dash**
- **Folium (geospatial analysis)**
- **Jupyter Notebook**

---

## 📂 Project Structure

```text
spacex-falcon9-landing-prediction/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   ├── 01_data_collection_api.ipynb
│   ├── 02_web_scraping.ipynb
│   ├── 03_data_wrangling.ipynb
│   ├── 04_eda_visualization.ipynb
│   ├── 05_eda_sql.ipynb
│   └── 06_ml_prediction.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── features.py
│   └── utils.py
│
├── models/
│   ├── trained_models/
│   │   └── random_forest_pipeline.pkl
│   └── metrics/
│       ├── model_comparison.csv
│       ├── model_comparison.png
│       └── confusion_matrix_random_forest.png
│
├── dashboard/
│   ├── app.py
│   ├── assets/style.css
│   └── README.md
│
├── screenshots/
│   ├── dashboard_all_sites.png
│   ├── dashboard_site_filter.png
│   └── folium_map.png
│
├── requirements.txt
├── environment.yml
├── runtime.txt
└── README.md
```

---

## 🔍 Project Highlights

### 📊 Exploratory & Geospatial Analysis
- Visual trend analysis of landing success
- Interactive launch site map built with **Folium**
- Map exported as `screenshots/folium_map.png`

### 🤖 Machine Learning
- Models trained and evaluated:
  - Logistic Regression
  - Decision Tree
  - Random Forest
- Evaluation metrics:
  - Accuracy
  - Precision
  - Recall
  - F1-score
- Metrics exported to `model_comparison.csv` and `model_comparison.png`
- Confusion matrix saved as `confusion_matrix_random_forest.png`

### 🧠 Model Artifact
- Final **Random Forest pipeline** serialized with `joblib`
- Stored at:
  ```
  models/trained_models/random_forest_pipeline.pkl
  ```
- Includes preprocessing + model steps for full reproducibility
- Used as a production-ready artifact (even if not loaded in the dashboard)

### 📈 Interactive Dashboard
- Built with **Plotly Dash**
- Filters by launch site and rocket
- KPIs and success-rate visualizations
- Deployed on Render

---

## 🌐 Live Demo

- **Live Dashboard:** https://spacex-falcon9-landing-prediction-zve7.onrender.com/
- **Portfolio:** https://razs.vercel.app/

---

## ▶️ Running Locally

```bash
conda env create -f environment.yml
conda activate spacex-ds
cd dashboard
python app.py
```

---

## 👤 Author

**Ricardo Zermeño**  
Software Engineer | Data & ERP-Oriented Developer  

🔗 Portfolio: https://razs.vercel.app/

---

## 📜 License

Educational and portfolio use.
