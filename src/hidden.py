import requests
from stem import Signal
from stem.control import Controller
from lxml import html
from src import miscellaneous
import os
import random


def start_tor(address):
    """
    Begin tor application
    :param address: file address of tor application
    """
    os.system(address)


def start_tor_session():
    """
    Start a session that uses tor port
    :return: session
    """
    session = requests.session()
    session.proxies = dict()
    session.proxies['http'] = 'socks5h://localhost:9150'
    session.proxies['https'] = 'socks5h://localhost:9150'

    session.cookies.clear()

    return session


def google_search(session, keyword):
    """
    Search for a keyword using tor port
    :param session: Requests session
    :param keyword: String to search
    :return: List of hyperlinks returned from search
    """
    renew_ip()

    url = 'http://www.google.com/search?q=' + keyword + '&ie=utf-8&oe=utf-8'
    result = session.get(url, timeout=2, headers=new_header())

    webpage = html.fromstring(result.content)
    hyperlinks = webpage.xpath('//a/@href')

    # Filter hyperlinks
    hyperlinks = [link for link in hyperlinks if "https://" in str(link)]
    hyperlinks = list(map(lambda x: x.replace('/url?q=', ''), hyperlinks))

    return hyperlinks


def get_page(session, url):
    """
    Retrieve html content from web page
    :param session: Requests session
    :param url: URL string
    :return: html content
    """
    return session.get(url, timeout=2, headers=new_header())


def new_header():
    """
    New header for session
    :return: headers
    """
    headers = dict()
    headers['User-agent'] = miscellaneous.random_string(random.randint(1, 20))
    return headers


def renew_ip():
    """
    Obtain a new IP for tor port
    """
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
