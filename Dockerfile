# Базовый образ, содержащий Python
FROM python:3

# Создание директории приложения внутри контейнера
WORKDIR /app

# Копирование файлов .py в директорию приложения в контейнере
COPY data_e.csv .
COPY main.py .
COPY task_a.py .
COPY task_b.py .
COPY task_c.py .
COPY task_d.py .
COPY task_e.py .
COPY task_f.py .

# Установка зависимостей, если они есть
# RUN pip install -r requirements.txt

# Команда для запуска приложения (здесь просто пример)
CMD ["python", "main.py"]