# 🎯 BIO - Портфолио Roman Karadev

Современное веб-приложение портфолио, созданное с использованием Django и HTMX. Динамичный интерфейс с AJAX функциональностью!

## 🚀 Особенности

- **📱 Адаптивный дизайн** - Отлично работает на всех устройствах
- **⚡ HTMX интеграция** - AJAX поиск проектов без перезагрузки страницы
- **🎨 Современный UI** - Темный дизайн с градиентами и анимациями
- **🔍 Живой поиск проектов** - Быстрый AJAX поиск с мгновенными результатами
- **📊 Музыкальная статистика** - Интерактивные карточки артистов
- **🛠 Админ-панель** - Удобное управление контентом
- **📝 Управляющие команды** - Автоматизация задач

## 🛠 Технологии

### Backend
- **Python 3.8+**
- **Django 4.2+** - Основной веб-фреймворк
- **SQLite** - База данных для разработки
- **Django Admin** - Управление контентом

### Frontend
- **HTML5** - Семантическая разметка
- **CSS3** - Современные стили с Grid и Flexbox
- **HTMX** - AJAX функциональность без написания JavaScript
- **JavaScript** - Интерактивность и анимации
- **Font Awesome** - Иконки
- **Google Fonts** - Типографика (Inter)

### Дополнительно
- **Адаптивный дизайн** - Mobile-first подход
- **Темная тема** - Современный внешний вид
- **SEO-оптимизация** - Правильная структура HTML

## 📋 Структура проекта

```
bio/
├── bio/                    # Основные настройки Django
│   ├── settings.py         # Конфигурация проекта
│   ├── urls.py            # Главный URL-роутинг
│   └── wsgi.py            # WSGI конфигурация
├── cabinet/               # Основное приложение
│   ├── models.py          # Модели данных
│   ├── views.py           # Представления
│   ├── admin.py           # Админ-панель
│   ├── management/        # Управляющие команды
│   ├── migrations/        # Миграции БД
│   └── templates/         # HTML шаблоны
│       ├── base.html      # Базовый шаблон
│       ├── home.html      # Главная страница
│       ├── about.html     # О разработчике
│       ├── skills.html    # Навыки
│       ├── projects.html  # Проекты
│       ├── contacts.html  # Контакты
│       └── fragments/     # Фрагменты шаблонов
├── static/               # Статические файлы
│   ├── css/
│   │   └── style.css     # Основные стили
│   ├── js/
│   │   └── script.js     # JavaScript функции
│   └── img/              # Изображения
├── media/                # Медиа файлы
│   ├── avatars/          # Аватарки
│   └── music/            # Музыкальные файлы
└── manage.py             # Django CLI
```

## 🚀 Установка и запуск

### Предварительные требования
- Python 3.8+
- pip (менеджер пакетов Python)
- Git

### 1. Клонирование репозитория
```bash
git clone https://github.com/yourusername/bio.git
cd bio
```

### 2. Создание виртуального окружения
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install django
# Или если есть requirements.txt:
# pip install -r requirements.txt
```

### 4. Применение миграций
```bash
python manage.py migrate
```

### 5. Создание суперпользователя
```bash
python manage.py createsuperuser
```

### 6. Запуск сервера разработки
```bash
python manage.py runserver
```

Откройте браузер и перейдите на `http://127.0.0.1:8000/`

## 📖 Использование

### Админ-панель
- Перейдите на `/admin/`
- Войдите под учетными данными суперпользователя
- Управляйте проектами, ссылками, музыкой и другим контентом


### Структура приложения
- **`/`** - Главная страница с обзором
- **`/about/`** - О разработчике и музыкальные предпочтения
- **`/skills/`** - Технические навыки и опыт
- **`/projects/`** - Портфолио проектов с поиском
- **`/contacts/`** - Контактная информация
- **`/project/<id>/`** - Детальная страница проекта

## 🎨 Особенности дизайна

### Цветовая схема
- **Фон**: Темные градиенты (#0a0a0a, #1a1a2e, #16213e)
- **Акцент**: Зеленый градиент (#00ff88, #0099ff)
- **Текст**: Белый с различной прозрачностью

### Типографика
- **Основной шрифт**: Inter
- **Заголовки**: 700-800 вес
- **Основной текст**: 400-500 вес

### Анимации
- Плавные переходы (0.3s ease)
- Hover эффекты
- Пульсация для аватара
- Анимированный заголовок страницы

## 🔧 Настройка

### Основные настройки в `settings.py`
```python
# Статические файлы
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Медиа файлы
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Модели данных
- **User** - Пользователь (профиль)
- **Project** - Проекты портфолио
- **Music** - Музыкальные предпочтения
- **Bio** - Биографическая информация
- **Link** - Ссылки на проекты
- **Icon** - Иконки для проектов

## 📱 Адаптивность

Проект полностью адаптивен и тестирован на:
- 📱 Мобильных устройствах (320px+)
- 📱 Планшетах (768px+)
- 🖥 Десктопах (1024px+)

### Мобильные особенности
- Hamburger меню
- Адаптивная типографика
- Оптимизированные изображения
- Touch-friendly интерфейс

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте feature-ветку (`git checkout -b feature/amazing-feature`)
3. Зафиксируйте изменения (`git commit -m 'Add amazing feature'`)
4. Запушьте ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📝 Лицензия

Этот проект создан для демонстрации навыков разработки. Все права защищены.

## 📞 Контакты

**Roman Karadev** - Python Developer

- 📧 Email: [vashhukr2008@gmail.com](mailto:vashhukr2008@gmail.com)
- 💬 Telegram: [@KaradevFaceKid](https://t.me/KaradevFaceKid)
- 🐙 GitHub: [testMonzeN](https://github.com/testMonzeN)
- 🌐 VK: [GospodinKaradev](https://vk.com/GospodinKaradev)
- 🔗 Bio: [guns.lol/karadev](https://guns.lol/karadev)

## 🎯 Roadmap

- [ ] Добавить Docker поддержку
- [ ] Интеграция с PostgreSQL
- [ ] Добавить тесты
- [ ] Система комментариев
- [ ] Многоязычность
- [ ] PWA поддержка
- [ ] Темная/светлая тема

---

⭐ Если вам нравится этот проект, поставьте звездочку)

**Сделано с ❤️ и Django**

## 🚀 Быстрый запуск

### 🐳 Docker (Рекомендуется)

```bash
# Сборка и запуск
docker-compose up --build

# Создание миграций
docker-compose exec web python manage.py makemigrations

# Применение миграций
docker-compose exec web python manage.py migrate

# Создание суперпользователя
docker-compose exec web python manage.py createsuperuser

# Доступ к приложению
http://185.232.169.130/
```

### 🛠️ Локальная разработка

```bash
# Виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

# Установка зависимостей
pip install -r requirements.txt

# Миграции
python manage.py makemigrations
python manage.py migrate

# Запуск сервера
python manage.py runserver
```

## 📱 Функции

- **Адаптивный дизайн** - работает на всех устройствах
- **Темная тема** - современный интерфейс
- **Поиск проектов** - быстрый поиск по названию
- **Музыкальная статистика** - воспроизведение треков
- **Контакты** - связь через форму

## 🔧 Технологии

- **Backend**: Django 4.2
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Server**: Nginx + uWSGI
- **Deployment**: Docker + Docker Compose

## 📂 Структура

```
bio/
├── bio/              # Основная конфигурация Django
├── cabinet/          # Приложение с моделями и views
├── static/           # Статические файлы
├── media/            # Медиа файлы
├── templates/        # Шаблоны HTML
├── docker-compose.yml
├── Dockerfile
├── nginx.conf
└── requirements.txt
```

## 🌐 Навигация

- **/** - Главная страница
- **/about/** - О себе
- **/skills/** - Навыки
- **/projects/** - Проекты
- **/contacts/** - Контакты
- **/admin/** - Админ панель

## 🚨 Production

1. Измените `SECRET_KEY` в `settings.py`
2. Установите `DEBUG = False`
3. Настройте `ALLOWED_HOSTS`
4. Используйте HTTPS в nginx
5. Настройте бэкапы PostgreSQL
