# There was no data generated for this project. This is only my code for computing hashes.

import hashlib

file_path = "IRENA_Stats_extract_2024 H2.xlsx"

with open(file_path, "rb") as file:
    file_data = file.read()
    md5_hash = hashlib.md5(file_data).hexdigest()

print(f"MD5 Hash of the Excel File: {md5_hash}")