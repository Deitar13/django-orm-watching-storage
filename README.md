# Пульт охраны банка
Данная программа это пульт охраны банка, она отображает все посещения депозитария с целью мониторинга и выявления подозрительных посещений, программа способна отображать активные карточки посетителей, время и продолжительность посещения, а так же отображать подозрительные посещения.


## Установка и требования
Для установки скачайте и распакуйте архив с программой. 
Создайте файл `.env` и внесите в него свои параметры и данные: 
```
DB_ENGINE=
DB_HOST=
DB_PORT=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_SECRET_KEY=
DEBUG=false
```
либо отредактируйте список параметров DATABASES в скрипте: 
`\django-orm-watching-storage\project\settings.py`

Для использования программы вам необходимы:
`python 3.5` или новее
`pip` или `pip3`

для установки необходимых библиотек и пакетов введите в консоли: 
`pip install -r requirements.txt`

либо установите следующие пакеты в ручную:
```
asgiref==3.5.0
Django==3.2.12
psycopg2-binary==2.9.3
pytz==2021.3
sqlparse==0.4.2
typing-extensions==4.0.1
```

## режим DEBUG
По умолчанию режим debug выключен, для включения, установите параметр `DEBUG=True` в файле .env или в скрипте: 
`\django-orm-watching-storage\project\settings.py`