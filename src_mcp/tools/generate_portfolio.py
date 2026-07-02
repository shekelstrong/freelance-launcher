"""generate_portfolio: генерация портфолио-демо сайта."""

import os
from pathlib import Path


# Шаблоны цветовых схем
SCHEMES = {
    "dark-saas": {"bg": "#0a0a0a", "fg": "#ffffff", "accent": "#7ee787", "secondary": "#79c0ff"},
    "light-clean": {"bg": "#ffffff", "fg": "#1a1a1a", "accent": "#2563eb", "secondary": "#0ea5e9"},
    "warm-soft": {"bg": "#faf7f2", "fg": "#2a1f1a", "accent": "#d97706", "secondary": "#92400e"},
}


async def run(niche: str, demo_type: str, color_scheme: str = "dark-saas", output_dir: str = "./") -> dict:
    """Генерирует портфолио-демо.

    Args:
        niche: Ниша клиента.
        demo_type: saas / service / ecommerce / mobile-app.
        color_scheme: dark-saas / light-clean / warm-soft.
        output_dir: Куда создать файлы.

    Returns:
        Словарь с путями к файлам.
    """
    colors = SCHEMES.get(color_scheme, SCHEMES["dark-saas"])
    base = Path(output_dir) / f"demo-{demo_type}-{niche.lower().replace(' ', '-')[:30]}"
    base.mkdir(parents=True, exist_ok=True)

    files = {}

    # index.html
    files["index.html"] = _gen_index_html(niche, demo_type, colors)
    (base / "index.html").write_text(files["index.html"])

    # styles.css
    files["styles.css"] = _gen_css(colors)
    (base / "styles.css").write_text(files["styles.css"])

    # app.js
    files["app.js"] = _gen_js()
    (base / "app.js").write_text(files["app.js"])

    # README
    files["README.md"] = _gen_readme(niche, demo_type, base.name)
    (base / "README.md").write_text(files["README.md"])

    return {
        "demo_type": demo_type,
        "niche": niche,
        "color_scheme": color_scheme,
        "output_dir": str(base),
        "files": list(files.keys()),
    }


def _gen_index_html(niche: str, demo_type: str, c: dict) -> str:
    title_map = {
        "saas": f"{niche.title()} — SaaS платформа",
        "service": f"{niche.title()} — профессиональные услуги",
        "ecommerce": f"{niche.title()} — интернет-магазин",
        "mobile-app": f"{niche.title()} — мобильное приложение",
    }
    title = title_map.get(demo_type, niche.title())

    cta_map = {
        "saas": "Попробовать бесплатно",
        "service": "Заказать услугу",
        "ecommerce": "В каталог",
        "mobile-app": "Скачать приложение",
    }
    cta = cta_map.get(demo_type, "Подробнее")

    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="hero">
        <nav>
            <div class="logo">{niche.title()}</div>
            <ul class="nav-links">
                <li><a href="#features">Возможности</a></li>
                <li><a href="#pricing">Тарифы</a></li>
                <li><a href="#contact">Контакты</a></li>
            </ul>
        </nav>
        <div class="hero-content">
            <h1>{title}</h1>
            <p class="subtitle">Современное решение для {niche}. Работает, проверено, нравится клиентам.</p>
            <div class="cta-group">
                <a href="#contact" class="btn-primary">{cta}</a>
                <a href="#features" class="btn-secondary">Подробнее</a>
            </div>
        </div>
    </header>

    <section id="features" class="features">
        <h2>Ключевые возможности</h2>
        <div class="features-grid">
            <div class="feature">
                <div class="feature-icon">⚡</div>
                <h3>Быстро</h3>
                <p>Работает моментально, без задержек</p>
            </div>
            <div class="feature">
                <div class="feature-icon">🔒</div>
                <h3>Безопасно</h3>
                <p>Все данные под защитой, шифрование end-to-end</p>
            </div>
            <div class="feature">
                <div class="feature-icon">📊</div>
                <h3>Аналитика</h3>
                <p>Метрики, графики, отчёты в один клик</p>
            </div>
        </div>
    </section>

    <section id="pricing" class="pricing">
        <h2>Тарифы</h2>
        <div class="pricing-grid">
            <div class="plan">
                <h3>Старт</h3>
                <div class="price">990 ₽<span>/мес</span></div>
                <ul>
                    <li>Базовые функции</li>
                    <li>До 1000 пользователей</li>
                    <li>Email-поддержка</li>
                </ul>
                <a href="#contact" class="btn-primary">Выбрать</a>
            </div>
            <div class="plan featured">
                <h3>Про</h3>
                <div class="price">4 990 ₽<span>/мес</span></div>
                <ul>
                    <li>Все функции</li>
                    <li>До 100k пользователей</li>
                    <li>Приоритетная поддержка</li>
                </ul>
                <a href="#contact" class="btn-primary">Выбрать</a>
            </div>
            <div class="plan">
                <h3>Бизнес</h3>
                <div class="price">14 990 ₽<span>/мес</span></div>
                <ul>
                    <li>Всё из Про</li>
                    <li>Безлимит</li>
                    <li>Выделенный менеджер</li>
                </ul>
                <a href="#contact" class="btn-primary">Выбрать</a>
            </div>
        </div>
    </section>

    <section id="contact" class="contact">
        <h2>Связаться</h2>
        <p>Telegram: <a href="https://t.me/nedopekin">@nedopekin</a></p>
        <p>Email: business.nedopekin@gmail.com</p>
    </section>

    <footer>
        <p>© 2026 {niche.title()}. Powered by freelance-launcher MCP.</p>
    </footer>

    <script src="app.js"></script>
</body>
</html>
"""


def _gen_css(c: dict) -> str:
    return f"""* {{ margin: 0; padding: 0; box-sizing: border-box; }}

body {{
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: {c['bg']};
    color: {c['fg']};
    line-height: 1.6;
}}

nav {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.5rem 2rem;
    max-width: 1200px;
    margin: 0 auto;
}}

.logo {{ font-size: 1.5rem; font-weight: 700; color: {c['accent']}; }}

.nav-links {{ display: flex; list-style: none; gap: 2rem; }}
.nav-links a {{ color: {c['fg']}; text-decoration: none; opacity: 0.8; transition: opacity 0.2s; }}
.nav-links a:hover {{ opacity: 1; color: {c['accent']}; }}

.hero {{
    padding: 4rem 2rem;
    text-align: center;
}}

.hero-content {{ max-width: 800px; margin: 0 auto; }}

h1 {{ font-size: 3rem; margin-bottom: 1rem; line-height: 1.2; }}

.subtitle {{
    font-size: 1.25rem;
    opacity: 0.7;
    margin-bottom: 2rem;
}}

.cta-group {{ display: flex; gap: 1rem; justify-content: center; }}

.btn-primary, .btn-secondary {{
    padding: 0.875rem 2rem;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.2s;
    display: inline-block;
}}

.btn-primary {{
    background: {c['accent']};
    color: {c['bg']};
}}

.btn-primary:hover {{ transform: translateY(-2px); box-shadow: 0 8px 20px {c['accent']}40; }}

.btn-secondary {{
    background: transparent;
    color: {c['fg']};
    border: 1px solid {c['fg']}30;
}}

section {{ padding: 4rem 2rem; max-width: 1200px; margin: 0 auto; }}
h2 {{ font-size: 2.5rem; margin-bottom: 2rem; text-align: center; }}

.features-grid, .pricing-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
}}

.feature, .plan {{
    background: {c['fg']}05;
    border: 1px solid {c['fg']}10;
    border-radius: 12px;
    padding: 2rem;
    text-align: center;
}}

.feature-icon {{ font-size: 3rem; margin-bottom: 1rem; }}

.plan.featured {{
    background: {c['accent']}10;
    border-color: {c['accent']};
    transform: scale(1.05);
}}

.price {{
    font-size: 2.5rem;
    font-weight: 700;
    color: {c['accent']};
    margin: 1rem 0;
}}

.price span {{ font-size: 1rem; opacity: 0.7; }}

.plan ul {{ list-style: none; margin: 1.5rem 0; }}
.plan li {{ padding: 0.5rem 0; opacity: 0.8; }}

.contact {{ text-align: center; }}
.contact a {{ color: {c['accent']}; text-decoration: none; }}

footer {{
    padding: 2rem;
    text-align: center;
    opacity: 0.5;
    border-top: 1px solid {c['fg']}10;
}}

@media (max-width: 768px) {{
    h1 {{ font-size: 2rem; }}
    .nav-links {{ display: none; }}
    .cta-group {{ flex-direction: column; }}
}}
"""


def _gen_js() -> str:
    return """// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
        e.preventDefault();
        const target = document.querySelector(a.getAttribute('href'));
        if (target) target.scrollIntoView({ behavior: 'smooth' });
    });
});

// CTA click tracking
document.querySelectorAll('.btn-primary').forEach(btn => {
    btn.addEventListener('click', () => {
        console.log('CTA clicked:', btn.textContent);
    });
});
"""


def _gen_readme(niche: str, demo_type: str, name: str) -> str:
    return f"""# {niche.title()} — {demo_type} Demo

Демо-сайт портфолио. Сгенерировано через [freelance-launcher](https://github.com/shekelstrong/freelance-launcher) MCP.

## Запуск

```bash
open index.html  # или открой в браузере
```

Или залей на Vercel/Layero:
```bash
npx vercel --prod
```

## Структура

- `index.html` — лендинг
- `styles.css` — стили (тёмная SaaS-тема по умолчанию)
- `app.js` — smooth scroll + CTA tracking
- `README.md` — этот файл
"""
