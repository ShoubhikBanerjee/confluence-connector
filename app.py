import os
import logging
from markitdown import MarkItDown
from utils import ConfluenceHandler, InitConfluencePageHandler, ParseConfluenceInnerPage, CreateDirectory, WriteToFile, FormatFileName, LoggerHandler

md = MarkItDown()

ALLOWED_CONFLUENCE_PAGE_OUTPUT_FORMAT = ['html', 'soup', 'pdf', 'markdown']

CONFLUENCE_HOST = os.getenv('CONFLUENCE_HOST', None)
CONFLUENCE_PAT = os.getenv('CONFLUENCE_PAT', None)
CONFLUENCE_PAGE_OUTPUT_FORMAT = os.getenv('CONFLUENCE_PAGE_OUTPUT_FORMAT', 'PDF') # HTML / SOUP / PDF / MARKDOWN
INIT_PAGE_ID = os.getenv('INIT_PAGE_ID', None)
OUTPUT_DIR = os.getenv('OUTPUT_DIR', 'Output/')

if CONFLUENCE_HOST == None:
    raise Exception('Please provide a valid CONFLUENCE_HOST in enviornment variables.')
if CONFLUENCE_PAT == None:
    raise Exception('Please provide a valid CONFLUENCE_PAT in enviornment variables.')
if INIT_PAGE_ID == None:
    raise Exception('Please provide a valid INIT_PAGE_ID in enviornment variables to start with.')
if CONFLUENCE_PAGE_OUTPUT_FORMAT == None:
    logging.info('Since `CONFLUENCE_PAGE_OUTPUT_FORMAT` is not set in envionment variables, using default value : `PDF`.')
if OUTPUT_DIR == None:
    logging.info('Since `OUTPUT_DIR` is not set in envionment variables, using default value : `Output/`.')


if str(CONFLUENCE_PAGE_OUTPUT_FORMAT).lower() not in ALLOWED_CONFLUENCE_PAGE_OUTPUT_FORMAT:
    raise Exception(f'Unsupported `CONFLUENCE_PAGE_OUTPUT_FORMAT` is provided. Got : `{CONFLUENCE_PAGE_OUTPUT_FORMAT}`, but expection either of `{",".join(ALLOWED_CONFLUENCE_PAGE_OUTPUT_FORMAT)}`.')

REQUESTED_CONFLUENCE_PAGE_OUTPUT_FORMAT = CONFLUENCE_PAGE_OUTPUT_FORMAT
if CONFLUENCE_PAGE_OUTPUT_FORMAT.lower() == 'markdown':
    CONFLUENCE_PAGE_OUTPUT_FORMAT = 'SOUP'

LOG_FILE_DIR_BASE = 'Logs/'
LOG_FILE_NAME = 'applocation.log'

LOG_FILE_DIR_PATH = CreateDirectory.create_directory_with_timestamp(base_path=LOG_FILE_DIR_BASE)

# Call the logging setup function
LoggerHandler.create_log_file(os.path.join(LOG_FILE_DIR_PATH, LOG_FILE_NAME), log_level=logging.INFO)

ConfluenceHandler.init_confluence_obj(confluence_host=CONFLUENCE_HOST, access_token=CONFLUENCE_PAT)

init_page_content, init_page_title = ConfluenceHandler.get_confluence_page_content(page_id=INIT_PAGE_ID, output_format='SOUP')

init_table_df = InitConfluencePageHandler.find_init_page_table(init_page_content)

dir_path = CreateDirectory.create_directory_with_timestamp(base_path=OUTPUT_DIR)

# Get number of rows using .shape
num_of_urls_to_be_procesed = init_table_df.shape[0]

failed_urls = []

for index, row in init_table_df.iterrows():
    url = str(row['URL_ACTUAL'])
    logging.info(f'URL to parse => {url}')

    page_content, page_title = ParseConfluenceInnerPage.parse_inner_pages(url=url, confluence_host=CONFLUENCE_HOST, access_token=CONFLUENCE_PAT, output_format=CONFLUENCE_PAGE_OUTPUT_FORMAT)

    if page_content == None:
        logging.error(f'Unable to parse content for url : {url}. Reason : {page_title}')
        failed_urls.append(url)
    else:
        file_name = FormatFileName.format_filename(page_title)
        WriteToFile.write_to_file(content=page_content, directory=dir_path, file_name=file_name, file_type=CONFLUENCE_PAGE_OUTPUT_FORMAT)
        if REQUESTED_CONFLUENCE_PAGE_OUTPUT_FORMAT.lower() == 'markdown':
            md_result = md.convert(f'{os.path.join(dir_path,file_name)}.html')
            WriteToFile.write_to_file(content=md_result.text_content, directory=dir_path, file_name=file_name, file_type=REQUESTED_CONFLUENCE_PAGE_OUTPUT_FORMAT)

        

logging.info('\n\n------ Done Processing |  Summary : ---------\n')

logging.info(f'Total URLs to be processed : {num_of_urls_to_be_procesed}')
logging.info(f'Successfully parsed URLs count : {num_of_urls_to_be_procesed - len(failed_urls)}')
logging.info(f'Failed URLs count : {len(failed_urls)}')
logging.info(f'URLs that failed : {"\n".join(failed_urls)}')
logging.info('\n\n------ END ---------\n')

    


