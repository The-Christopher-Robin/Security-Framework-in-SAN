import pandas as pd

# Initialize the DataFrame if it doesn't exist already
def initialize_log_df():
    return pd.DataFrame(columns=["user_name", "role", "file_name", "action", "status"])

def log_action(user_name, role, file_name, action, status, log_df):
    # Create a new row as a DataFrame
    new_entry = pd.DataFrame([{
        "user_name": user_name,
        "role": role,
        "file_name": file_name,
        "action": action,
        "status": status
    }])

    # Concatenate the new entry to the existing DataFrame
    log_df = pd.concat([log_df, new_entry], ignore_index=True)
    
    return log_df
