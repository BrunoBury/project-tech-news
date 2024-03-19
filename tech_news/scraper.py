# Requisito 1.
import time
import requests


def fetch(url):
    time.sleep(1)
    header = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(url, headers=header, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
