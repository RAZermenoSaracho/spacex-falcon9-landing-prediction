# 🚀 SpaceX Falcon 9 Landing Success Prediction

End-to-end **Data Science & Machine Learning project** focused on analyzing SpaceX Falcon 9 launch data to **predict first-stage landing success**.

The project covers the complete data lifecycle — from **data collection and cleaning**, through **exploratory and geospatial analysis**, to **machine learning modeling** and an **interactive dashboard** for real-time exploration.

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
├── README.md
├── requirements.txt
├── environment.yml
│
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
│       └── confusion_matrix_random_forest.png
│
├── dashboard/
│   ├── app.py
│   ├── assets/
│   │   └── style.css
│   └── README.md
│
└── screenshots/
    ├── dashboard_all_sites.png
    ├── dashboard_site_filter.png
    └── folium_map.png
```

---

## 🔍 Project Highlights

### Data Collection & Processing
- SpaceX public API ingestion
- Web scraping from Wikipedia
- Data cleaning and feature engineering
- Consolidated, reproducible data pipeline

### Exploratory & Geospatial Analysis
- SQL-based EDA
- Visual trend analysis
- Interactive launch site maps with Folium

### Machine Learning
- Classification models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
- Performance evaluation using:
  - Accuracy
  - Precision
  - Recall
  - F1-score
- Final model selection based on overall performance

### Model Artifacts
- Trained **Random Forest pipeline** serialized with `joblib`
- Metrics exported to CSV
- Confusion matrix saved as an image for reporting

### Interactive Dashboard
- Built with **Plotly Dash**
- Dynamic filtering by launch site and rocket configuration
- KPI indicators and success rate visualizations

---

## ▶️ Running the Project Locally

### 1️⃣ Environment setup

```bash
conda create -n spacex-ds python=3.10
conda activate spacex-ds
conda install numpy<2 pandas scikit-learn plotly dash folium
```

Or using the provided environment file:

```bash
conda env create -f environment.yml
conda activate spacex-ds
```

### 2️⃣ Launch the dashboard

```bash
cd dashboard
python app.py
```

Open in your browser:

```
http://127.0.0.1:8050/
```

---

## 🌐 Live Demo

- **Portfolio:** https://razs.vercel.app/
- **Live Dashboard:** *(deployment link to be added)*

---

## 👤 Author

**Ricardo Zermeño**  
Software Engineer | Data & ERP-Oriented Developer  

🔗 Portfolio: https://razs.vercel.app/

---

## 📜 License

This project is intended for **educational and portfolio purposes**.
