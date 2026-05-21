#!/usr/bin/env python3
"""Генерация ASCII-README."""

import os
from datetime import datetime
from random import choice

import requests
from ascii_magic import AsciiArt
from pyfiglet import Figlet

FALLBACK_NAME = "ChillLich"

# случайно выбирает один изх них
# Можно добавить: "3-d",  "speed", "tinker-toy"
LIST_OF_FONTS = ["bulbhead", "lean", "larry3d", "standard", "doom"]
TEXT_WIDTH = 120  # максимальная ширина в символах для pyfiglet

# Размер аватарки
COLUMNS = 104  # в символах. 104 чтобы не скроллить горизонтально если добавлять как raw ascii
ADD_AVATAR = True  # Показывать ли аватар?
# False чтобы вывести аватарку как изображение <img> в README.md
# True чтобы вывести аватарку символами ascii, только для простых сильноконтрастных аватарок
AS_RAW_ASCII_README = False
# Если True то создает плейсхолдеры чтоб на сайте была не картинка а raw ascii
REPLACE_AVATAR = True
AS_IMAGE_WIDTH = 300  # ширина PNG не рекомендуется более 890

# Всё что в README.md между заданными плейсхолдерами ишнорируется при сборке html
IGNORE_START = "<!-- IGNORE_S -->"
IGNORE_END = "<!-- IGNORE_E -->"
# Заменяется на ascii art
REPLACE_AVATAR_PLACEHOLDER = "<!-- AVATAR_AS_RAW_ASCII -->"


def get_avatar_ascii(username: str, columns: int = 104) -> str:
    """Получить ASCII строку - аватарку GitHub, использует API"""
    request = requests.get(f"https://api.github.com/users/{username}")
    request.raise_for_status()
    avatar_url = request.json()["avatar_url"]

    art = AsciiArt.from_url(avatar_url)
    art.to_image_file("avatar_ascii.png", columns=columns)
    ascii = art.to_ascii(columns=columns)
    with open("ASCII_AVATAR.txt", "w", encoding="utf-8") as f:
        f.write(ascii)
    return ascii


def make_ascii(text: str, font: str = "standard", width: int = TEXT_WIDTH) -> str:
    """Генерация ASCII-арта с указанным шрифтом"""
    return Figlet(font=font, width=width).renderText(text).rstrip()


def main():
    username = os.getenv("GITHUB_REPOSITORY_OWNER", FALLBACK_NAME).upper()
    FONT = choice(LIST_OF_FONTS)
    NAME_FONT = FONT
    DATE_FONT = FONT

    name_ascii = make_ascii(username, NAME_FONT)
    date_ascii = make_ascii(datetime.now().strftime("%d.%m.%Y"), DATE_FONT)

    # output
    terminal_block = f">>> profile.name()\n{name_ascii}" "\n\n" f">>> date.today()\n{date_ascii}"

    if ADD_AVATAR:
        ascii_art_as_image = (
            f'<img src="avatar_ascii.png" width="{AS_IMAGE_WIDTH}" alt="ASCII Avatar" />'
        )
        avatar_ascii = get_avatar_ascii(username, COLUMNS)
        if AS_RAW_ASCII_README:
            terminal_block += "\n\n" + f">>> profile.avatar()\n\n{avatar_ascii}"
        else:
            terminal_block += "\n\n" + ">>> profile.avatar()"

    terminal_block = f"```\n{terminal_block}\n```"

    if ADD_AVATAR and not AS_RAW_ASCII_README:
        terminal_block += (
            "\n"
            + f"{IGNORE_START if REPLACE_AVATAR else ''}"
            + ascii_art_as_image
            + f"{IGNORE_END + REPLACE_AVATAR_PLACEHOLDER if REPLACE_AVATAR else ''}"
        )

    try:
        with open("template.md", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""

    readme_content = content.replace("<!-- TERMINAL_PLACEHOLDER -->", terminal_block)

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print(f"✅ README.md обновлён (шрифт: {FONT})")


if __name__ == "__main__":
    main()
