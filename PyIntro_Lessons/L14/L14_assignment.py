"""
Lektion 14 - Advanced Data Visualization with Seaborn
Assignment: Exploratory Data Analysis with Seaborn

Instructions:
1. Complete the tasks below using the penguins dataset
2. Use appropriate Seaborn plot types for each analysis
3. Add proper titles, labels, and styling to your plots
4. Comment your code to explain your choices

Dataset: Use sns.load_dataset('penguins') to load the penguins dataset
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set up plotting style
# TODO: Set a nice style for your plots
# Hint: Use sns.set_style() and plt.rcParams

# Load the dataset
# TODO: Load the penguins dataset using seaborn

# Task 1: Data Exploration
# TODO: Display basic information about the dataset
# - Show the first few rows
# - Display dataset shape
# - Show data types
# - Display basic statistics

# Task 2: Univariate Analysis
# TODO: Create distribution plots for each numerical feature
# - Use histplot for bill_length_mm with KDE
# - Use displot for flipper_length_mm with different styling
# - Create a subplot with all numerical features (bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g)

# Task 3: Bivariate Analysis
# TODO: Analyze relationships between features
# - Create a scatter plot of bill_length_mm vs bill_depth_mm colored by species
# - Create boxplots showing flipper_length_mm distribution by species
# - Use catplot to create a more complex categorical analysis

# Task 4: Multivariate Analysis
# TODO: Create comprehensive visualizations
# - Generate a correlation heatmap for all numerical features
# - Create a pair plot with species as hue
# - Create a violin plot comparing body_mass_g across species

# Task 5: Advanced Visualizations
# TODO: Create more sophisticated plots
# - Create a scatter plot with multiple dimensions (x, y, hue, size)
# - Create a joint plot showing the relationship between two features
# - Create a custom subplot layout with different plot types

# Task 6: Insights and Conclusions
# TODO: Based on your visualizations, answer these questions:
# 1. Which species has the largest bill length on average?
# 2. Which two features are most strongly correlated?
# 3. Which species is most easily distinguishable from the others?
# 4. What patterns do you notice in the body mass measurements?
# 5. How do the different islands compare in terms of penguin characteristics?

# Bonus Challenge:
# TODO: Create a custom visualization that combines multiple Seaborn plot types
# in a single figure to tell a compelling story about the penguins dataset

print("Assignment completed! Review your plots and insights.")
