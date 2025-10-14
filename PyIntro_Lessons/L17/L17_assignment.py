"""
Lektion 17 - Statistics and Hypothesis Testing
Assignment: Statistical Analysis and Hypothesis Testing

Instructions:
1. Complete the statistical analysis tasks below
2. Use appropriate statistical tests for each scenario
3. Interpret results correctly and draw meaningful conclusions
4. Support your findings with visualizations

Dataset: You'll work with a sample dataset comparing two teaching methods
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Create sample dataset for teaching method comparison
np.random.seed(42)

# Generate data for two teaching methods
method_a_scores = np.random.normal(85, 12, 30)  # Method A: mean=85, std=12
method_b_scores = np.random.normal(78, 15, 30)  # Method B: mean=78, std=15

# Add some additional variables for correlation analysis
study_hours_a = np.random.normal(8, 2, 30)
study_hours_b = np.random.normal(6, 2.5, 30)

# Create DataFrame
data = {
    'student_id': [f'STU_{i:03d}' for i in range(1, 61)],
    'teaching_method': ['Method A'] * 30 + ['Method B'] * 30,
    'final_score': np.concatenate([method_a_scores, method_b_scores]),
    'study_hours': np.concatenate([study_hours_a, study_hours_b]),
    'previous_gpa': np.random.normal(3.2, 0.5, 60),
    'attendance_rate': np.random.uniform(0.7, 1.0, 60),
    'homework_completion': np.random.uniform(0.6, 1.0, 60)
}

df = pd.DataFrame(data)

# Add some correlation between variables
df['final_score'] = df['final_score'] + (df['study_hours'] * 2) + (df['previous_gpa'] * 5) + np.random.normal(0, 5, 60)
df['final_score'] = np.clip(df['final_score'], 0, 100)

print("Sample Dataset:")
print(df.head())
print(f"\nDataset shape: {df.shape}")
print(f"\nTeaching method distribution:")
print(df['teaching_method'].value_counts())

# Task 1: Descriptive Statistics
# TODO: Calculate and compare descriptive statistics
# - Calculate mean, median, std, min, max for final scores by teaching method
# - Create summary statistics for all numerical variables
# - Compare the distributions between the two teaching methods
# - Create visualizations to show the differences

# Task 2: Hypothesis Testing - Teaching Method Comparison
# TODO: Test if there's a significant difference between teaching methods
# - State your null and alternative hypotheses clearly
# - Choose the appropriate statistical test
# - Conduct the test and interpret the results
# - Calculate effect size
# - Create visualizations to support your findings
# - Draw conclusions about the teaching methods

# Task 3: Correlation Analysis
# TODO: Analyze relationships between variables
# - Calculate correlation matrix for all numerical variables
# - Test significance of correlations
# - Create correlation heatmap
# - Identify the strongest correlations
# - Interpret the practical significance of correlations

# Task 4: Additional Statistical Tests
# TODO: Conduct additional relevant tests
# - Test if study hours differ significantly between methods
# - Test if attendance rate affects final scores
# - Test if previous GPA is a good predictor of final scores
# - Use appropriate tests for each comparison

# Task 5: Assumption Checking
# TODO: Verify assumptions for your statistical tests
# - Check normality of distributions
# - Test for equal variances (if applicable)
# - Create Q-Q plots
# - Use appropriate tests for assumption checking
# - Document any assumption violations and their impact

# Task 6: Advanced Analysis
# TODO: Conduct more sophisticated analysis
# - Perform ANOVA if you have more than two groups
# - Create confidence intervals for your estimates
# - Perform power analysis
# - Calculate sample size needed for future studies

# Task 7: Visualization of Statistical Results
# TODO: Create comprehensive visualizations
# - Box plots comparing teaching methods
# - Histograms showing score distributions
# - Scatter plots showing relationships
# - Error bars showing confidence intervals
# - Combined plots that tell a complete story

# Task 8: Interpretation and Recommendations
# TODO: Provide actionable insights
# 1. What do your statistical tests tell you about the teaching methods?
# 2. Which factors are most important for student success?
# 3. What recommendations would you make to educators?
# 4. What are the limitations of your analysis?
# 5. What additional data would you need for a more complete analysis?

# Task 9: Statistical Report
# TODO: Write a comprehensive statistical report
# - Executive summary of findings
# - Detailed methodology
# - Results with proper interpretation
# - Limitations and assumptions
# - Recommendations for future research

# Bonus Challenge:
# TODO: Design a follow-up study
# - What would be the ideal sample size?
# - What additional variables would you measure?
# - How would you control for confounding variables?
# - What would be your experimental design?

print("\nStatistical Analysis Assignment Completed!")
print("Review your statistical tests, interpretations, and recommendations.")
