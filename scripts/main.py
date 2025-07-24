import pandas as pd
import os

# Paths
DATA_DIR = "data"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load CSV files
channel_code_df = pd.read_csv(f"{DATA_DIR}/channel_code.csv")
plan_df = pd.read_csv(f"{DATA_DIR}/plan.csv")
plan_payment_frequency_df = pd.read_csv(f"{DATA_DIR}/plan_payment_frequency.csv")
status_code_df = pd.read_csv(f"{DATA_DIR}/status_code.csv")
user_df = pd.read_csv(f"{DATA_DIR}/user.csv")
user_payment_detail_df = pd.read_csv(f"{DATA_DIR}/user_payment_detail.csv")
user_plan_df = pd.read_csv(f"{DATA_DIR}/user_plan.csv")
user_play_session_df = pd.read_csv(f"{DATA_DIR}/user_play_session.csv")
user_registration_df = pd.read_csv(f"{DATA_DIR}/user_registration.csv")

# DIMENSION TABLES

# dim_user: user + registration info
dim_user = pd.merge(user_df, user_registration_df, on="user_id", how="left")

# dim_channel
dim_channel = channel_code_df.rename(columns={
    "play_session_channel_code": "channel_code",
    "english_description": "channel_description"
})

# dim_status
dim_status = status_code_df.rename(columns={
    "play_session_status_code": "status_code",
    "english_description": "status_description"
})

# dim_plan
dim_plan = pd.merge(plan_df, plan_payment_frequency_df, on="payment_frequency_code", how="left")

# FACT TABLES

# fact_play_session: play session enriched with channel and status
fact_play_session = pd.merge(user_play_session_df, dim_channel, on="channel_code", how="left")
fact_play_session = pd.merge(fact_play_session, dim_status, on="status_code", how="left")

# fact_user_plan: user plans + payment + plan info
fact_user_plan = pd.merge(user_plan_df, user_payment_detail_df, on="payment_detail_id", how="left")
fact_user_plan = pd.merge(fact_user_plan, dim_plan, on="plan_id", how="left")

# SAVE OUTPUTS

dim_user.to_csv(f"{OUTPUT_DIR}/dim_user.csv", index=False)
dim_channel.to_csv(f"{OUTPUT_DIR}/dim_channel.csv", index=False)
dim_status.to_csv(f"{OUTPUT_DIR}/dim_status.csv", index=False)
dim_plan.to_csv(f"{OUTPUT_DIR}/dim_plan.csv", index=False)
fact_play_session.to_csv(f"{OUTPUT_DIR}/fact_play_session.csv", index=False)
fact_user_plan.to_csv(f"{OUTPUT_DIR}/fact_user_plan.csv", index=False)

print("✅ All dimension and fact tables generated and saved to 'outputs/' folder.")
