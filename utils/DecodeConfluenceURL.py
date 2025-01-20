import re
from urllib.parse import unquote
def extract_confluence_info_by_url(url):
    # Define the regex pattern to extract space and title
    pattern = r'https://(?:[\w\-]+\.)?[\w\-]+\.com/confluence/display/([^/]+)/([^/]+)'

    # Try to match the pattern
    match = re.match(pattern, url)

    if match:
        space = match.group(1)
        title = match.group(2)

        # Replace the '+' with spaces before URL decoding
        title_with_spaces = title.replace('+', ' ')

        # URL decode the title to convert '+' to spaces
        decoded_title = unquote(title_with_spaces)

        # Create the JSON object
        result = {
            "space": space,
            "title": decoded_title
        }

        return result
    else:
        return None  # Return None if the URL doesn't match the pattern