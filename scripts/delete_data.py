# delete all the data files created so far...
import os

data_dir = "data"

for root, dirs, files in os.walk(data_dir):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f" Failed to delete {file_path}: {e}")
