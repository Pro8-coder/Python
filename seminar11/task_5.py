"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""
from chardet import detect
import subprocess

lst1 = ['ping', 'yandex.ru']
ping_ya = subprocess.Popen(lst1, stdout=subprocess.PIPE)
for line in ping_ya.stdout:
    result = detect(line)
    print(line.decode(result['encoding']))
print('-' * 79)
lst2 = ['ping', 'youtube.com']
ping_yt = subprocess.Popen(lst2, stdout=subprocess.PIPE)
for line in ping_yt.stdout:
    result = detect(line)
    print(line.decode(result['encoding']))
