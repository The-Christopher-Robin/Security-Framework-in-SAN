import hashlib
import random

# Hashing function
def hash_file(file_data):
    return hashlib.sha256(file_data.encode()).hexdigest()

# Verify file integrity
def verify_integrity(file_data, stored_hash):
    return hash_file(file_data) == stored_hash

# Corrupt a random file
def simulate_corruption(files):
    file_to_corrupt = random.choice(list(files.keys()))
    files[file_to_corrupt] += "corruption"
    return file_to_corrupt
