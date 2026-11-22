import re
import requests
from bs4 import BeautifulSoup

URL = "https://afisha.relax.by/theatre/minsk/"
OUT = "theatre_events.txt"
HEADERS = {"User-Agent": "Mozilla/5.0"}

MONTHS = [
    "января", "февраля", "марта", "апреля", "мая", "июня",
    "июля", "августа", "сентября", "октября", "ноября", "декабря",
]


def clean(text):
    text = text.replace("\u200e", "").replace("\xa0", " ")
    return " ".join(text.split())


def get_soup(url):
    r = requests.get(url, headers=HEADERS, timeout=15)
    r.raise_for_status()
    return BeautifulSoup(r.text, "html.parser")


def find_date(text):
    words = text.lower().split()
    for i, w in enumerate(words):
        if w in MONTHS and i > 0 and words[i - 1].isdigit():
            day = words[i - 1]
            if 1 <= int(day) <= 31:
                if i + 1 < len(words) and ":" in words[i + 1]:
                    return f"{day} {w} {words[i + 1]}"
                return f"{day} {w}"
    return "не указано"


def parse_event(url):
    soup = get_soup(url)
    text = clean(soup.get_text(" ", strip=True))

    h1 = soup.find("h1")
    title = clean(h1.get_text()) if h1 else "Без названия"

    age = "не указано"
    for a in ["0+", "6+", "12+", "16+", "18+"]:
        if f" {a} " in f" {text} ":
            age = a
            break

    dt = find_date(text)

    venue = "не указано"
    for tag in soup.find_all(["a", "span", "div"]):
        t = clean(tag.get_text())
        low = t.lower()
        if any(w in low for w in ["театр", "дворец", "центр", "сцена", "филармония"]) and 5 <= len(t) <= 60:
            if not any(bad in low for bad in ["сегодня", "завтра", "билеты", "унп"]):
                venue = t
                break

    prices = [
        float(p.replace(",", "."))
        for p in re.findall(r"(\d+(?:[.,]\d+)?)\s*(?:руб|р\.|byn)", text.lower())
        if 1 <= float(p.replace(",", ".")) <= 5000
    ]

    return {
        "title": title,
        "dt": dt,
        "venue": venue,
        "age": age,
        "price": min(prices) if prices else None,
        "max_price": max(prices) if prices else None,
    }


def main():
    soup = get_soup(URL)
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if "/theatre/" in href and re.search(r"/\d{4,}", href) and href not in links:
            links.append(href)
        if len(links) == 15:
            break

    events = []
    for link in links:
        try:
            events.append(parse_event(link))
        except Exception:
            pass

    all_prices = [e["price"] for e in events if e["price"] is not None] + [
        e["max_price"] for e in events if e["max_price"] is not None
    ]
    min_p = min(all_prices) if all_prices else 0
    max_p = max(all_prices) if all_prices else 0
    avg_p = round(sum(all_prices) / len(all_prices), 2) if all_prices else 0

    venues = {}
    for e in events:
        if e["venue"] != "не указано":
            venues[e["venue"]] = venues.get(e["venue"], 0) + 1
    top_venue = max(venues, key=venues.get) if venues else "не указано"

    with_price = [e for e in events if e["price"] is not None]
    cheapest = min(with_price, key=lambda e: e["price"]) if with_price else None
    priciest = max(with_price, key=lambda e: e["max_price"] or e["price"]) if with_price else None

    lines = [
        f"Раздел: {URL}",
        f"Событий: {len(events)}",
        f"Мин. цена: {min_p} | Макс. цена: {max_p} | Средняя цена: {avg_p}",
        f"Самая загруженная площадка: {top_venue}",
        f"Самый дешёвый: {cheapest['title']} ({cheapest['price']})" if cheapest else "Самый дешёвый: нет данных",
        f"Самый дорогой: {priciest['title']} ({priciest['max_price'] or priciest['price']})" if priciest else "Самый дорогой: нет данных",
        "",
    ]
    for i, e in enumerate(events, 1):
        p_str = str(e["price"]) if e["price"] is not None else "не указана"
        lines.append(f"{i}. {e['title']} | {e['dt']} | {e['venue']} | Цена: {p_str} | {e['age']}")

    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print("Готово:", OUT)


if __name__ == "__main__":
    main()