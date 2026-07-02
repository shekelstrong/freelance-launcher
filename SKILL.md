---
name: freelance-launcher
description: Запуск фрилансера с нуля. Ресёрч ниши, генерация портфолио-демо (SaaS/Service/Ecommerce/Mobile), постинг в TenChat и VC.ru. Интеграция с kwork-gig-studio.
---

# Freelance Launcher

MCP-сервер для запуска фрилансера. От нуля до первого клиента за 7 дней.

## Когда использовать

- Юзер говорит «хочу начать фрилансить», «нужно портфолио», «с чего начать»
- Юзер просит исследовать нишу
- Нужно быстро собрать демо-сайт под клиента
- Нужны посты для TenChat или статьи для VC.ru

## 5 tools pipeline

```
цель → niche_research → generate_portfolio → create_kwork → post_tenchat/vc
                                              ↓
                                         (опубликовано)
```

## Алгоритм

### 1. niche_research
База по 5 нишам (ai, telegram, design, seo, data). Возвращает:
- demand / competition / avg_price_rub
- top_categories
- trends
- recommendations ("высокий спрос + низкая конкуренция = ОГОНЬ")

### 2. generate_portfolio
Создаёт готовое демо в указанной папке:
- `index.html` — лендинг с hero, фичами, тарифами, контактами
- `styles.css` — стили (3 цветовые схемы)
- `app.js` — smooth scroll + CTA tracking
- `README.md`

4 типа: saas / service / ecommerce / mobile-app.

### 3. create_kwork
Обёртка → редирект на kwork-gig-studio (там полная логика).

### 4. post_tenchat
Короткий пост (200-300 слов) + теги + лучшее время.

### 5. post_vc
Длинная статья (800-3000 слов) + подзаголовки + теги.

## Pitfalls

| Ошибка | Последствие | Как избежать |
|---|---|---|
| Без портфолио | HR не отвечает | Сначала generate_portfolio, потом kwork |
| Портфолио из чужих работ | Спалится на собесе | Только свои, с авторством |
| Постинг в одной сети | Узкий охват | TenChat + VC + Telegram = тройной |
| Пост без CTA | Низкий engagement | Всегда заканчивай вопросом/призывом |
| Одинаковый текст везде | Бан/спам | Адаптируй под каждую площадку |
| Демо без бэкенда | "А это работает?" | Wireframe + "готов к интеграции" |

## Стратегия 7 дней

- День 1-2: niche_research, выбор ниши
- День 3-4: 3-5 generate_portfolio (SaaS, service, ecommerce)
- День 5: create_kwork × 3-5 кворков
- День 6: post_tenchat + post_vc (3-5 постов)
- День 7: outreach по бирже + TenChat DM

## Связь с другими MCP

- **kwork-gig-studio** — создание кворков
- **hh-apply-suite** — если фриланс не пошёл, отклик на вакансии
- **telegram-suite** — для ботов в портфолио

## Источники

5 скиллов: freelance-portfolio-demo-sites, freelance-first-revenue, kwork-gig-creation, kwork-parallel-channels, affiliate-arbitrage-ops.
