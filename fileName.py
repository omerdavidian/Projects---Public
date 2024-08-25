import os

def rename_files_in_directory(directory):
    
    # Run through all the files in a directory and check for the folloing criteria
    for filename in os.listdir(directory):
        
        # Remove an ending of a file name "Photo1-Enhanced-NR-Edit.jpeg" --> "Photo1.jpeg"
        if '-Enhanced-NR-Edit' in filename:
            new_name = filename.replace('-Enhanced-NR-Edit', '') # Change text as needed
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_name)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_name}')   
        
        # Remove an ending of a file name "Photo1-Enhanced-NR.jpeg" --> "Photo1.jpeg"         
        elif '-Enhanced-NR' in filename:
            new_name = filename.replace('-Enhanced-NR', '') # Change text as needed
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_name)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: {filename} -> {new_name}')
        else:
            pass

# Directory path
directory_path = r"C:\Folder Location..."

rename_files_in_directory(directory_path)

# test 1

