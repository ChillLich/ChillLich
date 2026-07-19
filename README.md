```
>>> profile.name()
  ____ _   _ ___ _     _     _     ___ ____ _   _ 
 / ___| | | |_ _| |   | |   | |   |_ _/ ___| | | |
| |   | |_| || || |   | |   | |    | | |   | |_| |
| |___|  _  || || |___| |___| |___ | | |___|  _  |
 \____|_| |_|___|_____|_____|_____|___\____|_| |_|

>>> date.today()
 ____   ___   ___ _____ ____   ___ ____   __   
|___ \ / _ \ / _ \___  |___ \ / _ \___ \ / /_  
  __) | | | | | | | / /  __) | | | |__) | '_ \ 
 / __/| |_| | |_| |/ /_ / __/| |_| / __/| (_) |
|_____|\___(_)___//_/(_)_____|\___/_____|\___/

>>> profile.avatar()
```
<!-- IGNORE_S --><img src="avatar_ascii.png" width="300" alt="ASCII Avatar" /><!-- IGNORE_E --><!-- AVATAR_AS_RAW_ASCII -->

> [!TIP]
> 💡 *Обновляется автоматически. [Как это работает?](HOW_IT_WORKS.md)*

**[Профиль GitHub.](https://github.com/ChillLich)**

**[GitHub Pages website.](https://chilllich.github.io/ChillLich/)**

---

## Проекты

| Проект | Описание | Ключевое достижение / Результат | Стек технологий |
| :--- | :--- | :--- | :--- |
| **[Blog REST API](https://github.com/ChillLich/blog_api)** | **Спроектировал REST API** социальной сети с полным CRUD для постов, групп и подписок. Реализовал систему комментариев и работу с медиафайлами. | **Обеспечил безопасность и целостность данных:** настроил [объектные права](https://github.com/ChillLich/blog_api/blob/main/blog_api/api/views.py) доступа (Object-level permissions) для 4 моделей, реализовал безопасную загрузку медиафайлов и JWT-аутентификацию с ротацией refresh-токенов. Оптимизировал сложные связи Many-to-Many (подписки, группы). Реализовал пагинацию и OpenAPI-документацию. | `Python`, `Django`, `DRF`, `SQL`, `SimpleJWT`, `OpenAPI` |
| **[Artwork Scoreboard API](https://github.com/ChillLich/api_artwork_scoreboard)** | **Разработал бэкенд платформы** для агрегации оценок произведений искусства. Реализовал алгоритмы расчета рейтингов и механизм массового импорта данных. | **Реализовал production-ready API:** кастомная passwordless-аутентификация через email с `TimestampSigner` ([views.py](https://github.com/ChillLich/api_artwork_scoreboard/blob/main/api_artwork_scoreboard/api/views.py)), трёхуровневая система permissions ([permissions.py](https://github.com/ChillLich/api_artwork_scoreboard/blob/main/api_artwork_scoreboard/api/permissions.py)), разделение Read/Write сериализаторов, динамический расчет рейтингов через `annotate` и продвинутая фильтрация по связанным моделям (`genre__slug`). Массовый импорт CSV через management-команду. | `Python`, `Django`, `DRF`, `SQL`, `pytest` |
| **[QA & Testing](https://github.com/ChillLich/Django-testing)** | **Покрыл критические бизнес-сценарии** комплексом тестов для двух проектов. Реализовал тестирование маршрутов, контента и бизнес-логики. | **38+ тестов** ([pytest: 23](https://github.com/ChillLich/Django-testing/tree/main/PyTest-Project/news/tests), [unittest: 16](https://github.com/ChillLich/Django-testing/tree/main/UnitTest-Project/notes/tests)) с 100% покрытием ключевых endpoints. Тесты CRUD, модерации, пагинации, уникальности slug. Моки и фикстуры для изоляции. | `Python`, `pytest`, `pytest-django`, `unittest`, `CI/CD` |
| **[Diary Platform](https://github.com/ChillLich/diary)** | **Разработал блог-платформу** с системой публикаций, категорий и комментариев. Реализовал отложенные посты и кастомные страницы ошибок. | **3 приложения** ([blog](https://github.com/ChillLich/diary/tree/main/blogdiary/blog), [pages](https://github.com/ChillLich/diary/tree/main/blogdiary/pages), [core](https://github.com/ChillLich/diary/tree/main/blogdiary/core)), [3 кастомных миксина](https://github.com/ChillLich/diary/blob/main/blogdiary/blog/views.py) (`ListPostsMixin`, `PostOwnerCheckMixin`, `CommentMixin`), оптимизация через `select_related`/`annotate`,  планирование публикаций (publish_at), кастомные ошибки (403, 404, 500). | `Python`, `Django`, `SQL`, `Bootstrap 5`, `pytest` |
| **[Meteo&Tails Bot](https://github.com/ChillLich/Meteo-Tails-Bot)** | **Реализовал Telegram-бота** с персонализированными уведомлениями о погоде. Настроил интеграцию с внешними API и учет часовых поясов. | **8 [команд](https://github.com/ChillLich/Meteo-Tails-Bot/blob/main/main.py#L41)** (/today, /town, /time, /toggle), автоматическое определение часового пояса через GeoNames, учет летнего времени (DST), 3 канала логирования (Telegram, файл, консоль). | `Python`, `python-telegram-bot`, `APScheduler`, `Requests` |
| **[Pomodoro Timer](https://github.com/ChillLich/pomodoro-timer)** <br> <br>**[GitHub Pages](https://chilllich.github.io/pomodoro-timer/)** | **Создал десктопное приложение** для тайм-менеджмента. Реализовал глубокую интеграцию с ОС через управление системным медиаплеером. | **4 готовых [пресета](https://github.com/ChillLich/pomodoro-timer/blob/main/TIMER.py#L74) таймера** и гибкая конфигурация кастомного, 4 [фазы](https://github.com/ChillLich/pomodoro-timer/blob/main/TIMER.py#L7) (Focus, short rest, long rest, pause), отправка media-key системных событий, 7+ тем интерфейса и полная кастомизация пользовательских, автосохранение в JSON [config.py](https://github.com/ChillLich/pomodoro-timer/blob/main/config.py). | `Python`, `Tkinter`, `Pygame`, `Keyboard` |
| **[Kittygram CI/CD](https://github.com/ChillLich/kittygram_cicd)** | **Реализовал контейнеризацию и оркестрацию** существующего full-stack приложения: написал Dockerfile для каждого сервиса, сконфигурировал Django/Nginx/PostgreSQL и связал их в единую мультиконтейнерную инфраструктуру с автоматическим деплоем. | **Выстроил production-ready инфраструктуру:** 4 сервиса ([docker-compose.yml](https://github.com/ChillLich/kittygram_cicd/blob/main/docker-compose.yml)), 3 persistent volume, **5 этапов пайплайна** ([.github/workflows](https://github.com/ChillLich/kittygram_cicd/tree/main/.github/workflows)): lint → test → build → SSH-deploy → Telegram-notify. Настроил Nginx reverse proxy и персистентное хранение данных. | `Docker`, `Docker Compose`, `GitHub Actions`, `Nginx`, `CI/CD`, `SSH` |

---
