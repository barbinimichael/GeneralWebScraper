# Runner for web scraper
# Michael Barbini
# 12/20/2018

from src import page_fetcher, analyze, miscellaneous, hidden
from bs4 import BeautifulSoup
import threading
import time


class WebScraper:
    """
    Web scraper designed to extract information on any form webpage
    """
    def __init__(self):
        self.url_queue = {}
        self.visited_links = []
        self.visited_links_file = None
        self.is_tor_setup = False
        self.session = None

    # Get URL from file
    def file_search(self, file):
        self.url_queue = page_fetcher.get_url(file)

    def google_search(self, keyword, num):
        self.url_queue = page_fetcher.web_search(keyword, num=num)

    def tor_search(self, keyword):
        if self.is_tor_setup:
            self.url_queue = hidden.google_search(keyword=keyword)
        else:
            self.setup_tor()

    def setup_tor(self, location):
        # first connect to tor network
        thread1 = threading.Thread(target=hidden.start_tor,
                                   args=(location,))
        thread1.start()

        time.sleep(4)

        self.session = hidden.start_tor_session()

        self.is_tor_setup = True

    def setup_log(self, folder_name):
        # Track visited links
        visited_links_file_name = folder_name + miscellaneous.format_date_time()
        self.visited_links_file = open(visited_links_file_name, "x")

    def write_log(self):
        # Write hyperlinks to external final
        visit_file = open(self.visited_links_file, "a")
        visit_file.write("\n".join(self.visited_links))
        visit_file.close()

    def process(self, queue, cap):
        for url in queue:
            if url not in self.visited_links and len(self.visited_links) <= cap:

                raw_html_content = page_fetcher.get_html_content(url)

                if raw_html_content:
                    html_content = BeautifulSoup(raw_html_content, 'html.parser')
                    # Do processing here
                    # analyze.analyze_general(html_content)

                    # Get hyperlinks
                    # new_queue = page_fetcher.get_links(html_content, url)
                    #
                    self.visited_links.append(url)
                    #
                    # Recurse
                    # process(new_queue)


raw_html_content = page_fetcher.get_html_content("https://en.wikipedia.org/wiki/Boronia_tenuis")
html_content = BeautifulSoup(raw_html_content, 'html.parser')
analyze.analyze_general(html_content)
