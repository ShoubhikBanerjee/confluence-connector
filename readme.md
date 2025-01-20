# Confluence Connector Documentation

## Overview

**Confluence Connector** is a Python project designed to connect to a Confluence instance, scrape content from pages, and save the data in various formats such as **PDF**, **HTML**, **BeautifulSoup**, and **Markdown**.

## Features

- **Confluence Integration**: Easily connect to your Confluence instance and scrape pages.
- **Multiple Output Formats**: Output data in `PDF`, `HTML`, BeautifulSoup(`soup`), or `Markdown` format.
- **Environment Configurable**: Use environment variables for setting Confluence URL, personal access token (PAT), output format, and directories.

## Requirements

To use the **Confluence Connector**, make sure you have the following Python libraries installed:

- `atlassian-python-api==3.41.18`
- `markitdown==0.0.1a3`
- `beautifulsoup4==4.12.3`
- `pandas==2.2.3`

You can install them via:

```bash
python -m virtualenv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

## Setup and Configuration

1. Set the following environment variables:

    ```env
    export CONFLUENCE_HOST=https://yourcompany.atlassian.net
    export CONFLUENCE_PAT=your_personal_access_token
    export CONFLUENCE_PAGE_OUTPUT_FORMAT=PDF
    export INIT_PAGE_ID=123456789
    export OUTPUT_DIR=Output/
    ```

2. Run the script using the following command:

    ```bash
    python app.py
    ```

## How it Works

1. The scraper connects to the **Confluence API** using the **Personal Access Token (PAT)** and the **Confluence Host** URL.
2. It fetches the page by the provided **page ID** (`INIT_PAGE_ID`).
3. Based on the **output format** (`CONFLUENCE_PAGE_OUTPUT_FORMAT`), the content is either saved as a `PDF`, `HTML`, `Soup` object, or `Markdown`.
4. The scraped content is stored in the specified **output directory** (`OUTPUT_DIR`).
4. The application logs content is stored in the specified **Logs directory** (`Logs`).


## Contributing

We welcome contributions to this project! If you have any improvements, bug fixes, or suggestions, feel free to follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them with a clear message.
4. Push your changes to your forked repository.
5. Open a pull request with a description of your changes.

Please make sure your code follows the project's coding style and includes appropriate tests.

We appreciate your help in making this project better!


Made with ❤️ by Shoubhik Banerjee
