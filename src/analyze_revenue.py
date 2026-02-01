import pandas as pd
import yaml

df = pd.read_csv("data/revenue_sample.csv")
latest = df.iloc[-1]

with open("config/thresholds.yaml") as f:
    thresholds = yaml.safe_load(f)

gap_pct = (latest.actual_revenue - latest.target_revenue) / latest.target_revenue

if gap_pct <= thresholds["critical_gap"]:
    status = "🚨 Off Track"
elif gap_pct <= thresholds["warning_gap"]:
    status = "⚠️ At Risk"
else:
    status = "✅ On Track"

message = f"""
{status}
Revenue pacing {gap_pct:.1%} vs target.
Suggested action: Review pipeline conversion and merchant activity.
"""

print(message)
