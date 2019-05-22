import requests
from stem import Signal
from stem.control import Controller
from lxml import html
from src import miscellaneous
import os


# Do a google search for a given key word
# Use results page as seeds for hyperlinks
# Use tor to do search
def hidden_search(keyword):
    renew_ip()
    session = requests.session()
    session.proxies = dict()
    session.proxies['http'] = 'socks5h://localhost:9150'
    session.proxies['https'] = 'socks5h://localhost:9150'

    session.cookies.clear()

    headers = dict()
    headers['User-agent'] = miscellaneous.random_string(10)

    url = 'http://www.google.com/search?q=' + keyword + '&ie=utf-8&oe=utf-8'
    result = session.get(url, timeout=2, headers=headers)

    webpage = html.fromstring(result.content)
    hyperlinks = webpage.xpath('//a/@href')

    hyperlinks = [link for link in hyperlinks if "https://" in str(link)]

    hyperlinks = list(map(lambda x: x.replace('/url?q=', ''), hyperlinks))

    return hyperlinks


def start_tor(address):
    os.system(address)


def renew_ip():
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
