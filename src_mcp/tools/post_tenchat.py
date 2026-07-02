"""post_tenchat: генерация поста для TenChat."""


async def run(topic: str, target_audience: str = "", cta: str = "") -> dict:
    """Генерирует пост для TenChat.

    Args:
        topic: Тема поста.
        target_audience: Целевая аудитория.
        cta: Призыв к действию.

    Returns:
        Словарь с заголовком и телом.
    """
    title = f"Как {topic} и не сойти с ума"

    body = f"""Недавно столкнулся с задачей: {topic}.

{('Для кого: ' + target_audience) if target_audience else ''}

Что я понял:

1. Это проще чем кажется
2. Главное — не пытаться сделать всё сразу
3. Доверять процессу

{('Что дальше: ' + cta) if cta else 'Если интересно — расскажу подробнее в комментариях.'}

#тенчат #{topic.replace(' ', '')}"""

    return {
        "title": title,
        "body": body,
        "tags": ["тенчат", topic.replace(' ', '').lower()],
        "best_posting_time": "9:00-11:00 или 18:00-20:00 МСК",
    }
