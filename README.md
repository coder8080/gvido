# Gvido

Гвидо - мой простой голосовой ассистент, написанный на python, который может управлять ходящим роботом из lego.
Назван он, как вы могли догадаться, в честь [создателя Python](https://ru.wikipedia.org/wiki/%D0%92%D0%B0%D0%BD_%D0%A0%D0%BE%D1%81%D1%81%D1%83%D0%BC,_%D0%93%D0%B2%D0%B8%D0%B4%D0%BE).

# Содержание

- [Запуск](#Запуск)
  - [Windows](#Windows)
    - [Зависимости](#Зависимости)
    - [У меня другая версия](#У_меня_другая_версия)
    - [RHVoice](#RHVoice)
    - [Хочу использовать другой голос](#Хочу_использовать_другой_голос)
    - [Микрофон](#Микрофон)
    - [Погода](#Погода)
    - [Старт](#Старт_windows)
  - [Linux](#Linux)
    - [Отличия от windows-версии](#Отличия_от_windows-версии)
    - [Другие_элементы](#Другие_элементы)
    - [Старт_linux](#Старт_linux)
  - [Mac os](#Mac_os)

# Запуск

Скачиваем код:

```
git clone https://github.com/coder8080/gvido
cd gvido
```

## Windows

Для начала вам нужны:

- Python 3-ей версии
- Рабочий терминал
- Динамики
- Микрофон

### Зависимости

Далее вам нужно установить зависимости:

```
pip install -r requirements.txt
```

Теперь нужно установить pyaudio. На момени создания репозитория его было сложно собрать самому через pip, поэтому в папке installers я оставил готовые билды для 64 разрядной винды для трёх последних версий python:

- 3.8
- 3.9
- 3.10

Свою версию python можно узнать с помощью команды:

```
python -V

```

#### У*меня*другая_версия

Тогда вам нужно скачать билд для вашей версии отсюда [отсюда](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbG95eEZpOGRBNHpERnFwLTk4aHFsSVY3MUt0UXxBQ3Jtc0ttdEI5anAwUWZ2cmNTZzVUMmJoQ0RRWngwbEd2Q2FsekN3Uzk2bWFGdEdrNXhRR3dtTGxjc0RBMGE1aHdDMFZQSjJoX3lxNVR3N28xWWZvaVFOcXZNWF9fcFcwejNfX1ZMemh2ODVWZnFBY3g4TkhITQ&q=https%3A%2F%2Fwww.lfd.uci.edu%2F%7Egohlke%2Fpythonlibs%2F%23pyaudio) и переместить в папку проекта.

Далее устанавливаем готовый билд командой:

```
pip install ./имя_файла_с_билдом
```

_Напоминаю, что билды для перечисленных версий лежат в папке installers._

### RHVoice

Теперь нужно установить rhvoice и голос для него. Устанавливаем как любые другие программы сначала `installers/rhvoice-setup`, потом `installers/rhvoice-alesandr-setup`.

#### Хочу*использовать*другой_голос

Сначала вам нужно скачать его [отсюда](https://rhvoice.ru/ru-voices/) и установить.
Затем проверяем, какие голоса доступны:

```
python ./list-voices.py
```

Смотрим, какой по порядку в списке нужный голос (перед харастеристиками отображается номер) и меняем номер в 48-ой строке файла `main.py`.

### Микрофон

Теперь выбираем микрофон. Убедитесь, что ваш микрофон подключен и работает и посмотрите все доступные микрофоны:

```
python ./list-microphones.py
```

Меняете в 45-ой строке файла `main.py` номер на нужный

### Погода

Чтобы ассистент говорил погоду, вам нужно получить свой api-ключь с сайта [openweathermap](https://openweathermap.org/). Нужна зарегистрироваться, перейти во вкладку api и выбрать бесплатный тариф. Я надеюсь, что ваш iq выше 3 и в с этим разберётесь.
Полученный ключь указываем в 16 строчке вместо `your_api_key`

### Старт_windows

Теперь можно запускать:

```
python ./main.py
```

## Linux

### Отличия_от_windows-версии

- У меня не получилось заставить rhvoice на линуксе, так что довольствуемся голосом из гугл переводчика.
- Роботом с линукса управлять нельзя
- Работает немного медленнее из-за того, что для синтеза речи требуется интернет
- Не нужно отдельно устанавливать Pyaudio

Устанавливаем зависимости:

```
pip install -r ./linux/requirements.txt
```

### Другие_элементы

Настройка [погоды](#Погода) и [выбор микрпофона](#Микрофон) осуществляется как в винде (ссылки активны).

### Старт_linux

```
python ./linux/main.py
```

## Mac_os

Вообще хз. Нет возможности протестировать. Но есть мысли:

- Pyaudio должен установиться нормально
- Роботом скорее всего тоже управлять нельзя (только если exe-шники как-то через эмулятор поднимать)

Вывод: попробуйте установку для линукса.

---

# Проблемы

Привозникновении проблем пишите в [раздел issues](https://github.com/coder8080/gvido/issues)
