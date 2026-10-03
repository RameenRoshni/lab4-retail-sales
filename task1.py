import pandas as pd
import numpy as np
from scipy import stats # type: ignore
# 1. Create Pandas Series
scores = pd.Series([
    72, 65, 88, np.nan, 54,
    91, 76, np.nan, 83, 69
])
print("Original Exam Scores:")
print(scores)
# 2. Descriptive Statistics
print("\nDescriptive Statistics:")
print(scores.describe())
# 3. Skewness and Kurtosis
# Dropping missing values before using SciPy
clean_scores = scores.dropna()
print("\nSkewness:", stats.skew(clean_scores))
print("Kurtosis:", stats.kurtosis(clean_scores))
# 4. Detect Missing Values
missing_values = scores.isnull().sum()
print("\nMissing values:", missing_values)
# 5. Fill Missing Values with Mean
mean_score = scores.mean()
filled_scores = scores.fillna(mean_score)
print("\nMean Score:", mean_score)
print("\nFilled Scores:")
print(filled_scores)