# Power BI RBI Dashboard: Cheat Sheet

Once you have run the Python ETL scripts, you will have a clean `data/processed_complaints.csv` file. 

Follow these steps to build the dashboard that will blow away the RBI recruiters.

## Step 1: Import the Data
1. Open Power BI Desktop.
2. Click **Get Data** -> **Text/CSV**.
3. Select the `processed_complaints.csv` file you just generated.
4. Click **Load**.

## Step 2: Create the "RBI Recruiter" Visuals
To prove you understand what the CEP01 (Consumer Education & Protection) and DOS02 (Supervision) departments care about, build these exactly:

### Visual 1: Complaint Trends Over Time (Line Chart)
* **Visual Type:** Line Chart
* **X-Axis:** `date_received` (Make sure it's set to Year/Month hierarchy)
* **Y-Axis:** Count of `complaint_id`
* *Why:* Shows you can track "complaint trends" (specifically requested in CEP01 PDF).

### Visual 2: Top Customer Pain Points (Bar Chart)
* **Visual Type:** Clustered Bar Chart
* **Y-Axis:** `product`
* **X-Axis:** Count of `complaint_id`
* *Why:* Shows you can identify "emerging issues and customer pain points" (CEP01 PDF).

### Visual 3: Company Response Status (Donut Chart)
* **Visual Type:** Donut Chart
* **Legend:** `company_response_to_consumer`
* **Values:** Count of `complaint_id`
* *Why:* Shows you monitor regulatory compliance and SLA timelines.

## Step 3: Add Advanced DAX (The Secret Sauce)
The DOS02 role explicitly asks for "Advanced DAX". You MUST add these two measures.

Click **Modeling** -> **New Measure** and paste these in:

**1. High Priority Complaint Ratio:**
```dax
High_Priority_Ratio = 
DIVIDE(
    CALCULATE(COUNT(complaints[complaint_id]), complaints[is_high_priority] == True),
    COUNT(complaints[complaint_id]),
    0
)
```

**2. Month-over-Month Growth:**
```dax
MoM_Complaint_Growth = 
VAR CurrentMonth = COUNT(complaints[complaint_id])
VAR PreviousMonth = CALCULATE(COUNT(complaints[complaint_id]), PREVIOUSMONTH(complaints[date_received]))
RETURN
DIVIDE(CurrentMonth - PreviousMonth, PreviousMonth, 0)
```

## Step 4: Publish
Take a clean screenshot of this dashboard. We will use this screenshot to replace the "Gesture Player" on your portfolio website!
