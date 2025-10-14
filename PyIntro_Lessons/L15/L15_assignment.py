"""
Lektion 15 - Feature Engineering
Assignment: Transform Raw Data into Predictive Features

Instructions:
1. Complete the feature engineering tasks below
2. Use the provided sample data or create your own dataset
3. Document your reasoning for each transformation
4. Test your engineered features with basic analysis

Dataset: You'll work with a sample e-commerce dataset
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.preprocessing import LabelEncoder

# Sample e-commerce dataset
np.random.seed(42)
n_records = 100

data = {
    'order_id': [f'ORD_{i:04d}' for i in range(1, n_records + 1)],
    'customer_id': np.random.randint(1000, 9999, n_records),
    'order_date': pd.date_range('2023-01-01', periods=n_records, freq='H'),
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], n_records),
    'product_name': [f'Product_{i}' for i in range(1, n_records + 1)],
    'price': np.random.uniform(10, 500, n_records).round(2),
    'quantity': np.random.randint(1, 10, n_records),
    'customer_review': np.random.choice(['Excellent', 'Good', 'Average', 'Poor', None], n_records, p=[0.3, 0.4, 0.2, 0.05, 0.05]),
    'discount_code': np.random.choice(['SAVE10', 'SAVE20', 'WELCOME', None], n_records, p=[0.2, 0.1, 0.1, 0.6]),
    'shipping_address': [f'{np.random.randint(1, 999)} Main St, City {i}' for i in range(1, n_records + 1)]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df.head())
print(f"\nDataset shape: {df.shape}")
print(f"\nData types:\n{df.dtypes}")

# Task 1: Time Feature Engineering
# TODO: Extract meaningful time-based features from order_date
# - Day of week (0=Monday, 6=Sunday)
# - Hour of day
# - Month
# - Quarter
# - Is weekend (boolean)
# - Is business hours (9 AM - 5 PM, boolean)
# - Days since first order (for each customer)

# Task 2: Text Feature Engineering
# TODO: Create features from text columns
# - Product name length
# - Number of words in product name
# - Extract city from shipping address
# - Create a feature indicating if product name contains numbers
# - Create a feature for address length

# Task 3: Categorical Encoding
# TODO: Handle categorical variables appropriately
# - One-hot encode product_category
# - Label encode customer_review (if not null)
# - Create binary features for discount_code (has_discount, specific codes)
# - Handle missing values in categorical columns

# Task 4: Derived Features
# TODO: Create new features from existing ones
# - Total order value (price * quantity)
# - Price per unit
# - Is high-value order (above median total value)
# - Customer order frequency (orders per customer)
# - Average order value per customer
# - Product category price range (min, max, mean per category)

# Task 5: Advanced Feature Engineering
# TODO: Create more sophisticated features
# - Customer lifetime value (sum of all orders per customer)
# - Time since last order (for each customer)
# - Order sequence number (1st, 2nd, 3rd order for each customer)
# - Price category (low, medium, high based on percentiles)
# - Seasonal indicators (holiday season, back-to-school, etc.)

# Task 6: Feature Validation
# TODO: Validate your engineered features
# - Check for any new missing values created
# - Verify feature distributions make sense
# - Create correlation matrix of numerical features
# - Identify any potential data leakage

# Task 7: Feature Selection and Documentation
# TODO: Document your feature engineering process
# 1. List all features you created and explain their purpose
# 2. Identify which features might be most predictive for different business questions
# 3. Suggest which features could be used for:
#    - Customer segmentation
#    - Sales forecasting
#    - Product recommendation
#    - Fraud detection

# Bonus Challenge:
# TODO: Create a feature that combines multiple variables to predict
# customer satisfaction (you can create a synthetic target variable)

print("\nFeature Engineering Assignment Completed!")
print("Review your engineered features and their potential business value.")
