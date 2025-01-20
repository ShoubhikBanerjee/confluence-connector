import pandas as pd

def find_init_page_table(html_soup):

    table = html_soup.find_all('table')
    df = pd.read_html(str(table))[0]
    df.columns = df.iloc[0]
    # Drop row with index 0 (1st row)
    df = df.drop(index=0)
    # Convert column names to uppercase
    df.columns = df.columns.str.upper()

    # Extract the URLs and Labels (text of <a> tags)
    urls = [a['href'] for a in html_soup.find_all('a', href=True)]
    labels = [a.text for a in html_soup.find_all('a')]

    # Create a DataFrame from the extracted data
    df2 = pd.DataFrame({
        'URL_ACTUAL': urls,
        'Label': labels
    })

    merged_df = pd.concat([df.reset_index(drop=True), df2.reset_index(drop=True)], axis=1)

    return merged_df
