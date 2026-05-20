#!/usr/bin/env python3
"""Генерация ASCII-README."""

import os
from datetime import datetime
from random import choice

import requests
from ascii_magic import AsciiArt
from pyfiglet import Figlet

# случайно выбирает один изх них
# Можно добавить: "3-d", "lean", "speed"
LIST_OF_FONTS = ["bulbhead", "larry3d", "standard", "doom", "tinker-toy"]

# Размер аватарки
COLUMNS = 65


def get_avatar_ascii(username: str, columns: int = 65) -> str:
    """Получить ASCII строку - аватарку GitHub, использует API"""
    request = requests.get(f"https://api.github.com/users/{username}")
    request.raise_for_status()
    avatar_url = request.json()["avatar_url"]

    art = AsciiArt.from_url(avatar_url)
    return art.to_ascii(columns=columns)


def make_ascii(text: str, font: str = "standard") -> str:
    """Генерация ASCII-арта с указанным шрифтом"""
    return Figlet(font=font).renderText(text).rstrip()


def main():
    username = os.getenv("GITHUB_REPOSITORY_OWNER", "Octocat")
    FONT = choice(LIST_OF_FONTS)
    NAME_FONT = FONT
    DATE_FONT = FONT

    name_ascii = make_ascii(username, NAME_FONT)
    date_ascii = make_ascii(datetime.now().strftime("%d.%m.%Y"), DATE_FONT)
    avatar_ascii = get_avatar_ascii(username, COLUMNS)

    # output
    terminal_block = (
        f">>> profile.name()\n{name_ascii}"
        "\n\n"
        f">>> time.today()\n{date_ascii}"
        "\n\n"
        f">>> profile.avatar()\n{avatar_ascii}"
    )

    try:
        with open("template.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""

    readme_content = content.replace("<!-- TERMINAL_PLACEHOLDER -->", f"```\n{terminal_block}\n```")

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"✅ README.md обновлён (шрифт: {FONT})")


if __name__ == "__main__":
    main()
