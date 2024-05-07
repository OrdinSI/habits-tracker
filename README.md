## Настройка проекта

### Инициализация базы данных
После применения миграций базы данных, необходимо заполнить базу начальными данными. Для этого выполните команду:

```bash
python manage.py create_week_day
```

### Настройка временной зоны
Убедитесь, что временная зона настроена правильно в файле `config.settings.py`:
- Измените `CELERY_TIMEZONE` и `TIME_ZONE` на актуальную для вашего региона.

### Запуск Celery
Для запуска фоновых задач используйте Celery. Запустите worker и beat для обработки задач:

1. Запуск worker:
    ```bash
    celery -A config worker -l INFO
    ```
2. Запуск beat с использованием планировщика задач Django:
    ```bash
    celery -A config beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler
    ```

### Создание суперпользователя
Для доступа к административной панели создайте суперпользователя с помощью следующей команды:

```bash
python manage.py csu
```
