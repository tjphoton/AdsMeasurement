[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://adsmeasurement.streamlit.app/)


# Ads Measurement Self-service Data Science Tools
#### © 2022 Xinjie Qiu ℠

The Ads Measurement App is a self-service Data Science tool designed to aid digital marketers and strategists in 
aligning their business goals with their Key Performance Indicators (KPIs), assessing real-time campaign performance, 
and generating actionable insights. This tool is developed using Python's Streamlit library.

This is still in the prototype demo stage with a lot of moving parts not completed yet. 

## Features

- **Business Goal and KPI**: Establish SMART (specific, measurable, achievable, relevant and time-bound) business goals and select corresponding KPIs.
- **Data Acquisition**: Real-time data quality monitoring on ingestion, transformation.
- **Ads Measurements**: Choose from experimental, observational, or quasi-experiment measurement methodologies to evaluate ad performance.
- **In-Flight Signals**: Provides real-time campaign performance assessment and visibility into the incremental impact of advertising efforts.
- **Insights Toolkit**: Generates insights from causal inference analysis and provides concrete, actionable recommendations.

## Installation

Before installing this application, please ensure you have Python 3.6 or later installed. 
You'll also need the following Python libraries: Streamlit, pandas, altair, and datetime.

Clone this repository:

```bash
git clone https://github.com/tjphoton/AdsMeasurement.git
```

Navigate into the cloned repository:

```bash
cd AdsMeasurement
```

Create a virtual environment and install the required packages:

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
To run the app, simply execute the following command:

```bash
streamlit run Ads_Measurement_Tools_Demo.py
```
