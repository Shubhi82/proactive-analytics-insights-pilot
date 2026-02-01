# Proactive Analytics Insights – Pilot

## Problem
Executives rely on static dashboards and manual reports to understand revenue performance.
Important signals are often discovered late.

## Objective
Demonstrate a lightweight analytics operating model where
insights are automatically generated and pushed to leaders
when business performance deviates from plan.

## What This Project Does
- Monitors revenue pacing vs target
- Detects meaningful deviations using simple rules
- Generates executive-ready narrative insights
- Delivers alerts directly to Slack (no dashboards required)

## Why This Matters
This mirrors a modern analytics vision:
- Proactive, not reactive
- Decision-driven, not report-driven
- Embedded into the flow of work

## Architecture
CSV / Google Sheets  
→ Python (analysis + insight logic)  
→ Slack alert

## Tools Used
- Python (pandas)
- Slack Incoming Webhooks
- CSV / Google Sheets
- GitHub

## How This Runs
This project runs fully online using GitHub Actions.
No local setup is required.

The workflow executes on a scheduled basis, analyzes revenue data,
and sends automated email insights to stakeholders.


## Example Insight
🚨 Revenue Alert  
Revenue pacing -6.3% vs target  
Suggested action: Review pipeline conversion and merchant activity

## How This Scales
- Rules → anomaly detection models
- CSV → data warehouse
- Text templates → LLM summaries
