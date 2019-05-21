# Runner for web scraper
# Michael Barbini
# 12/20/2018

from src import page_fetcher
from src import analyze
from src import miscellaneous
from bs4 import BeautifulSoup


# Ready url queue
file = "C:/Users/micha/PycharmProjects/GeneralWebScraper/URLs/medium.txt"
url_queue = page_fetcher.get_url(file)

# Track visited links
visited_links_file_name = "C:/Users/micha/PycharmProjects/GeneralWebScraper/URLs/Visited Links/" + \
                          miscellaneous.format_date_time()
visited_links_file = open(visited_links_file_name, "x")
visited_links = []


def process(queue):
    """
    Recursively extracts data and proceeds to all found hyperlinks
    :param queue
    """

    for url in queue:
        if url not in visited_links and len(visited_links) <= 20:

            raw_html_content = page_fetcher.get_html_content(url)

            if raw_html_content:
                html_content = BeautifulSoup(raw_html_content, 'html.parser')
                # Do processing here
                analyze.analyze_general(html_content)

                # Get hyperlinks
                new_queue = page_fetcher.get_links(html_content, url)
                #
                visited_links.append(url)
                #
                # # Recurse
                process(new_queue)


process(url_queue)
print(visited_links)
# Write hyperlinks to external final
visit_file = open(visited_links_file_name, "a")
visit_file.write("\n".join(visited_links))
visit_file.close()


