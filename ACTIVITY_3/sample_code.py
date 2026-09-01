import os

def calculate_size(path):
    """
    Recursively calculates the total size of all files under a given path.
    
    Base case: if path is a file, return its size.
    Recursive case: if path is a directory, sum sizes of all contents.
    """
    # BASE CASE: It's a file — just return its size
    if os.path.isfile(path):
        return os.path.getsize(path)
    
    # RECURSIVE CASE: It's a directory — explore every entry inside
    total = 0
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        total += calculate_size(full_path)  # recursive call
    
    return total

# Example usage
folder_path = r"C:\Users\jvinc\Downloads"  # change this to any folder
print(f"Total size: {calculate_size(folder_path)} bytes")
