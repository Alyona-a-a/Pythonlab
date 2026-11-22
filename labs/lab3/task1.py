import re
import requests
from bs4 import BeautifulSoup

SECTION_URL = "https://afisha.relax.by/theatre/minsk/"
OUTPUT_FILE = "theatre_events.txt"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


def fetch_soup(url: str) -> BeautifulSoup:
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def clean(text: str) -> str:
    text = text.replace("\u200e", "").replace("\u200f", "").replace("\xa0", " ")
    return " ".join(text.split())


def extract_prices(text: str) -> list[float]:
    found = []
    for m in re.findall(r"(\d+(?:[.,]\d+)?)\s*(?:руб|р\.|byn)", text.lower()):
        val = float(m.replace(",", "."))
        if 1 <= val <= 5000:
            found.append(val)
    return found


def detect_venue(soup: BeautifulSoup) -> str:
    bad_words = [
        "сегодня", "завтра", "понедельник", "вторник", "среда",
        "четверг", "пятница", "суббота", "воскресенье", "билеты", "афиша",
    ]
    bad_prefixes = ("вс,", "ср,", "чт,", "пт,", "сб,", "пн,", "вт,")
    for el in soup.find_all(["a", "span", "div"]):
        t = clean(el.get_text())
        low = t.lower()
        if any(b in low for b in bad_words) or low.startswith(bad_prefixes):
            continue
        if any(k in low for k in ["театр", "дворец", "центр", "дом культуры", "сцена", "филармония"]):
            if 5 <= len(t) <= 70:
                return t
    return "не указано"


def parse_event_page(url: str) -> dict:
    soup = fetch_soup(url)
    page_text = clean(soup.get_text(" ", strip=True))

    h1 = soup.find("h1")
    title = clean(h1.get_text()) if h1 else ""

    age_match = re.search(r"\b(0\+|6\+|12\+|16\+|18\+)\b", page_text)
    age = age_match.group(1) if age_match else "не указано"

    date_match = re.search(
        r"\b\d{1,2}\s+(?:января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)(?:\s+\d{4})?(?:\s*,?\s*\d{1,2}:\d{2})?\b",
        page_text.lower(),
    )
    dt = date_match.group(0) if date_match else "не указано"

    venue = detect_venue(soup)
    prices = extract_prices(page_text)
    min_p = min(prices) if prices else None
    max_p = max(prices) if prices else None

    return {
        "title": title,
        "dt": dt,
        "venue": venue,
        "min_price": min_p,
        "max_price": max_p,
        "age": age,
        "url": url,
    }


def collect_events(section_url: str, limit: int = 15) -> list[dict]:
    soup = fetch_soup(section_url)
    links = []
    seen = set()

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if "/theatre/" in href and re.search(r"/\d{4,}", href):
            if href not in seen:
                seen.add(href)
                links.append(href)
        if len(links) >= limit:
            break

    events = []
    for link in links:
        try:
            item = parse_event_page(link)
            if item["title"]:
                events.append(item)
        except Exception:
            continue
    return events


def build_report(events: list[dict]) -> str:
    all_prices = []
    venues = {}
    cheapest = None
    priciest = None

    for ev in events:
        v = ev["venue"]
        if v != "не указано":
            venues[v] = venues.get(v, 0) + 1
        if ev["min_price"] is not None:
            all_prices.append(ev["min_price"])
            if cheapest is None or ev["min_price"] < cheapest["min_price"]:
                cheapest = ev
        if ev["max_price"] is not None:
            all_prices.append(ev["max_price"])
            if priciest is None or ev["max_price"] > priciest["max_price"]:
                priciest = ev

    top_venue = max(venues.items(), key=lambda x: x[1])[0] if venues else "не определена"
    min_price = min(all_prices) if all_prices else 0
    max_price = max(all_prices) if all_prices else 0
    avg_price = round(sum(all_prices) / len(all_prices), 2) if all_prices else 0

    lines = [
        f"Раздел: {SECTION_URL}",
        f"Событий обработано: {len(events)}",
        f"Мин. цена билета: {min_price}",
        f"Макс. цена билета: {max_price}",
        f"Средняя цена билета: {avg_price}",
        f"Самая загруженная площадка: {top_venue}",
        f"Самый дешёвый билет: {cheapest['title']} ({cheapest['min_price']})" if cheapest else "Самый дешёвый билет: нет данных",
        f"Самый дорогой билет: {priciest['title']} ({priciest['max_price']})" if priciest else "Самый дорогой билет: нет данных",
        "",
    ]

    for i, ev in enumerate(events, 1):
        price_str = f"{ev['min_price']}..{ev['max_price']}" if ev["min_price"] is not None else "не указана"
        lines.append(
            f"{i}. {ev['title']} | Дата/время: {ev['dt']} | Место: {ev['venue']} | "
            f"Цена: {price_str} | Возраст: {ev['age']}"
        )

    return "\n".join(lines) + "\n"


def main() -> None:
    events = collect_events(SECTION_URL)
    report = build_report(events)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"Готово. Сохранено в {OUTPUT_FILE}, событий: {len(events)}")


if __name__ == "__main__":
    main()