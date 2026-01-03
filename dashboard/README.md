# 📊 SpaceX Falcon 9 Dashboard

This folder contains the **interactive Dash dashboard** for visualizing Falcon 9 landing success.

The dashboard is fully responsive and designed to be **production-ready**, with clean UI and stable Plotly rendering.

---

## 🚀 Features

- Interactive dropdown filters:
  - Launch Site
  - Rocket Version
- Key performance indicators (KPIs):
  - Landing success rate
  - Total launches
  - Launch years
- Visualizations:
  - Success vs failure bar chart
  - Landing success rate over time

---

## 🧱 Architecture

```
dashboard/
├── app.py          # Dash application
├── assets/
│   └── style.css   # Custom dark theme & responsive styles
└── README.md
```

The dashboard uses:
- **Dash 3.x**
- **Plotly**
- Modular data loading from `src/data_loader.py`

---

## ▶️ Running Locally

From the project root:

```bash
conda activate spacex-ds
python dashboard/app.py
```

Then open:
```
http://127.0.0.1:8050
```

---

## 🎨 UI & UX Notes

- Custom dark theme
- Mobile-first responsive layout
- Fixed Plotly resizing issues
- No horizontal scroll on mobile
- Stable rendering without hacks

---

## 🌍 Deployment

The dashboard is ready to be deployed on platforms such as:
- Render
- Railway
- Fly.io

Just point the service to `dashboard/app.py`.

---

## 👤 Author

**Ricardo Zermeño**  
Portfolio: https://razs.vercel.app/
