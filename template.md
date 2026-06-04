<!-- TERMINAL_PLACEHOLDER -->

> [!TIP]
> 💡 *Обновляется автоматически. [Как это работает?](HOW_IT_WORKS.md)*

**[Профиль GitHub.](https://github.com/ChillLich)**

**[GitHub Pages website.](https://chilllich.github.io/ChillLich/)**

---

## Projects

| Проект | Описание (Что сделали) | Ключевое достижение / Результат | Стек технологий |
| :--- | :--- | :--- | :--- |
| **[Blog REST API](https://github.com/ChillLich/blog_api)** | **Спроектировал REST API** социальной сети с полным CRUD для постов, групп и подписок. Реализовал систему комментариев и работу с медиафайлами. | **Обеспечил безопасность и производительность:** JWT-аутентификация с refresh-токенами, оптимизированные Many-to-Many связи, строгая ролевая модель (RBAC). | `Python`, `Django`, `DRF`, `SimpleJWT`, `OpenAPI` |
| **[Artwork Scoreboard API](https://github.com/ChillLich/api_artwork_scoreboard)** | **Разработал бэкенд платформы** для агрегации оценок произведений искусства. Реализовал алгоритмы расчета рейтингов и механизм массового импорта данных. | **Автоматизировал обработку данных:** Алгоритмы расчета агрегированных рейтингов, оптимизированный импорт из CSV, гибкая ролевая модель (User/Moderator/Admin). | `Python`, `Django`, `DRF`, `PyJWT`, `CSV Import`, `pytest` |
| **[QA & Testing](https://github.com/ChillLich/Django-testing)** | **Покрыл критические бизнес-сценарии** комплексом тестов для двух проектов (News/Comments и Notes). Реализовал тестирование маршрутов, контента и бизнес-логики. | **Достиг высокого покрытия тестами:** Тесты CRUD-операций, модерации, пагинации, уникальности slug. Использование моков и фикстур для изоляции окружения. | `Python`, `pytest`, `unittest`, `pytest-django` |
| **[Diary Platform](https://github.com/ChillLich/diary)** | **Разработал блог-платформу** с системой публикаций, категорий и комментариев. Реализовал отложенные посты и кастомные страницы ошибок (403, 404, 500). | **Оптимизировал производительность БД:** Миксины (`ListPostsMixin`, `PostOwnerCheckMixin`), сокращение SQL-запросов через `select_related` и `annotate`, разделение прав. | `Python`, `Django`, `PostgreSQL`, `Bootstrap5`, `pytest` |
| **[Meteo&Tails Bot](https://github.com/ChillLich/Meteo-Tails-Bot)** | **Реализовал Telegram-бота** с персонализированными уведомлениями о погоде. Настроил интеграцию с внешними API и учет часовых поясов пользователей. | **Обеспечил персонализацию UX:** Интеграция с OpenWeatherMap API, автоматический учет геолокации через GeoNames, гибкое логирование, конфигурация через `.env`. | `Python`, `Telegram API`, `OpenWeatherMap`, `GeoNames`, `APScheduler` |
| **[Pomodoro Timer](https://github.com/ChillLich/pomodoro-timer)** <br> <br>**[GitHub Pages](https://chilllich.github.io/pomodoro-timer/)** | **Создал десктопное приложение** для тайм-менеджмента с автоматической настройкой окружения. Реализовал глубокую интеграцию с ОС через управление медиаплеером. | **Достиг глубокой интеграции с ОС:** Отправка media-key событий (Play/Pause) через `keyboard`, режим «всегда сверху», автосохранение настроек в JSON, пресеты таймера. | `Python`, `Tkinter`, `pygame`, `keyboard`, `JSON` |
| **[Kittygram CI/CD](https://github.com/ChillLich/kittygram_cicd)** | **Выстроил production-ready CI/CD** для full-stack приложения. Автоматизировал полный цикл: линтинг → тесты → сборка образов → SSH-деплой на VPS. | **Автоматизировал деплой на 100%:** Пайплайн GitHub Actions с уведомлениями в Telegram, контейнеризация 4 сервисов, персистентное хранение данных, zero-downtime обновления. | `Docker`, `Docker Compose`, `GitHub Actions`, `Nginx`, `CI/CD`, `Django`, `PostgreSQL` |

---
