# freelance-launcher

> MCP-сервер: запуск фрилансера с нуля. Портфолио + кворки + постинг в TenChat / VC.ru.

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org)
[![MCP](https://img.shields.io/badge/MCP-compatible-purple.svg)](https://modelcontextprotocol.io)

## 🎯 Что это

MCP-сервер с 5 инструментами для запуска фрилансера:

- 🔍 **niche_research** — ресёрч ниши (спрос, конкуренция, цены, тренды)
- 🎨 **generate_portfolio** — генерация портфолио-демо (SaaS/Service/Ecommerce/Mobile)
- 🛍 **create_kwork** — обёртка над kwork-gig-studio
- 📝 **post_tenchat** — генерация постов для TenChat
- 📰 **post_vc** — генерация статей для VC.ru

## 📦 Установка

```bash
git clone https://github.com/shekelstrong/freelance-launcher.git
cd freelance-launcher
pip install -r requirements.txt
```

## 🛠 MCP Tools

### niche_research
```python
result = await niche_research.run("ai", platform="kwork")
# → {demand: "high", competition: "medium", avg_price_rub: 5000, recommendations: [...]}
```

5 ниш в базе: ai, telegram, design, seo, data.

### generate_portfolio
```python
result = await generate_portfolio.run(
    niche="CRM для малого бизнеса",
    demo_type="saas",
    color_scheme="dark-saas",
    output_dir="./portfolio"
)
# Создаст: index.html, styles.css, app.js, README.md
```

4 типа демо:
- `saas` — SaaS-лендинг
- `service` — услуги
- `ecommerce` — магазин
- `mobile-app` — мобильное приложение

3 цветовые схемы:
- `dark-saas` (по умолчанию)
- `light-clean`
- `warm-soft`

### create_kwork
Обёртка, которая ссылается на [kwork-gig-studio](https://github.com/shekelstrong/kwork-gig-studio).

### post_tenchat
```python
result = await post_tenchat.run(
    topic="запустить SaaS",
    target_audience="инди-фаундеры",
    cta="пиши в комментах"
)
# → {title, body, tags, best_posting_time}
```

### post_vc
```python
result = await post_vc.run(
    topic="AI-агенты для автоматизации",
    angle="кейс",
    length="long"
)
# → {title, subtitles, body, tags, word_count_target}
```

## 📁 Структура

```
freelance-launcher/
├── README.md
├── LICENSE
├── SKILL.md
├── requirements.txt
├── src_mcp/
│   ├── server.py
│   └── tools/
│       ├── niche_research.py
│       ├── generate_portfolio.py
│       ├── create_kwork.py
│       ├── post_tenchat.py
│       └── post_vc.py
└── .github/workflows/ci.yml
```

## 📄 License

MIT © Vasiliy Nedopekin (shekelstrong)
