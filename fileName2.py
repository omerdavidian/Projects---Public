import os

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        # Split the filename at the first occurrence of '-' and keep only the part before it
        if '-' in filename:
            new_name = filename.split('-', 1)[0] + os.path.splitext(filename)[1]  # Keep the file extension
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_name)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_name}')
        else:
            pass

# Directory path
directory_path = r"G:\My Drive\Tech Learning\Code\Python\fileName\Testing Files"

rename_files_in_directory(directory_path)
