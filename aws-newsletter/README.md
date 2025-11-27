# AWS Newsletter Subscription Application

A complete serverless newsletter subscription system using:
- AWS Lambda (Python)
- Amazon API Gateway
- Amazon SNS
- AWS IAM

Users subscribe through a simple HTML page, and SNS sends them a confirmation email.

## Files Included
- app.py — Lambda backend with CORS and SNS subscribe
- index.html — Simple frontend subscription form
- template.yaml — Optional AWS SAM deployment template
- .gitignore — Git ignore rules
- README.md — Documentation
