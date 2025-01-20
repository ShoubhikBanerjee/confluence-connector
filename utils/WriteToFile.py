import os
from bs4 import BeautifulSoup
import logging

def write_to_file(content, directory, file_name, file_type="html"):
    """
    Writes HTML string, BeautifulSoup object, or PDF content to a file in a specified directory with the correct extension.
    
    Parameters:
    - content: Either a string containing HTML, a BeautifulSoup object, or PDF binary content.
    - directory: The directory path where the file should be saved.
    - file_name: The name of the file where the content should be saved (extension is added based on file_type).
    - file_type: Type of content - either "html", "soup", or "pdf" (default is "html").
    """
    # Ensure the directory exists, if not, create it
    os.makedirs(directory, exist_ok=True)

    # Determine the proper file extension based on file_type
    if file_type.lower() == "html":
        file_extension = ".html"
    elif file_type.lower() == "soup":
        file_extension = ".html"  # Use .html for BeautifulSoup object as well
    elif file_type.lower() == "pdf":
        file_extension = ".pdf"
    elif file_type.lower() == "markdown":
        file_extension = ".md"
    else:
        raise ValueError(f"Unsupported file type: {file_type}. Use 'html', 'soup', or 'pdf'.")

    # If the provided file_name doesn't already have the extension, append the proper one
    if not file_name.lower().endswith(file_extension):
        file_name += file_extension

    # Construct the full path to the file
    file_path = os.path.join(directory, file_name)

    # Handling HTML content (file_type == "html")
    if file_type.lower() == "html":
        # If content is a BeautifulSoup object, convert it to a string
        if isinstance(content, BeautifulSoup):
            content = str(content)

        # Open the file in write mode ('w') and write the HTML content
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        logging.info(f"HTML content has been written to {file_path}")

    # Handling BeautifulSoup object specifically (file_type == "soup")
    elif file_type.lower() == "soup":
        # Convert BeautifulSoup object to string and write to file
        if isinstance(content, BeautifulSoup):
            content = str(content)
        else:
            raise TypeError("Expected BeautifulSoup object for 'soup' file type.")

        # Open the file in write mode ('w') and write the content
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        logging.info(f"BeautifulSoup content has been written to {file_path}")
    
    # Handling PDF content (file_type == "pdf")
    elif file_type.lower() == "pdf":
        # If content is PDF binary (byte string), write it to a file
        with open(file_path, 'wb') as file:
            file.write(content)
        logging.info(f"PDF content has been written to {file_path}")

     # If the content is markdown text
    elif file_type.lower() == 'markdown': 
        content = str(content)
        # Write the markdown text directly to file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        logging.info(f"Markdown content has been written to {file_path}")
       


