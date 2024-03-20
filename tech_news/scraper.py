from bs4 import BeautifulSoup
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
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        news_urls = []

        articles = soup.find_all("article", class_="entry-preview")

        for article in articles:
            link = article.find("a", href=True)
            if link:
                news_urls.append(link["href"])
        return news_urls
    except Exception as e:
        print(f"Erro ao fazer scrape: {e}")
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page_link = soup.find("a", rel="next")
    if not next_page_link:
        next_page_link = soup.find("a", href=True, string="Próxima")
    if next_page_link and next_page_link.has_attr("href"):
        return next_page_link["href"]

    return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
