# Парсер телеграм бот

### Описание

Бот для парсинга страниц. Для работы ему необходимо скинуть excel файл следующего формата:

| title    | url                   | xpath                               |
|----------|-----------------------|-------------------------------------|
| Название | Ссылка откуда парсить | xpath элемента котрый нужно собрать |

### Стек
- python - язык разработки
- aiogram - фреймворк для написания логики бота
- sqlite - БД для хранения информации
- SQLAlchemy - ORM для взаимодействия с БД


### Функционал бота:

start/ - приветствие
отправлен excel файл - скачивает файл, сохраняет в папку, парсит с помощью pandas, после чего парсит url'ы и находит xpath указанные в файле

### Запуск
Добавьте переменные окружения в файл .env
```python
BOT_TOKEN = ""
```

Выполнить миграции
```bash
alembic upgrade head
```

Зайти в директорию bot
```bash
cd bot
```

Запустить бота
```bash
python main.py
```


### О себе
Целеустремленный Python разработчик - альтруист, ищущий оффер мечты.

Занимаюсь разработкой более 2х лет, умею: писать чистый код, проводить code review, взаимодействовать со сторонними API, разрабатывать RESTful API, писать unit тесты, работать в команде, декомпозировать сложные задачи. Также имею 3 года опыта работы в нефтяной и тепловых компаниях,

Реализовал 5 проектов 1 из них коммерческий (парсер для компании АНО "Центр развития"), 1 командный (интернет магазин бытовой техники), 1 для личных целей (телеграмм бот для учета заправленного топлива), остальные учебные.

Выбор нового направления в качестве python разработчика, обусловлен тем, что разработчик творческая и в то же время техническая профессия. Разработка дает возможность делать жизнь проще как для бизнеса, так и для людей.

Telegram: https://t.me/ReBiwer
Github: https://github.com/ReBiwer
