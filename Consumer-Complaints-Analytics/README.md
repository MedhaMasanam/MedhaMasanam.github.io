# Consumer Financial Complaints: Analytics & ETL Automation

## 📊 Overview
This project demonstrates an end-to-end data analytics and automation pipeline for consumer financial complaints. It mimics the exact workflows required by modern regulatory and central banking bodies (such as the Reserve Bank of India) to monitor consumer protection, identify pain points, and automate MIS reporting.

**Key Highlights:**
- **Automated Data Pipeline (ETL):** A robust Python/Pandas script that extracts real financial complaint data, cleans missing or unstructured information, standardizes dates/categories, and engineers priority flags.
- **Report Automation:** Eliminates manual reporting by programmatically generating aggregated, multi-sheet Excel Executive Summaries.
- **Interactive Dashboarding:** Data is modeled and visualized in **Power BI** with drill-through functionality to track geographical trends, product-level anomalies, and company response times.

## 🛠️ Tech Stack
- **Languages/Libraries:** Python, Pandas, NumPy, OpenPyXL, Requests
- **Visualization:** Power BI (DAX, Interactive Dashboards)
- **Data Source:** Consumer Financial Protection Bureau (CFPB) API (50,000+ real complaint records)

## 📁 Repository Structure
- `download_data.py`: Connects to the public API to fetch the latest complaint dataset.
- `etl_pipeline.py`: The core automation engine. Cleans the data and generates the automated MIS reports.
- `data/`: Contains the raw and processed datasets (generated locally).
- `reports/`: Contains the automated Excel reports.

## 🚀 How to Run
1. Ensure Python is installed.
2. Run the downloader: `python download_data.py`
3. Run the ETL pipeline: `python etl_pipeline.py`
4. Open Power BI and connect it to `data/processed_complaints.csv` to explore the dashboard.

## 📈 Business Value & Policy Impact
By leveraging this automated pipeline, regulatory bodies can:
1. **Reduce Reporting Latency:** Move from manual monthly reporting to automated daily data ingestion.
2. **Identify Systemic Issues:** Rapidly spot spikes in specific financial products (e.g., credit reporting, debt collection).
3. **Data-Driven Policy Formulation:** Provide senior management with interactive, real-time dashboards to support evidence-based policy stances.
