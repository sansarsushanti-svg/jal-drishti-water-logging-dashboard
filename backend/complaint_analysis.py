import pandas as pd

# Load complaint data
complaints = pd.read_csv("../data/sample_complaints.csv")

# Count complaints per ward
complaint_summary = complaints.groupby("ward_name").size().reset_index(name="total_complaints")

# Urgency classification
def classify_urgency(count):
    if count >= 3:
        return "High"
    elif count >= 1:
        return "Medium"
    else:
        return "Low"

complaint_summary["urgency_level"] = complaint_summary["total_complaints"].apply(classify_urgency)

# Display result
print(complaint_summary)

