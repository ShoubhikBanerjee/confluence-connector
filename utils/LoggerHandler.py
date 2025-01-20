import logging
import os



def create_log_file(log_file_path, log_level=logging.INFO):
    """
    Creates a log file and configures logging settings.
    
    Parameters:
    - log_file_path (str): The path where the log file will be created.
    - log_level (int): The logging level (e.g., logging.DEBUG, logging.INFO). Default is INFO.
    """
    # Ensure the directory for the log file exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

    # Create a logger
    logger = logging.getLogger()

    # Set the logging level (can be DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(log_level)

    # Create a file handler to write logs to a file
    file_handler = logging.FileHandler(log_file_path)

    # Define the log message format (e.g., timestamp, log level, message)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Apply the formatter to the file handler
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Optionally, also log to the console (stdout)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # # Example log entries
    # logger.info("Log file created successfully.")
    # logger.debug("This is a debug message.")
    # logger.warning("This is a warning message.")
    # logger.error("This is an error message.")
    # logger.critical("This is a critical message.")

    print(f"Log file created at: {log_file_path}")

# # Example usage:
# log_file_path = 'logs/my_application.log'
# create_log_file(log_file_path, log_level=logging.DEBUG)
