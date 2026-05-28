import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("publ_years.csv", header=0)
print(df.head())
print(df.shape)
print(df.info())

# Compute span
df["SPAN"] = df["LAST_YEAR"] - df["FIRST_YEAR"] + 1

# Descriptive statistics
print("\n--- Span Statistics ---")
print("Min:   ", df["SPAN"].min())
print("Max:   ", df["SPAN"].max())
print("Mean:  ", round(df["SPAN"].mean(), 2))
print("Median:", df["SPAN"].median())
print("Q1:    ", df["SPAN"].quantile(0.25))
print("Q3:    ", df["SPAN"].quantile(0.75))
print("\nFull describe:")
print(df["SPAN"].describe())

# Box plot
plt.figure(figsize=(10, 5))
plt.boxplot(df["SPAN"].dropna(), vert=False)
plt.title("Boxplot of Publication Spans")
plt.xlabel("Span (years)")        # ← correct axis label
plt.tight_layout()
plt.savefig("boxplot_span.png", dpi=150, bbox_inches="tight")
plt.show()