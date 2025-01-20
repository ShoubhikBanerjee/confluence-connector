
from atlassian import Confluence
import bs4 as bs


confluence_obj = None

def init_confluence_obj(confluence_host, access_token):
    global confluence_obj
    confluence_obj = Confluence(url=confluence_host, token=access_token)
    return confluence_obj

def get_confluence_page_content(page_id=None, space=None, page_title=None, output_format='HTML'): # output can be HTML or SOUP or PDF
    global confluence_obj  # Use global to refer to the global Confluence object
    
    # Check if the Confluence object is initialized
    if confluence_obj is None:
        raise Exception('Confluence object is not initialized yet. Use `init_confluence_obj` to initialize the object.')
    
    # If both page_id and (space, page_title) are provided, raise an exception
    if page_id is not None and (space is not None or page_title is not None):
        raise Exception('Both `page_id` and `space`/`page_title` cannot be provided simultaneously. Please provide only one option.')
    
    # If page_id is provided, fetch the page by its ID
    if page_id is not None:
        res = confluence_obj.get_page_by_id(page_id, expand='space,body.view,version,container', status=None, version=None)
        html_body = res['body']['view']['value']
        title = res['title']
        if str(output_format).lower() == 'html':
            return html_body, title
        elif str(output_format).lower() == 'soup':
            return bs.BeautifulSoup(html_body,'html'), title
        elif str(output_format).lower() == 'pdf':
            return confluence_obj.export_page(page_id), title
        else:
            raise Exception(f'Invalid `output_format` provided. Received value : `{output_format}` but supports only `HTML`, `SOUP` or `PDF`.')
            

    # If space and page_title are provided, fetch the page by space and title
    if space is not None and page_title is not None:
        res = confluence_obj.get_page_by_title(space, page_title, expand='space,body.view,version,container')
        html_body = res['body']['view']['value']
        title = res['title']
        if str(output_format).lower() == 'html':
            return html_body, title
        elif str(output_format).lower() == 'soup':
            return bs.BeautifulSoup(html_body,'html'), title
        elif str(output_format).lower() == 'pdf':
            return confluence_obj.export_page(res['id']), title
        else:
            raise Exception(f'Invalid `output_format` provided. Received value : `{output_format}` but supports only `HTML` or `SOUP`.')
    
    # If neither page_id nor (space and page_title) are provided, raise an error
    raise Exception('Either `page_id` or both `space` and `page_title` must be provided.')

    




