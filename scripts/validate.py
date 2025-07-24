import pandas as pd

# Load required datasets
user_df = pd.read_csv("data/user.csv")
user_registration_df = pd.read_csv("data/user_registration.csv")
user_play_session_df = pd.read_csv("data/user_play_session.csv")
user_plan_df = pd.read_csv("data/user_plan.csv")
user_payment_detail_df = pd.read_csv("data/user_payment_detail.csv")

# Null checks
print("Null values in user.csv:")
print(user_df.isnull().sum())
print()

print("Null values in user_registration.csv:")
print(user_registration_df.isnull().sum())
print()

print("Null values in user_play_session.csv:")
print(user_play_session_df.isnull().sum())
print()

# Foreign key integrity
missing_users = user_play_session_df[~user_play_session_df["user_id"].isin(user_df["user_id"])]
print("Play sessions with unknown user_id:", len(missing_users))

missing_reg_ids = user_plan_df[~user_plan_df["user_registration_id"].isin(user_registration_df["user_registration_id"])]
print("User plans with unknown user_registration_id:", len(missing_reg_ids))
print()

# Date range checks
user_plan_df['start_date'] = pd.to_datetime(user_plan_df['start_date'], errors='coerce')
user_plan_df['end_date'] = pd.to_datetime(user_plan_df['end_date'], errors='coerce')
invalid_dates = user_plan_df[user_plan_df['start_date'] > user_plan_df['end_date']]
print("User plans where start_date is after end_date:", len(invalid_dates))
print()

# Duplicate user IDs
duplicate_users = user_df[user_df.duplicated(subset='user_id')]
print("Duplicate user_id entries:", len(duplicate_users))
