import os
from datetime import datetime
from pathlib import Path
import logging

def create_dir(dir_path):
    # Create directory if it doesn't exist
    os.makedirs(dir_path, exist_ok=True)
    logging.info(f"Directory '{dir_path}' is created (if it didn't exist already).")


def create_directory_with_timestamp(base_path, timestamp_format='%Y%m%d_%H%M%S'):
    """
    Creates a directory with a timestamp in its name.
    
    Parameters:
    - base_path: The base path where the directory should be created.
    - timestamp_format: The format for the timestamp (default is '%Y%m%d_%H%M%S').
    
    Returns:
    - The path of the created directory.
    """
    # Get current timestamp formatted according to the provided format
    timestamp = datetime.now().strftime(timestamp_format)
    
    # Combine the base path with the timestamp using '/'
    dir_path = Path(f'{base_path}/{timestamp}')
    
    # Create the directory if it doesn't exist
    dir_path.mkdir(parents=True, exist_ok=True)
    
    return dir_path


