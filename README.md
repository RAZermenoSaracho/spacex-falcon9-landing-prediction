# 🚀 SpaceX Falcon 9 Landing Prediction

End-to-end **Data Science and Analytics project** focused on analyzing SpaceX Falcon 9 launch data to **predict first-stage landing success**.  
The project covers the full data lifecycle: **data collection, cleaning, exploratory analysis, interactive visualization, and machine learning**, and includes a **live interactive dashboard**.

This project is part of my professional portfolio and demonstrates applied skills in **Python, SQL, data visualization, and ML**, using real-world data sources.

---

## 📌 Project Overview

SpaceX significantly reduces launch costs by reusing the first stage of its Falcon 9 rockets.  
Accurately predicting whether a booster will land successfully is critical for:

- Estimating launch costs
- Improving operational planning
- Supporting competitive bidding strategies in the aerospace industry

The goal of this project is to **analyze historical launch data** and **build predictive models** to estimate landing success.

---

## 🧱 Tech Stack

- **Python**
- **Pandas, NumPy**
- **SQL (SQLite)**
- **Plotly, Dash**
- **Folium**
- **Scikit-learn**
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
├── dashboard/
│   ├── app.py
│   ├── assets/
│   │   └── style.css
│   └── README.md
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── features.py
│   └── utils.py
│
├── models/
│   ├── trained_models/
│   └── metrics/
│
└── screenshots/
    ├── dashboard_all_sites.png
    ├── dashboard_site_filter.png
    └── folium_map.png
```

---

## 🔍 Key Features

- Data collection via SpaceX public API and web scraping
- Data cleaning and feature engineering
- SQL-based and visual exploratory data analysis
- Interactive geospatial analysis with Folium
- Interactive dashboard with Plotly Dash
- Machine learning classification models with evaluation

---

## ▶️ Running the Project Locally

```bash
conda create -n spacex-ds python=3.10
conda activate spacex-ds
conda install numpy<2 pandas scikit-learn plotly dash folium
```

```bash
cd dashboard
python app.py
```

Then open: http://127.0.0.1:8050/

---

## 🌐 Live Demo

- Portfolio: https://razs.vercel.app/
- Live dashboard: (to be added)

---

## 👤 Author

**Ricardo Zermeño**  
Software Engineer | Data & ERP-Oriented Developer  

Portfolio: https://razs.vercel.app/

---

## 📜 License

Educational and portfolio use.
