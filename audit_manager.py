import pandas as pd

# Initialize the global audit log as an empty DataFrame
audit_log = pd.DataFrame(columns=["User", "Role", "File", "Action", "Status"])

def log_action(user, role, file, action, status):
    global audit_log
    log = pd.DataFrame([[user, role, file, action, status]], columns=["User", "Role", "File", "Action", "Status"])
    audit_log = pd.concat([audit_log, log], ignore_index=True)
