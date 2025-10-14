"""
Lektion 16 - Data Quality
Assignment: Data Quality Audit and Cleaning Pipeline

Instructions:
1. Complete the data quality tasks below using the provided messy dataset
2. Document all issues found and your cleaning decisions
3. Create a comprehensive data quality report
4. Justify your cleaning strategies

Dataset: You'll work with a deliberately messy sales dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a deliberately messy dataset
np.random.seed(42)
n_records = 200

# Generate messy data with various quality issues
data = {
    'customer_id': [f'CUST_{i:04d}' for i in range(1, n_records + 1)],
    'customer_name': [f'Customer_{i}' for i in range(1, n_records + 1)],
    'email': [f'customer{i}@email.com' if i % 10 != 0 else None for i in range(1, n_records + 1)],
    'age': np.random.normal(35, 15, n_records).astype(int),
    'income': np.random.normal(50000, 20000, n_records),
    'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose'], n_records),
    'purchase_date': pd.date_range('2023-01-01', periods=n_records, freq='D'),
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports', 'Beauty', 'Toys'], n_records),
    'product_price': np.random.uniform(10, 1000, n_records),
    'quantity': np.random.randint(1, 20, n_records),
    'discount_percent': np.random.uniform(0, 50, n_records),
    'satisfaction_rating': np.random.choice([1, 2, 3, 4, 5, None], n_records, p=[0.1, 0.1, 0.2, 0.3, 0.25, 0.05])
}

df_messy = pd.DataFrame(data)

# Introduce data quality issues
# 1. Add some extreme outliers
df_messy.loc[10:15, 'income'] = [500000, 600000, 700000, 800000, 900000, 1000000]
df_messy.loc[20:25, 'age'] = [150, 200, 180, 160, 170, 190]

# 2. Add some duplicates
df_messy = pd.concat([df_messy, df_messy.iloc[0:5]], ignore_index=True)

# 3. Add inconsistent data
df_messy.loc[30:35, 'city'] = ['NYC', 'LA', 'Chi', 'HOU', 'PHX', 'PHI']  # Abbreviated cities
df_messy.loc[40:45, 'customer_name'] = ['', '   ', 'Customer_1', 'customer_2', 'CUSTOMER_3', 'Customer_4']  # Inconsistent naming

# 4. Add some impossible values
df_messy.loc[50:55, 'quantity'] = [-5, 0, 1000, -1, 50, 0]
df_messy.loc[60:65, 'discount_percent'] = [150, -20, 200, -50, 300, 0]

# 5. Add some missing values randomly
df_messy.loc[np.random.choice(df_messy.index, 20, replace=False), 'email'] = None
df_messy.loc[np.random.choice(df_messy.index, 15, replace=False), 'age'] = None

print("Messy Dataset Created!")
print(f"Dataset shape: {df_messy.shape}")
print("\nFirst few rows:")
print(df_messy.head())

# Task 1: Data Quality Assessment
# TODO: Create a comprehensive data quality audit
# - Check for missing values in each column
# - Identify duplicate records
# - Check for data type inconsistencies
# - Identify outliers using statistical methods
# - Check for impossible or invalid values
# - Validate data ranges and formats

# Task 2: Missing Value Analysis
# TODO: Analyze and handle missing values
# - Create a missing value summary
# - Visualize missing value patterns
# - Determine appropriate imputation strategies for each column
# - Implement missing value imputation
# - Document your reasoning for each imputation choice

# Task 3: Duplicate Detection and Handling
# TODO: Identify and handle duplicates
# - Find exact duplicate rows
# - Find potential duplicates (same customer_id but different other fields)
# - Decide on duplicate handling strategy
# - Implement duplicate removal or merging
# - Document your duplicate handling decisions

# Task 4: Outlier Detection and Treatment
# TODO: Identify and handle outliers
# - Use IQR method to detect outliers in numerical columns
# - Use domain knowledge to identify impossible values
# - Create visualizations to show outliers
# - Implement outlier treatment (capping, removal, or transformation)
# - Justify your outlier treatment choices

# Task 5: Data Consistency and Validation
# TODO: Ensure data consistency
# - Standardize categorical values (city names, customer names)
# - Validate data ranges (age, income, quantities, percentages)
# - Check for logical inconsistencies
# - Fix formatting issues
# - Create data validation rules

# Task 6: Data Quality Monitoring
# TODO: Create data quality monitoring functions
# - Write functions to detect common data quality issues
# - Create a data quality score calculation
# - Implement automated data quality checks
# - Create alerts for future data quality issues

# Task 7: Comprehensive Data Quality Report
# TODO: Generate a final data quality report
# - Compare before and after cleaning statistics
# - Document all issues found and actions taken
# - Calculate data quality metrics
# - Provide recommendations for data collection improvements
# - Create visualizations showing the impact of cleaning

# Task 8: Data Quality Best Practices
# TODO: Document lessons learned
# 1. What were the most common data quality issues?
# 2. Which cleaning strategies were most effective?
# 3. What would you do differently in future data collection?
# 4. How would you prevent these issues in a production system?

# Bonus Challenge:
# TODO: Create a reusable data quality pipeline that can be applied
# to similar datasets in the future

print("\nData Quality Assignment Completed!")
print("Review your cleaning decisions and their impact on data quality.")
