#!/usr/bin/env python3
"""Сборка сайта: README.md -> index.html (с игнорированием блоков)"""

import html
import os
import re
import shutil
from pathlib import Path

import markdown
from generate_readme import REPLACE_AVATAR_PLACEHOLDER

README_FILE = Path("README.md")
TEMPLATE_HTML = "index.template.html"
# OUTPUT_DIR папка для вывода. но еще этому скрипту после работы
# scripts\generate_readme.py нужны некоторые файлы отсюда
OUTPUT_DIR = Path("dist")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
DOC_PATH = Path("HOW_IT_WORKS.md")

# Всё что в README.md между заданными плейсхолдерами ишнорируется при сборке html
IGNORE_START = "<!-- IGNORE_S -->"
IGNORE_END = "<!-- IGNORE_E -->"

# по нему вставляется результат. обязательно должен присутствовать в TEMPLATE_HTML файле
CONTENT_PLACEHOLDER = "<!-- CONTENT_PLACEHOLDER -->"

# Плейсхолдеры для динамических данных в TEMPLATE_HTML файле, тоже должны присутствовать
TITLE_PLACEHOLDER = "<!-- TITLE_PLACEHOLDER -->"
PROFILE_LINK_PLACEHOLDER = "<!-- PROFILE_LINK_PLACEHOLDER -->"
REPO_LINK_PLACEHOLDER = "<!-- REPO_LINK_PLACEHOLDER -->"

FAVICON_PLACEHOLDER = "<!-- FAVICON_PLACEHOLDER -->"

FALLBACK_USERNAME = "ChillLich"
USERNAME = os.getenv("GITHUB_REPOSITORY_OWNER", FALLBACK_USERNAME)
FALLBACK_REPO_URL = "ChillLich/ChillLich"
USER_REPO = os.getenv("GITHUB_REPOSITORY", FALLBACK_REPO_URL)
BASE_GITHUB_URL = f"https://github.com/{USER_REPO}/blob/main/"
RAW_GITHUB_URL = f"https://raw.githubusercontent.com/{USER_REPO}/main/"
PROFILE_URL = f"https://github.com/{USERNAME}"
REPO_URL = f"https://github.com/{USER_REPO}/"

FAVICON_URL = f"{RAW_GITHUB_URL}avatar_ascii.png"


def load_text(path: str | Path) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def save_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def clean_markdown(content: str) -> str:
    """Удаляет всё между IGNORE_S и IGNORE_E (включая сами маркеры)"""
    # non-greedy match (.*?), чтобы удалять каждый блок отдельно, если их много
    pattern = re.compile(re.escape(IGNORE_START) + r".*?" + re.escape(IGNORE_END), re.DOTALL)
    return pattern.sub("", content)


def fix_relative_links(html_content: str) -> str:
    """Превращает относительные ссылки в абсолютные, не трогая уже существующие глобальные"""

    def replace(match):
        attr = match.group(1)  # "href" или "src"
        url = match.group(2)  # значение атрибута | исходная относительная ссылка

        # пропустить уже абсолютные ссылки. ВАЖНО! может быть надо дополнить
        if url.startswith(("http://", "https://", "//", "data:", "#", "mailto:")):
            return match.group(0)  # группа 0 - полное исходное вхождение

        if url.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")):
            new_url = f"{RAW_GITHUB_URL}{url}"
        else:
            new_url = f"{BASE_GITHUB_URL}{url}"

        return f'{attr}="{new_url}"'

    # Ловим и href="..." и src="...", в группу 2 извлекаем атрибут не выходя за кавычку "
    pattern = r'(href|src)="([^"]*)"'
    return re.sub(pattern, replace, html_content)


def get_raw_ascii():
    try:
        with open(OUTPUT_DIR / "ASCII_AVATAR.txt", "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        content = ""

    content = html.escape(content)
    return content


def main():
    print("Building site...")

    readme_raw = load_text(OUTPUT_DIR / README_FILE)
    html_template = load_text(TEMPLATE_HTML)

    readme_clean = clean_markdown(readme_raw)
    # extensions=['tables', 'fenced_code'] включают поддержку таблиц и блоков кода ```
    readme_html = markdown.markdown(readme_clean, extensions=["tables", "fenced_code"])
    readme_html = fix_relative_links(readme_html)

    ascii_avatar = f'<pre class="ascii-avatar">\n{get_raw_ascii()}\n</pre>'

    final_html = html_template
    final_html = final_html.replace(CONTENT_PLACEHOLDER, readme_html)
    final_html = final_html.replace(REPLACE_AVATAR_PLACEHOLDER, ascii_avatar)
    final_html = final_html.replace(TITLE_PLACEHOLDER, USERNAME)
    final_html = final_html.replace(PROFILE_LINK_PLACEHOLDER, PROFILE_URL)
    final_html = final_html.replace(REPO_LINK_PLACEHOLDER, REPO_URL)
    final_html = final_html.replace(FAVICON_PLACEHOLDER, FAVICON_URL)

    output_file = OUTPUT_DIR / "docs" / "index.html"
    save_text(output_file, final_html)

    # т.к. ветка теперь dev пусть дока обновляется/складывается в main для доступности
    if DOC_PATH.exists():
        shutil.copy(DOC_PATH, OUTPUT_DIR / DOC_PATH)
        print(f"Copied {DOC_PATH}")
    else:
        raise FileNotFoundError(f"Critical file {DOC_PATH} not found in dev branch!")

    github_src = Path(".github")
    github_dst = OUTPUT_DIR / ".github"
    if github_src.exists() and github_src.is_dir():
        if github_dst.exists():
            # полностью обновляем удаляя старое если есть (хоть на раннере не и будет)
            shutil.rmtree(github_dst)
        shutil.copytree(github_src, github_dst)
        print(f"Copied {github_src}")
    else:
        raise FileNotFoundError(f"Critical directory {github_src} not found in dev branch!")

    print(f"✅ Site built for {USERNAME} successfully: {output_file}")


if __name__ == "__main__":
    main()
