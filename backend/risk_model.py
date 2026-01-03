import pandas as pd

# Load data
ward_data = pd.read_csv("../data/ward_data.csv")
rainfall_data = pd.read_csv("../data/sample_rainfall_data.csv")
complaints_data = pd.read_csv("../data/sample_complaints.csv")

# Merge datasets
data = ward_data.merge(rainfall_data, on="ward_name")

# Count complaints per ward
complaint_counts = complaints_data.groupby("ward_name").size().reset_index(name="complaint_count")
data = data.merge(complaint_counts, on="ward_name", how="left")
data["complaint_count"] = data["complaint_count"].fillna(0)

# Risk scoring function
def calculate_risk(row):
    score = 0

    # Rainfall impact
    if row["avg_rainfall_mm"] > 120:
        score += 2
    elif row["avg_rainfall_mm"] > 90:
        score += 1

    # Drainage condition impact
    if row["drainage_condition"] == "Poor":
        score += 2
    elif row["drainage_condition"] == "Moderate":
        score += 1

    # Complaint impact
    if row["complaint_count"] >= 3:
        score += 2
    elif row["complaint_count"] >= 1:
        score += 1

    # Final risk classification
    if score >= 5:
        return "Red"
    elif score >= 3:
        return "Yellow"
    else:
        return "Green"

# Apply risk classification
data["risk_level"] = data.apply(calculate_risk, axis=1)

# Display result
print(data[["ward_name", "risk_level"]])

