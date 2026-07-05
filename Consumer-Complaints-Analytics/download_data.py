import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_synthetic_cfpb_data():
    print("Generating highly realistic synthetic CFPB data for analysis...")
    
    # Configuration
    num_records = 15000
    np.random.seed(42)
    
    # Lists for synthetic generation
    products = [
        'Credit reporting, credit repair services, or other personal consumer reports',
        'Debt collection',
        'Credit card or prepaid card',
        'Mortgage',
        'Checking or savings account',
        'Student loan',
        'Vehicle loan or lease'
    ]
    
    responses = [
        'Closed with explanation',
        'Closed with monetary relief',
        'Closed with non-monetary relief',
        'In progress',
        'Untimely response'
    ]
    
    companies = ['JPMorgan Chase & Co.', 'Bank of America', 'Wells Fargo', 'Citibank', 'Equifax', 'Experian', 'TransUnion', 'Capital One']
    states = ['CA', 'TX', 'FL', 'NY', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI']
    
    # Generate dates over the last 2 years
    end_date = datetime.now()
    start_date = end_date - timedelta(days=730)
    date_range = (end_date - start_date).days
    
    random_days = np.random.randint(0, date_range, num_records)
    dates_received = [start_date + timedelta(days=int(d)) for d in random_days]
    
    # Some complaints take 1-15 days to send to company
    days_to_send = np.random.randint(0, 15, num_records)
    dates_sent = [dates_received[i] + timedelta(days=int(days_to_send[i])) for i in range(num_records)]
    
    # Build dataframe
    df = pd.DataFrame({
        'complaint_id': np.arange(3000000, 3000000 + num_records),
        'date_received': dates_received,
        'product': np.random.choice(products, num_records, p=[0.3, 0.2, 0.15, 0.1, 0.1, 0.05, 0.1]),
        'sub_product': 'General',
        'issue': 'Incorrect information on your report',
        'sub_issue': 'Information belongs to someone else',
        'consumer_complaint_narrative': np.random.choice([np.nan, "The bank charged me a fee I did not authorize.", "My credit report shows an account I never opened."], num_records, p=[0.7, 0.15, 0.15]),
        'company_public_response': np.nan,
        'company': np.random.choice(companies, num_records),
        'state': np.random.choice(states, num_records),
        'zip_code': '12345',
        'tags': np.nan,
        'consumer_consent_provided': 'Consent provided',
        'submitted_via': 'Web',
        'date_sent_to_company': dates_sent,
        'company_response_to_consumer': np.random.choice(responses, num_records, p=[0.6, 0.1, 0.1, 0.15, 0.05]),
        'timely_response': np.random.choice(['Yes', 'No'], num_records, p=[0.9, 0.1]),
        'consumer_disputed?': np.random.choice(['Yes', 'No', np.nan], num_records, p=[0.2, 0.4, 0.4])
    })
    
    # Introduce some artificial "dirty data" for the ETL script to clean
    df.loc[np.random.choice(df.index, 500), 'product'] = np.nan
    df.loc[np.random.choice(df.index, 300), 'company_response_to_consumer'] = np.nan
    
    os.makedirs("data", exist_ok=True)
    output_path = "data/raw_complaints.csv"
    df.to_csv(output_path, index=False)
    print(f"Successfully generated {len(df)} realistic records and saved to {output_path}")

if __name__ == "__main__":
    generate_synthetic_cfpb_data()
