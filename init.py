import kagglehub
import yaml
import os
import shutil

# Load config
with open("config.yaml", "r") as f:
    cfg = yaml.safe_load(f)

# Get the data directory
target_dir = cfg['paths']['data_dir']

# Create a dir if not exists
os.makedirs(target_dir, exist_ok=True)

# Download latest version of the data set
cache_path = kagglehub.dataset_download("asifxzaman/university-students-performance-and-study-habits2026")

for filename in os.listdir(cache_path):
    source_file = os.path.join(cache_path, filename)
    target_file = os.path.join(target_dir, filename)

    shutil.move(source_file, target_file)
    print(f"\nDataset successfully synced to: {os.path.abspath(target_dir)}")