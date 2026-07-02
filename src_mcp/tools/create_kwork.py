"""create_kwork: обёртка над kwork-gig-studio."""


async def run(niche: str, price: int, deadline_days: int) -> dict:
    """Создание кворка.

    Args:
        niche: Ниша.
        price: Цена в рублях.
        deadline_days: Срок.

    Returns:
        Словарь с черновиком (заглушка).
    """
    return {
        "tool": "create_kwork",
        "note": "Этот tool — обёртка. Реальная логика в kwork-gig-studio MCP.",
        "redirect_to": "https://github.com/shekelstrong/kwork-gig-studio",
        "params": {"niche": niche, "price": price, "deadline_days": deadline_days},
    }
