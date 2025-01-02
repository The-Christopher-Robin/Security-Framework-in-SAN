import random
import pandas as pd
from log_functions import log_action, initialize_log_df
import time

# Initialize the log dataframe
log_df = initialize_log_df()

# List of example users and file names
users = [
    {"name": "User_1", "role": "Admin"},
    {"name": "User_2", "role": "Editor"},
    {"name": "User_3", "role": "Viewer"},
    {"name": "User_4", "role": "Admin"},
    {"name": "User_5", "role": "Editor"},
]

files = [f"file_{i}.txt" for i in range(1, 11)]  # Dynamically generate 10 example files
actions = ["create", "delete", "update", "view"]

# Generate and log 100 random actions
for _ in range(100):
    user = random.choice(users)  # Randomly pick a user
    file = random.choice(files)  # Randomly pick a file
    action = random.choice(actions)  # Randomly pick an action
    status = random.choice(["Success", "Failure"])  # Randomly pick a status
    
    # Log the action and update the dataframe
    log_df = log_action(user["name"], user["role"], file, action, status, log_df)

# Save the log data to a CSV file
log_df.to_csv('log_file.csv', index=False)

print(f"Logged {len(log_df)} actions to log_file.csv.")


test = input("Enter Y/N to see metrics: ")
if test.lower() == 'y':
    from metrics import generate_metrics
    generate_metrics(log_df)