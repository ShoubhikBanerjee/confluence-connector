from utils.DecodeConfluenceURL import extract_confluence_info_by_url
from utils import ConfluenceHandler
import logging

def parse_inner_pages(url, confluence_host, access_token, output_format='PDF'):
    url = str(url)

    ConfluenceHandler.init_confluence_obj(confluence_host=confluence_host, access_token=access_token)

    if '?pageid=' in url.lower():
        inner_page_id = url.lower().split('?pageid=')[1]
        logging.info(f'Parsing page with id : {inner_page_id}')
        try:
            page_content, page_title = ConfluenceHandler.get_confluence_page_content(page_id=inner_page_id, output_format=output_format)
            return page_content, page_title
        except Exception as e:
            return None, e
    else:
        page_info = extract_confluence_info_by_url(url=url)
        if page_info is None:
            raise Exception('Invalid page info provided in url')
        else:
            confluence_space = page_info['space']
            page_title = page_info['title']

            try:
                logging.info(f'Parsing page with space : {confluence_space} and page title : {page_title}')
                page_content, page_title = ConfluenceHandler.get_confluence_page_content(space=confluence_space, page_title=page_title, output_format=output_format)
                return page_content, page_title
            except Exception as e:
                return None, e

        