# how to access a folder via terminal
# https://www.youtube.com/watch?v=hv1iJohgQ6s&list=PLJcqk6mrJtxCscRkxYBFIaUFJ0RupGWuc&index=10

# Подключаем модуль sys
import sys      # sys - часть стандартной библиотеки Python

# Принимаем первый аргумент командной строки
# и сохраняем его в переменную name (все это касается работы через
# основной терминал MacOS)
name = sys.argv[1]
last_name = sys.argv[2]

# Выводим слово "Hello" и данные из переменной name
print("Hello,", name, last_name, "!")

