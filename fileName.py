import os

def rename_files_in_directory(directory):
    # List of endings to remove
    remove_endings = ['-Enhanced-NR-Edit', '-Enhanced-NR']
    
    # Iterate through all the files in the directory
    for filename in os.listdir(directory):
        for ending in remove_endings:
            if ending in filename:
                new_name = filename.replace(ending, '')  # Replace the matching ending
                old_file_path = os.path.join(directory, filename)
                new_file_path = os.path.join(directory, new_name)
                os.rename(old_file_path, new_file_path)
                print(f'Renamed: {filename} -> {new_name}')
                break  # Exit the loop once an ending is replaced
        else:
            pass

# Directory path
directory_path = r"G:\My Drive\Tech Learning\Code\Python\fileName\Testing Files"

rename_files_in_directory(directory_path)
