import re
import os

def format_filename(file_name, max_length=255):
    """
    Formats a string to be a valid file name by removing or replacing invalid characters.
    
    Parameters:
    - file_name (str): The string to be formatted into a valid file name.
    - max_length (int): The maximum length of the file name. Default is 255 characters.
    
    Returns:
    - str: The formatted valid file name.
    """
    # Strip leading/trailing spaces
    file_name = file_name.strip()

    # Replace spaces with underscores
    file_name = file_name.replace(" ", "_")

    # Define a regular expression to match invalid characters (based on the OS)
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'  # Common invalid characters for Windows and Unix-based OS

    # Replace invalid characters with underscores
    file_name = re.sub(invalid_chars, "_", file_name)

    # Ensure the file name is not empty
    if not file_name:
        raise ValueError("File name cannot be empty after formatting.")

    # Truncate the file name to the max length if needed
    file_name = file_name[:max_length]

    # Ensure the file name does not end with a space or period
    file_name = file_name.rstrip(" .")

    return file_name

