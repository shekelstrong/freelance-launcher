"""niche_research: ресёрч ниши для фрилансера."""


# Примерные данные по популярным нишам (обновляются вручную)
NICHE_DATA = {
    "ai": {
        "demand": "high",
        "competition": "medium",
        "avg_price_rub": 5000,
        "top_categories": ["AI-аудит", "Боты с LLM", "RAG-системы", "AI-агенты"],
        "trends": "Растёт на 30% в год, главный драйвер — массовый запуск LLM-приложений",
        "competitors_top": [
            {"name": "AI-интеграторы", "count": 50, "rating": "4.7"},
            {"name": "Ботмейкеры", "count": 200, "rating": "4.5"},
        ],
    },
    "telegram": {
        "demand": "high",
        "competition": "high",
        "avg_price_rub": 3000,
        "top_categories": ["Telegram-боты", "Mini Apps", "Каталоги ботов"],
        "trends": "Стабильный рост 20% в год, монетизация через Stars",
        "competitors_top": [
            {"name": "Telegram-разработчики", "count": 500, "rating": "4.6"},
        ],
    },
    "design": {
        "demand": "medium",
        "competition": "high",
        "avg_price_rub": 2500,
        "top_categories": ["Лендинги", "UX-аудит", "Figma-шаблоны"],
        "trends": "Спрос стабилен, конкуренция растёт",
    },
    "seo": {
        "demand": "medium",
        "competition": "medium",
        "avg_price_rub": 4000,
        "top_categories": ["SEO-аудит", "Семантика", "Технический SEO"],
        "trends": "AI-SEO набирает обороты",
    },
    "data": {
        "demand": "high",
        "competition": "low",
        "avg_price_rub": 6000,
        "top_categories": ["Парсинг", "Аналитика", "Дашборды"],
        "trends": "Растёт спрос на data-engineering",
    },
}


async def run(niche: str, platform: str = "kwork") -> dict:
    """Ресёрч ниши.

    Args:
        niche: Ниша (ai / telegram / design / seo / data / custom).
        platform: Платформа для анализа.

    Returns:
        Словарь со статистикой по нише.
    """
    niche_key = niche.lower()
    data = NICHE_DATA.get(niche_key, {
        "demand": "unknown",
        "competition": "unknown",
        "avg_price_rub": 3000,
        "top_categories": [niche],
        "trends": "Нет данных, проведи ручной ресёрч",
    })

    return {
        "niche": niche,
        "platform": platform,
        **data,
        "recommendations": _build_recommendations(data),
    }


def _build_recommendations(data: dict) -> list:
    recs = []
    if data["demand"] == "high" and data["competition"] == "low":
        recs.append("ОГОНЬ: высокий спрос, низкая конкуренция — входи быстро")
    elif data["demand"] == "high" and data["competition"] == "high":
        recs.append("Высокая конкуренция: нужна узкая ниша + сильное портфолио")
    elif data["demand"] == "medium" and data["competition"] == "low":
        recs.append("Стабильная ниша: ищи своего клиента через каналы")
    else:
        recs.append("Средняя ниша: расширяй стек или меняй на смежную")

    if data["avg_price_rub"] >= 5000:
        recs.append("Средний чек высокий — фокус на качестве и кейсах")

    return recs
