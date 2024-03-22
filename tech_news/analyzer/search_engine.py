from datetime import datetime
from typing import List, Tuple
from tech_news.database import db


# Requisito 7
def search_by_title(title: str) -> List[Tuple[str, str]]:
    title = title.lower()
    result = []

    for news in db.news.find({"title": {"$regex": title, "$options": "i"}}):
        result.append((news["title"], news["url"]))

    return result


# Requisito 8
def search_by_date(date):

    if not date or len(date) != 10 or date[4] != "-" or date[7] != "-":
        raise ValueError("Data inválida")

    try:
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
    except ValueError:
        raise ValueError("Data inválida")

    result = []
    for news in db.news.find({"timestamp": formatted_date}):
        result.append((news["title"], news["url"]))

    return result


# Requisito 9
def search_by_category(category):
    cursor = db.news.find(
        {"category": {"$regex": f".*{category}.*", "$options": "i"}}
    )
    result = [(news["title"], news["url"]) for news in cursor]
    return result
