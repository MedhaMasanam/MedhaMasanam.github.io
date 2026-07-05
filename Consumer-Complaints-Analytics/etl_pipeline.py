import pandas as pd
import numpy as np
import os
from datetime import datetime

def run_etl_pipeline():
    print("Starting ETL Pipeline...")
    
    # 1. EXTRACT
    raw_data_path = "data/raw_complaints.csv"
    if not os.path.exists(raw_data_path):
        print(f"Error: Could not find {raw_data_path}. Please run download_data.py first.")
        return
        
    print(f"Loading raw data from {raw_data_path}...")
    # Load dataset, handling mixed types
    df = pd.read_csv(raw_data_path, low_memory=False)
    
    # 2. TRANSFORM
    print("Cleaning and transforming data...")
    
    # Drop rows where critical information is missing
    df = df.dropna(subset=['product', 'date_received'])
    
    # Standardize Dates
    df['date_received'] = pd.to_datetime(df['date_received'])
    df['year_month'] = df['date_received'].dt.to_period('M').astype(str)
    
    # Clean text: fill NaN narratives with placeholder
    df['consumer_complaint_narrative'] = df['consumer_complaint_narrative'].fillna('No narrative provided')
    
    # Feature Engineering: Flag high-priority complaints (e.g., involving credit reporting or debt collection)
    high_priority_products = ['Credit reporting, credit repair services, or other personal consumer reports', 'Debt collection']
    df['is_high_priority'] = df['product'].isin(high_priority_products)
    
    # Calculate resolution time (if date_sent_to_company is available)
    if 'date_sent_to_company' in df.columns:
        df['date_sent_to_company'] = pd.to_datetime(df['date_sent_to_company'])
        df['days_to_send'] = (df['date_sent_to_company'] - df['date_received']).dt.days
    
    # Standardize categorical variables
    df['company_response_to_consumer'] = df['company_response_to_consumer'].fillna('Pending / No Response')
    
    # 3. LOAD (Save Processed Data)
    processed_data_path = "data/processed_complaints.csv"
    df.to_csv(processed_data_path, index=False)
    print(f"Saved processed clean dataset ({len(df)} rows) to {processed_data_path} for Dashboard consumption.")
    
    # 4. AUTOMATED REPORTING (MIS Automation)
    print("Generating automated Executive Summary Report...")
    os.makedirs("reports", exist_ok=True)
    report_path = f"reports/Executive_Summary_{datetime.now().strftime('%Y%m%d')}.xlsx"
    
    # Calculate Metrics for the Report
    product_summary = df.groupby('product').size().reset_index(name='Total Complaints').sort_values('Total Complaints', ascending=False)
    
    response_summary = df.groupby('company_response_to_consumer').size().reset_index(name='Count')
    
    monthly_trend = df.groupby('year_month').size().reset_index(name='Complaints').sort_values('year_month')
    
    # Write to an Excel file with multiple sheets
    with pd.ExcelWriter(report_path, engine='openpyxl') as writer:
        product_summary.to_excel(writer, sheet_name='By Product', index=False)
        response_summary.to_excel(writer, sheet_name='By Response', index=False)
        monthly_trend.to_excel(writer, sheet_name='Monthly Trend', index=False)
        
    print(f"Successfully generated automated report: {report_path}")
    print("ETL Pipeline completed successfully!")

if __name__ == "__main__":
    run_etl_pipeline()
