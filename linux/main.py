"""linux версия"""

# получаю зависимости
import webbrowser
import subprocess
import gtts
import playsound
import speech_recognition as sr
from fuzzywuzzy import fuzz
import datetime
import random
import pyowm

# Настраиваю pyowm
owm = pyowm.OWM('your_api_key')
o = owm.weather_manager().weather_at_place('Moscow,Ru')

# Объект распознавателя
r = sr.Recognizer()

# Настройки
options = {
    # Имя ассистента
    'name': 'гвидо',
    # Команды
    'cmd': {
        'time': ['сколько времени', 'который час', 'время'],
        'thanks': ['спасибо', 'классно', 'молодец', 'крут'],
        'humor': ['расскажи анекдот', 'анекдот', 'шутка', 'пошути'],
        'weather': ['погода', 'на улице', 'температура'],
        'explorer': ['открой проводник', 'файлы'],
        'whoareyou': ['кто ты', 'кто ты такой', 'кто'],
        'howtolearn': ['как научиться программировать', 'научиться']
    },
    # Номер микрофона (необходимо изменить), у вас он 100% другой
    'microphone_index': 17,
}


def say(text: str):
    """Функция синтеза речи"""
    tts = gtts.gTTS(text, lang='ru')
    tts.save('audio.mp3')
    playsound('audio.mp3')


def say_random(vars: list):
    """Воспроизводит рандомную из предоставленных фраз"""
    say(random.choice(vars))


def command(text: str):
    """Основная функция (распознаёт и выполняет команды)"""
    # Вывожу, что оудалось распознать
    print('[log] Распознано:' + text)
    # Если пользователь обратился к ассистенту
    if fuzz.ratio(text.split()[0], options['name']) > 50:
        # Убираю из текста имя, чтобы оно не мешало распознаванию
        text = ' '.join(text.split()[1:])
        # Распознаю команду
        cmd = {'cmd': '', 'persent': 0}
        for command, values in options['cmd'].items():
            for c in values:
                if fuzz.ratio(text, c) > cmd['persent']:
                    cmd['cmd'] = command
                    cmd['persent'] = fuzz.ratio(text, c)
        # Обрезаю процент совпадения
        cmd = cmd['cmd']
        # Выполняю команду
        if cmd == 'time':
            now = datetime.datetime.now()
            res = f'сейчас {now.hour} {now.minute}'
            if now.minute // 10 == 0:
                res = f'сейчас {now.hour} 0{now.minute}'
            say(res)
        elif cmd == 'thanks':
            say_random(['рад стараться.', 'вы лучший'])
        elif cmd == 'humor':
            say_random([
                'Занимайтесь лбимым делом и вы никогда не будете \
                работать. Кушать тоже будете редко.', 'Дела шли хорошо, но \
                фиг знает куда.'
            ])
        elif cmd == 'weather':
            weather = o.weather
            say(f'сейчас на улице {int(weather.temperature("celsius")["temp"])}\
            градусов')
        elif cmd == 'explorer':
            subprocess.Popen('nemo')
            say_random(['Готово', 'Открываю'])
        elif cmd == 'whoareyou':
            webbrowser.open(
                'https://ru.wikipedia.org/wiki/%D0%92%D0%B0%D0%BD_%D0%A0%D0%BE%D1%81%D1%81%D1%83%D0%BC,_%D0%93%D0%B2%D0%B8%D0%B4%D0%BE',
                new=2)
            say('Создатель питона')
        elif cmd == 'howtolearn':
            webbrowser.open('https://docs.python.org/3/index.html', new=2)
            say('Сначала научитесь гуглить')


# Здороваюсь
say('Доброго времени суток')
say('Я вас слушаю')

# Основной цикл
while True:
    with sr.Microphone(device_index=options['microphone_index']) as m:
        print('listening...')
        audio = r.listen(m)
    try:
        # Пробуем распознать и соответственно исполнить команду
        text = r.recognize_google(audio, language='ru-RU')
        command(text.lower())
    except:
        print('[log] Не смог распознать')
