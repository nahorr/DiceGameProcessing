# Dice Game Data Processing Project

## Overview

This project simulates data processing and analytics for a fictional "Dice Game" app launched in 2024. The goal is to transform raw user and activity data into a structured data warehouse format using Python and extract actionable business insights to inform planning for 2025.

## Technologies Used

- Python 3
- Pandas
- CSV-based file input/output
- Star Schema modeling

## Folder Structure

dice_game_project/
├── data/           # Raw input CSV files
├── outputs/        # Transformed dimension and fact tables
├── main.py         # Loads, transforms, and outputs data
├── validate.py     # Runs data integrity checks
├── insights.py     # Extracts business insights
└── README.md       # Project documentation

## How to Run the Application

> Make sure all CSV files are placed inside the `data/` folder before running the application.

### 1. Install dependencies
```bash
pip install pandas
```

### 2. Run the full processing pipeline
This will read raw data, transform it into a star schema, validate it, and output insights:

```bash
python main.py       # Transform data into fact/dim tables
python validate.py   # Run validation checks on the data
python insights.py   # Output key business insights
```

### Output Files
Located in the `outputs/` folder:
- dim_user.csv
- dim_channel.csv
- dim_status.csv
- dim_plan.csv
- fact_play_session.csv
- fact_user_plan.csv

## Business Insights Generated

- Session Distribution: Shows how users accessed the game (Browser vs Mobile)
- Subscription Breakdown: Onetime, Monthly, Annual plan usage
- Estimated Revenue: Calculates gross revenue from 2024 subscription data

## Validation Summary

- Checked for null values in critical tables
- Ensured foreign key integrity between user and session/plan records
- Validated plan date ranges (start before end)
- Checked for duplicate user IDs

## Notes

- One session record has a `user_id` that doesn't exist in the user table.
- Some users are missing `email` or `social_media_handle`, which is acceptable.

## Author

Nnamdi Okeke  
Senior Data Developer Candidate