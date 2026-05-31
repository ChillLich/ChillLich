```
>>> profile.name()
  ___  _   _  ____  __    __    __    ____  ___  _   _ 
 / __)( )_( )(_  _)(  )  (  )  (  )  (_  _)/ __)( )_( )
( (__  ) _ (  _)(_  )(__  )(__  )(__  _)(_( (__  ) _ ( 
 \___)(_) (_)(____)(____)(____)(____)(____)\___)(_) (_)

>>> date.today()
 ___  __    ___   ___    ___   ___  ___    _  
(__ )/  )  / _ \ | __)  (__ \ / _ \(__ \  / ) 
 (_ \ )(  ( (_) )|__ \   / _/( (_) )/ _/ / _ \
(___/(__)()\___/ (___/()(____)\___/(____)\___/

>>> profile.avatar()
```
<!-- IGNORE_S --><img src="avatar_ascii.png" width="300" alt="ASCII Avatar" /><!-- IGNORE_E --><!-- AVATAR_AS_RAW_ASCII -->

> [!TIP]
> 💡 *Обновляется автоматически. [Как это работает?](HOW_IT_WORKS.md)*

**[Профиль GitHub.](https://github.com/ChillLich)**

**[GitHub Pages website.](https://chilllich.github.io/ChillLich/)**

---

## Projects

| Проект | Описание | Сильная сторона / Key Feature | Стек технологий |
| :--- | :--- | :--- | :--- |
| **[Blog REST API](https://github.com/ChillLich/blog_api)** | Масштабируемый API социальной сети: посты, группы, подписки, комментарии. | **Безопасность:** JWT auth (access/refresh), строгая система прав доступа (RBAC), поддержка медиафайлов. | `Python`, `Django`, `DRF`, `SimpleJWT`, `OpenAPI` |
| **[Artwork Scoreboard API](https://github.com/ChillLich/api_artwork_scoreboard)** | Платформа отзывов и рейтингов произведений искусства (книги, фильмы, музыка). | **Ролевая модель:** Разграничение прав (User/Moderator/Admin), импорт данных из CSV, расчет агрегированных рейтингов. | `Python`, `Django`, `DRF`, `PyJWT`, `CSV Import` |
| **[QA & Testing Suite](https://github.com/ChillLich/Django-Testing)** | Демонстрация культуры тестирования: модульные и интеграционные тесты для Django-приложений. | **Надежность:** 100% покрытие критических путей, изоляция через моки/фикстуры, проверка граничных случаев и прав доступа. | `Python`, `pytest`, `unittest`, `pytest-django`, `CI/CD basics` |
| **[Diary Platform](https://github.com/ChillLich/blogdiary)** | Полноценный блог-сервис с классическим MVC, админкой и пользовательскими профилями. | **Архитектура:** Clean Code, DRY-принципы, миксины для переиспользования логики, оптимизация SQL-запросов (`select_related`). | `Python`, `Django`, `PostgreSQL`, `Bootstrap5`, `CBV` |
| **[Meteo&Tails Bot](https://github.com/ChillLich/Meteo-Tails-Bot)** | Telegram-бот с прогнозом погоды, авто-уведомлениями и развлекательным контентом. | **UX & Интеграции:** Учет часовых поясов (GeoNames), работа с внешними API (OpenWeather), гибкая конфигурация логирования. | `Python`, `Telegram API`, `OpenWeatherMap`, `GeoNames`, `.env config`, `Logging` |
| **[Pomodoro Timer](https://github.com/ChillLich/pomodoro-timer)** <br> <br>**[GitHub Pages проекта.](https://chilllich.github.io/pomodoro-timer/)** | Десктопное приложение для тайм-менеджмента по методу Помодоро с гибкой настройкой интервалов. | **Desktop Integration:** Управление системным медиаплеером, режим «всегда сверху», кастомные темы, авто-сохранение настроек. | `Python`, `Tkinter`, `pygame`, `keyboard`, `JSON config` |
| **[Kittygram CI/CD](https://github.com/ChillLich/kittygram_cicd)** | Full-stack платформа для фото питомцев с автоматическим деплоем и мониторингом. | **Production-ready DevOps:** полный CI/CD пайплайн (тесты → сборка → деплой на VPS), контейнеризация 4 сервисов, авто-уведомления, Nginx reverse proxy. | `Python`, `Django`, `DRF`, `React`, `PostgreSQL`, `Docker`, `Docker Compose`, `GitHub Actions`, `Nginx`, `CI/CD` |

---
