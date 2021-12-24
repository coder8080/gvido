"""Выводит все доступные голоса"""
import pyttsx3

engine = pyttsx3.init()
print(*[f'{i}-{e}' for i, e in enumerate(engine.getProperty('voices'))],
      sep='\n')
