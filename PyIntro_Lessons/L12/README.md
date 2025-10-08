# US Census Data Dashboard

A comprehensive Streamlit dashboard for analyzing US Census data from 2010-2019.

## Features

- **Interactive Data Visualization**: Multiple chart types including line charts, bar charts, scatter plots, and histograms
- **Dynamic Filtering**: Filter data by year range, states, and regions
- **Population Trends**: Track population changes over time
- **Regional Analysis**: Compare population patterns across different US regions
- **Growth Analysis**: Analyze population growth rates and patterns
- **Responsive Design**: Clean, modern interface with sidebar controls

## Getting Started

### Prerequisites

- Python 3.7+
- Required packages (see requirements.txt)

### Installation

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Ensure the census data file (`nst-est2019-alldata.csv`) is in the same directory as the dashboard script.

### Running the Dashboard

```bash
streamlit run L12_census_dashboard.py
```

The dashboard will open in your default web browser at `http://localhost:8501`.

## Dashboard Sections

### 📊 Population Trends
- Line charts showing population changes over time
- Bar charts displaying population growth by state

### 🗺️ Geographic Analysis
- Population distribution by state
- Interactive state comparison tables

### 📈 Growth Analysis
- Growth rate distributions
- Scatter plots showing population size vs growth rate

### 🌎 Regional Analysis
- Regional population trends
- Regional summary statistics

## Data Source

US Census Bureau - Annual Estimates of the Resident Population for the United States, Regions, States, and Puerto Rico: April 1, 2010 to July 1, 2019

## Educational Notes

This dashboard demonstrates various Streamlit features:
- Data loading and caching with `@st.cache_data`
- Interactive widgets (sliders, selectboxes, multiselect)
- Layout organization (columns, sidebar, tabs)
- Multiple visualization types with Plotly
- Data filtering and aggregation
- Responsive design with custom CSS

Perfect for learning Streamlit fundamentals and data visualization techniques!