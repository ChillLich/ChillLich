# How It Works

Это Python-скрипт, который автоматически генерирует и обновляет GitHub README с ASCII-артом, а также собирает персональный сайт на GitHub Pages. При запуске он забирает данные профиля через GitHub API, преобразует имя в текстовый баннер (`pyfiglet`), а аватар - в ASCII-символы или PNG (`ascii_magic`), после чего подставляет результат в шаблоны. Работает в связке с GitHub Actions: обновляет профиль по расписанию, при пуше и вручную.

## Как это работает

### 1. Генерация README (`generate_readme.py`)

- Берёт имя пользователя из `GITHUB_REPOSITORY_OWNER` (или fallback)
- Случайно выбирает шрифт из `LIST_OF_FONTS`
- Генерирует:
  - **Имя** → `pyfiglet` ASCII-арт
  - **Дату** → `pyfiglet` ASCII-арт  
  - **Аватар** → `ascii_magic` (PNG + raw ASCII)
- Вставляет блок в `<!-- TERMINAL_PLACEHOLDER -->` файла `template.md`
- Сохраняет результат в `README.md`

### 2. Сборка сайта (`generate_site.py`)

- Читает `README.md` и удаляет блоки между `<!-- IGNORE_S -->` и `<!-- IGNORE_E -->`
- Конвертирует Markdown в HTML (с поддержкой таблиц и блоков кода)
- Заменяет относительные ссылки на абсолютные (`github.com` / `raw.githubusercontent.com`)
- Подставляет raw ASCII-аватар вместо PNG (если настроено)
- Вставляет результат в `index.template.html` по плейсхолдерам
- Сохраняет финальный сайт в `docs/index.html` для GitHub Pages

### 3. Деплой

Деплоит результат и документацию в ветку `main`.

Исходный код доступен в ветке `dev`.

## Конфигурация

Все настройки находятся в начале файлов и объяснены в коде комментариями:
`generate_readme.py`, `index.template.html`, `generate_site.py`
Эти файлы находятся в ветке `dev`.

## Система плейсхолдеров

### В `template.md` (для README)

```markdown
<!-- TERMINAL_PLACEHOLDER -->
```

Заменяется на сгенерированный терминальный блок с именем, датой и аватаром.

### В `template.md` (для сборки сайта)

```markdown
<!-- IGNORE_S -->
Этот блок будет удалён при сборке сайта.
Например, здесь может быть PNG-аватар, который на сайте заменится на raw ASCII.
<!-- IGNORE_E -->
```

```markdown
<!-- AVATAR_AS_RAW_ASCII -->

```

Добавляется и заменяется на `<pre>` блок с raw ASCII-аватаром при сборке сайта (если `REPLACE_AVATAR = True`) автоматически.
Используется автоматически и только при выборе определенной конфигурации.

### В `index.template.html` (для сайта)

```html
<title><!-- TITLE_PLACEHOLDER --> | Profile</title>
<a href="<!-- PROFILE_LINK_PLACEHOLDER -->">Profile</a>
<a href="<!-- REPO_LINK_PLACEHOLDER -->">Repo</a>
<!-- CONTENT_PLACEHOLDER -->
```

Эти плейсхолдеры автоматически заполняются данными из GitHub API:

- `TITLE_PLACEHOLDER` → имя пользователя
- `PROFILE_LINK_PLACEHOLDER` → ссылка на профиль GitHub
- `REPO_LINK_PLACEHOLDER` → ссылка на репозиторий
- `CONTENT_PLACEHOLDER` → отрендеренный Markdown из README

## Как скопировать к себе

1. Нажмите **Use this template** в GitHub. ВАЖНО - `Include all branches` обязательно включить!
2. Назовите репозиторий **строго своим ником** (например, `ChillLich/ChillLich`)
3. Настройте предпочтительные параметры в `scripts/generate_readme.py` в ветке `dev`.
4. Заполните `template.md` по вкусу.
5. Запустите workflow **Update Profile README** вручную (вкладка Actions) или дождитесь срабатывания по расписанию
6. Включите GitHub Pages в настройках репозитория: **Settings → Pages → Source: Deploy from a branch → Branch: main → Folder: /docs**

## GitHub Actions Workflow

Автоматизировано с помощью Actions

## Темы сайта

Сайт поддерживает две темы с сохранением выбора в `localStorage`:

- **💡 Светлая (BIOS)**: синий фон, серый текст, жесткая тень - стиль старых BIOS
- **🌙 Темная (Классический терминал)**: черный фон, красный текст - современный терминал

Переключатель находится в заголовке окна терминала рядом со ссылками на профиль и репозиторий.

## Зависимости

```txt
ascii_magic==2.7.5    # Конвертация изображений → ASCII / PNG
pyfiglet==1.0.4       # Генерация текстовых баннеров
requests==2.34.2      # HTTP-запросы к GitHub API
markdown==3.10.2      # Парсинг Markdown в HTML
```

## LICENSE

MIT, создано [ChillLich](https://github.com/ChillLich)
