def check_access(user, action):
    """
    Simulates access control checks based on the user's role and action.
    """
    if user["role"] == "Read-Only" and action in ["write", "delete"]:
        return False
    return True
