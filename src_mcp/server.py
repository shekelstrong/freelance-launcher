"""Freelance Launcher MCP Server."""

import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from src_mcp.tools import generate_portfolio, create_kwork, post_tenchat, post_vc, niche_research


app = Server("freelance-launcher")


@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="niche_research",
            description="Ресёрч ниши для фрилансера: спрос, конкуренция, средние цены, тренды.",
            inputSchema={
                "type": "object",
                "properties": {
                    "niche": {"type": "string"},
                    "platform": {"type": "string", "enum": ["kwork", "fl", "upwork", "all"]},
                },
                "required": ["niche"],
            },
        ),
        Tool(
            name="generate_portfolio",
            description="Генерация портфолио-демо (HTML+CSS+JS) под нишу.",
            inputSchema={
                "type": "object",
                "properties": {
                    "niche": {"type": "string"},
                    "demo_type": {"type": "string", "enum": ["saas", "service", "ecommerce", "mobile-app"]},
                    "color_scheme": {"type": "string", "default": "dark-saas"},
                    "output_dir": {"type": "string", "default": "./"},
                },
                "required": ["niche", "demo_type"],
            },
        ),
        Tool(
            name="create_kwork",
            description="Обёртка над kwork-gig-studio: создание кворка с правилами модерации.",
            inputSchema={
                "type": "object",
                "properties": {
                    "niche": {"type": "string"},
                    "price": {"type": "integer"},
                    "deadline_days": {"type": "integer"},
                },
                "required": ["niche", "price", "deadline_days"],
            },
        ),
        Tool(
            name="post_tenchat",
            description="Генерация поста для TenChat: цепляющий заголовок, тело поста, CTA.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string"},
                    "target_audience": {"type": "string"},
                    "cta": {"type": "string"},
                },
                "required": ["topic"],
            },
        ),
        Tool(
            name="post_vc",
            description="Генерация статьи для VC.ru: заголовок, подзаголовки, тело, теги.",
            inputSchema={
                "type": "object",
                "properties": {
                    "topic": {"type": "string"},
                    "angle": {"type": "string", "description": "Угол подачи (опыт / кейс / инструкция / аналитика)"},
                    "length": {"type": "string", "enum": ["short", "medium", "long"], "default": "medium"},
                },
                "required": ["topic"],
            },
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    import json
    tools_map = {
        "niche_research": niche_research,
        "generate_portfolio": generate_portfolio,
        "create_kwork": create_kwork,
        "post_tenchat": post_tenchat,
        "post_vc": post_vc,
    }
    try:
        result = await tools_map[name].run(**arguments)
        return [TextContent(type="text", text=json.dumps(result, ensure_ascii=False, indent=2))]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {type(e).__name__}: {e}")]


async def main():
    async with stdio_server() as (rs, ws):
        await app.run(rs, ws, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
