import kagglehub
import yaml
import os
import shutil

# Load config
with open("config.yaml", "r") as f:
    cfg = yaml.safe_load(f)

# Iterate through all entries in the 'paths' section
if 'paths' in cfg:
    for path_name, path_value in cfg['paths'].items():
        os.makedirs(path_value, exist_ok=True)
        print(f"Verified directory: {path_value} (for {path_name})")
else:
    print("Error: 'paths' section not found in config.yaml")

# Get the data directory
target_dir = cfg['paths']['data_dir']

# Download latest version of the data set
cache_path = kagglehub.dataset_download("asifxzaman/university-students-performance-and-study-habits2026")

for filename in os.listdir(cache_path):
    source_file = os.path.join(cache_path, filename)
    target_file = os.path.join(target_dir, filename)

    shutil.move(source_file, target_file)
    print(f"\nDataset successfully synced to: {os.path.abspath(target_dir)}")