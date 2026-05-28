import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("publ_years.csv", header=0)
df["SPAN"] = df["LAST_YEAR"] - df["FIRST_YEAR"] + 1

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Histogram 1 - Span (0 to 72, one bin per year)
axes[0].hist(df["SPAN"].dropna(), bins=range(0, 74), edgecolor="black", color="steelblue")
axes[0].set_title("Distribution of Publication Span")
axes[0].set_xlabel("Span (years)")
axes[0].set_ylabel("Number of Authors")

# Histogram 2 - First Year
axes[1].hist(df["FIRST_YEAR"].dropna(), bins=range(1950, 2027), edgecolor="black", color="seagreen")
axes[1].set_title("Distribution of First Publication Year")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Number of Authors")

# Histogram 3 - Last Year
axes[2].hist(df["LAST_YEAR"].dropna(), bins=range(1950, 2027), edgecolor="black", color="tomato")
axes[2].set_title("Distribution of Last Publication Year")
axes[2].set_xlabel("Year")
axes[2].set_ylabel("Number of Authors")

plt.tight_layout()
plt.savefig("histograms.png", dpi=150, bbox_inches="tight")
plt.show()


# ── BEFORE filtering ──────────────────────────────────────────
print("=== BEFORE FILTERING ===")
print("Count:  ", len(df))
print("Mean:   ", round(df["SPAN"].mean(), 2))
print("Median: ", df["SPAN"].median())
print("Min:    ", df["SPAN"].min())
print("Max:    ", df["SPAN"].max())

# ── CLASS 1 — Span = 0 (LAST_YEAR < FIRST_YEAR) ───────────────
class1 = df[df["SPAN"] <= 0]
print("\n--- Class 1: Invalid Span (SPAN <= 0) ---")
print("Count:  ", len(class1))
print("Example:\n", class1.head(1).to_string())

# ── CLASS 2 — Missing values ───────────────────────────────────
class2 = df[df["FIRST_YEAR"].isna() | df["LAST_YEAR"].isna()]
print("\n--- Class 2: Missing Values (NaN) ---")
print("Count:  ", len(class2))
print("Example:\n", class2.head(1).to_string())

# ── APPLY FILTER ───────────────────────────────────────────────
df_clean = df[
    (df["SPAN"] > 0) &
    (df["FIRST_YEAR"].notna()) &
    (df["LAST_YEAR"].notna())
]

# ── AFTER filtering ────────────────────────────────────────────
print("\n=== AFTER FILTERING ===")
print("Count:  ", len(df_clean))
print("Mean:   ", round(df_clean["SPAN"].mean(), 2))
print("Median: ", df_clean["SPAN"].median())
print("Min:    ", df_clean["SPAN"].min())
print("Max:    ", df_clean["SPAN"].max())
print("Removed:", len(df) - len(df_clean))

fig, axes = plt.subplots(1, 3, figsize=(15, 5))
# Histogram 1 - Span (1 to 72, one bin per year)
axes[0].hist(df_clean["SPAN"].dropna(), bins=range(0, 74), edgecolor="black", color="steelblue")
axes[0].set_title("Distribution of Publication Span (Filtered)")
axes[0].set_xlabel("Span (years)")
axes[0].set_ylabel("Number of Authors")

# Histogram 2 - First Year
axes[1].hist(df_clean["FIRST_YEAR"].dropna(), bins=range(1950, 2027), edgecolor="black", color="seagreen")
axes[1].set_title("Distribution of First Publication Year (Filtered)")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Number of Authors")

# Histogram 3 - Last Year
axes[2].hist(df_clean["LAST_YEAR"].dropna(), bins=range(1950, 2027), edgecolor="black", color="tomato")
axes[2].set_title("Distribution of Last Publication Year (Filtered)")
axes[2].set_xlabel("Year")
axes[2].set_ylabel("Number of Authors")

plt.tight_layout()
plt.savefig("histograms1.png", dpi=150, bbox_inches="tight")
plt.show()