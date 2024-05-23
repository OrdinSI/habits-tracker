## Запуск проекта с использованием Docker

### Шаги по запуску

1. **Клонируйте репозиторий**
    ```bash
    git clone https://github.com/OrdinSI/habits-tracker.git
    cd habits-tracker
    ```

2. **Скопируйте пример файла окружения и отредактируйте его**
    ```bash
    cp .env.example .env
    ```

3. **Постройте и запустите контейнеры Docker**
    ```bash
    docker-compose up  -d --build
    ```

4. **Создание суперпользователя**
    ```bash
    docker-compose exec app python manage.py csu
    ```

### Доступ к приложению

- Приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)
- Админ панель Django: [http://localhost:8000/admin](http://localhost:8000/admin)

### Остановка контейнеров
Для остановки контейнеров используйте следующую команду:

```bash
docker-compose down
