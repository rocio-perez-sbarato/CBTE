import os

data_folder = 'data'

for root, dirs, files in os.walk(data_folder):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            os.unlink(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
