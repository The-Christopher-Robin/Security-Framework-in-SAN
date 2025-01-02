import random
import string

# data_simulation.py (example)
def generate_files(num_files, file_size):
    files = {}
    for i in range(num_files):
        file_name = f"file_{i+1}.txt"
        files[file_name] = "a" * file_size  # Simulating file content
    return files

def generate_users(num_users):
    users = []
    for i in range(num_users):
        user = {
            "name": f"User_{i+1}",
            "role": random.choice(["Admin", "Read-Only", "Read-Write"])
        }
        users.append(user)
    return users
