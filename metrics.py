# metrics.py

import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate and display metrics
def generate_metrics(log_df):
    # User Action Summary (Total actions per user)
    user_action_count = log_df.groupby("user_name").size()
    print("\nUser Action Count:")
    print(user_action_count)
    
    # Action Distribution (Create, Delete, View, Update)
    action_distribution = log_df["action"].value_counts()
    print("\nAction Distribution:")
    print(action_distribution)
    
    # Action Success Rate
    action_success_rate = log_df.groupby("action")["status"].value_counts(normalize=True).unstack().fillna(0)
    print("\nAction Success Rate:")
    print(action_success_rate)
    
    # User Role Analysis
    role_action_count = log_df.groupby("role")["action"].value_counts().unstack().fillna(0)
    print("\nRole Action Count:")
    print(role_action_count)

    # File Action Breakdown
    file_action_count = log_df.groupby("file_name")["action"].value_counts().unstack().fillna(0)
    print("\nFile Action Breakdown:")
    print(file_action_count)

    # --- Plotting ---
    plt.figure(figsize=(10, 6))
    
    # Action Distribution Plot
    plt.subplot(2, 2, 1)
    action_distribution.plot(kind="bar", color="skyblue")
    plt.title("Action Distribution")
    plt.xlabel("Action")
    plt.ylabel("Count")
    
    # User Action Count Plot
    plt.subplot(2, 2, 2)
    user_action_count.plot(kind="bar", color="orange")
    plt.title("User Action Count")
    plt.xlabel("User")
    plt.ylabel("Action Count")
    
    # Success/Failure Rate Plot
    plt.subplot(2, 2, 3)
    action_success_rate.plot(kind="bar", stacked=True)
    plt.title("Action Success Rate")
    plt.xlabel("Action")
    plt.ylabel("Rate")
    
    # Role Action Distribution Plot
    plt.subplot(2, 2, 4)
    role_action_count.plot(kind="bar", stacked=True)
    plt.title("Role Action Distribution")
    plt.xlabel("Role")
    plt.ylabel("Action Count")
    
    plt.tight_layout()
    plt.show()
