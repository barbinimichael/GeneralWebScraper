# PageFetcher
# Retrieves new URLs given known ones
# 1) Start with initial URLs- the "seeds"
# 2) Visit pages
# 3) Identify all hyperlinks
# 4) Add links to queue of URLs- "crawler frontier"
# 5) Recursively visit

from requests import get
from requests.exceptions import RequestException
from contextlib import closing
import re
import googlesearch


# Start with initial URLs- the "seeds", given in file format
# Only if do not plan to begin with a general web search
def get_url(file):
    """
    Extract URLs from file, add to crawler frontier and return
    :param file:
    :return: url_queue
    """
    url_queue = []
    file_txt = open(file)

    for url in file_txt:
        if "\n" in url:
            # Remove next line character from url
            url = url[0:len(url)-1]
        url_queue.append(url)
    file_txt.close()
    return url_queue


# Do a google search for a given key word
# Use results page as seeds for hyperlinks
def web_search(keyword, num):
    googlesearch.search(keyword, num=num)


# 2) Visit pages
# Download Information
def get_html_content(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)


# 3) Identify all hyperlinks
def get_links(html_content, original_url):
    links = []

    for link in html_content.findAll('a', attrs={'href': re.compile("/")}):
        url = link.get('href')
        if len(url) > 1:
            if url[0] == "/":
                url = original_url + url
            links.append(url)

    return links
