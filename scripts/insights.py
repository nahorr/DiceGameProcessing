import pandas as pd

# Load data
sessions_df = pd.read_csv("outputs/fact_play_session.csv")
user_plan_df = pd.read_csv("outputs/fact_user_plan.csv")

# Play Sessions by Channel
session_counts = sessions_df['channel_code'].value_counts()
print("Sessions by Channel:")
print(session_counts)
print()

# Subscription Breakdown
plan_counts = user_plan_df['payment_frequency_code'].value_counts()
print("Subscription Types:")
print(plan_counts)
print()

# Estimated Gross Revenue for 2024
user_plan_df['start_date'] = pd.to_datetime(user_plan_df['start_date'], errors='coerce')
user_plan_df_2024 = user_plan_df[user_plan_df['start_date'].dt.year == 2024]
total_revenue = user_plan_df_2024['cost_amount'].sum()
print("Estimated Gross Revenue for 2024: $%.2f" % total_revenue)
