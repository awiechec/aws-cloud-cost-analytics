
import pandas as pd

# Load the spending dataset
data = pd.read_csv("data/cloud_spending.csv")

# Calculate total cloud spending
total_cost = data["cost_usd"].sum()

# Calculate average spending
average_cost = data["cost_usd"].mean()

# Calculate spending by AWS service
service_summary = data.groupby("service")["cost_usd"].sum()

# Calculate spending by month
monthly_summary = data.groupby("date")["cost_usd"].sum()

# Display results
print("Total Cloud Spending:", total_cost)

print("Average Cost Per Service Record:", average_cost)

print("\nSpending By AWS Service:")
print(service_summary)

print("\nMonthly Spending:")
print(monthly_summary)

# Export reports
service_summary.to_csv("reports/service_cost_summary.csv")

monthly_summary.to_csv("reports/monthly_cost_summary.csv")
