import os

path = os.getcwd()

if not os.path.exists(path):
    print("Path does not exist.")

if os.access(path, os.R_OK):
    print(f"{path} is readable.")
else:
    print(f"{path} is not readable.")

if os.access(path, os.W_OK):
    print(f"{path} is writable.")
else:
    print(f"{path} is not writable.")

if os.access(path, os.X_OK):
    print(f"{path} is executable.")
else:
    print(f"{path} is not executable.")
