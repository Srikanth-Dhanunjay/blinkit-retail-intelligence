# Retail Profit Intelligence Simulator
### Python · Streamlit · Plotly | Margin Modeling & Category Performance

A high-performance, executive-grade retail analytics dashboard and interactive profit forecasting simulator designed for quick-commerce operational tracking. This application transforms raw, transactional grocery data into scannable, high-impact business insights.

🌐 **[View Live Interactive Dashboard](https://blinkit-retail-intelligence-sjsd.streamlit.app/)**

---

## 🎯 Executive Overview & Business Value
Instead of relying on rigid, off-the-box corporate BI platforms, this application features custom engine optimization to give retail managers an immediate pulse on financial health. It delivers real-time aggregates on total revenue distributions, wholesale procurement costs, and target profit margins across dynamic store sizes and geographic tiers.

### ⚡ Key Features & Engineering Highlights
* **Split-Themed Workspace UI:** Tailored with premium CSS injections to generate high-contrast white card layouts for primary metric visualizations, coupled with a sleek, low-glare dark sidebar panel for user layout controls.
* **Granular Data Cross-Filtering:** Interactive multi-select fields allow instant performance evaluation based on Location Tiers (Tier 1, Tier 2, Tier 3) and Outlet Operational Configurations.
* **Production-Grade Performance:** Optimized with strict dataframe token caching (`@st.cache_data`) to prevent redundant data processing cycles and ensure ultra-low latency interactions.
* **Dynamic Graphical Visualizations:** Advanced analytical horizontal bar charts and multi-discrete donut charts engineered via Plotly Express to evaluate revenue contributions by department size and store footprints.

---

## 📂 Project Repository Structure
```text
├── .streamlit/
│   └── config.toml          # Custom platform configurations
├── data/
│   ├── blinkit_processed.csv # Production dataset optimized for app runtime
│   └── BlinkIT-Grocery-Data.csv # Base source raw materials
├── notebooks/               # Jupyter analytics development blueprints
├── src/
│   └── app.py               # Main pipeline architecture & core logic script
├── .gitignore               # Strictly excludes caches, env folders, and notebook checkpoints
└── requirements.txt         # Production-level application dependencies
```

---

## 🛠️ Technology Stack & Dependencies
* **Core Logic & Framework:** Python, Streamlit
* **Data Pipelines:** Pandas
* **Data Visualization Graphics:** Plotly Express
* **Interface Styling:** Advanced HTML5 / Inline CSS Custom Overrides

---

## 🏁 How to Run the App Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Srikanth-Dhanunjay/blinkit-retail-intelligence.git](https://github.com/Srikanth-Dhanunjay/blinkit-retail-intelligence.git)
   cd blinkit-retail-intelligence
   ```

2. **Set up a clean virtual environment and activate it:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install production dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute the execution engine:**
   ```bash
   streamlit run src/app.py
   ```
```
