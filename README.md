# Пульт охраны банка «Сияние»

## Описание проекта

**Пульт охраны** — это Django-приложение, которое подключается  
к удалённой базе данных с визитами и карточками пропуска сотрудников банка.  
С его помощью можно отслеживать, кто находится в здании,  
и анализировать продолжительность визитов.

---

## Как установить и запустить

1. **Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/Adelina2302/django-orm-watching-storage-part-1
   cd django-orm-watching-storage-part-1
   ```
2. **Создайте виртуальное окружение и активируйте его:**
   ```bash
python -m venv venv
source venv/bin/activate       # для Mac/Linux
venv\Scripts\activate          # для Windows
   ```

3. **Установите зависимости:**
   ```bash
pip install -r requirements.txt
   ```

4. **Создайте файл .env в корне проекта и добавьте туда настройки:**
   ```bash
ENGINE=
HOST=
PORT=
NAME=
USER=
PASSWORD=
SECRET_KEY=
   ```

5. **Запустите скрипт:**
   ```bash
python main.py
   ```
