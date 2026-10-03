import pandas as pd
import numpy as np
from scipy.stats import zscore
# 1. Creating the dataset
data = {
    "Day": range(1, 11),
    "Revenue": [45, 52, np.nan, 48, 390, 55, np.nan, 50, 47, 53]
}
df = pd.DataFrame(data)
print("Original Dataset:")
print(df)
# 2. Detecting missing values
missing_values = df["Revenue"].isnull().sum()
print("\nMissing values in Revenue:", missing_values)
# 3. Filling missing values using median
median_revenue = df["Revenue"].median()
df["Revenue"] = df["Revenue"].fillna(median_revenue)
print("\nMedian Revenue:", median_revenue)
print("\nAfter Median Fill:")
print(df)
# 4. Min-Max Normalization
df["Revenue_MinMax"] = (
    (df["Revenue"] - df["Revenue"].min())
    / (df["Revenue"].max() - df["Revenue"].min())
)
# 5. Z-score Standardization
df["Revenue_Zscore"] = zscore(df["Revenue"])
# 6. IQR Outlier Detection
Q1 = df["Revenue"].quantile(0.25)
Q3 = df["Revenue"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
# Create Outlier Boolean column
df["Outlier"] = (
    (df["Revenue"] < lower_bound)
    | (df["Revenue"] > upper_bound)
)
# 7. Print IQR information
print("\nQ1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
# 8. Print detected outlier days
outlier_days = df.loc[df["Outlier"], "Day"].tolist()
print("\nIQR outliers detected on day(s):", outlier_days)
# 9. Final table
print("\nFinal Table:")
print(df)