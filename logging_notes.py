# Источники:
    # Конспект статьи: https://realpython.com/python-logging


# Содержание:
# 1_ Уровни сообщений в логгере:

# 2_ Илюстрация уровней логгирования

# 3_ Конфигурация root логгера

# 4_ Обработчики ошибок и логгирование
    # 4_1 С использованием спец. флага exc_info
    # 4_2 Использование спец. метода exception

# 5_ Кастомные логгеры
    # 5_1 Создаём кастомный логгер
    # 5_2 Создаём логгер с именем модуля, в котором он находится
    # 5_3 Проверяем обработку лога сформированного в другом файле

# 6_ Конфигурируем кастомный логгер
    # 6_1 Введение в основные сущности библиотеки logging
    # 6_2 Пример конфигурации кастомного логгера




# TODO Расписать отличие root логгера и созданного через logger.getLogger(), например конфигурация и т.д.
# 1_ Уровни сообщений в логгере:
"""
- CRITICAL
- ERROR
- WARNING - по умолчанию
- INFO
- DEBUG

У логгера можно выставить уровень сообщений, которые будут обрабатываться.
Всё что находится ниже указанного уровня, обрабатываться логгером не будет.
"""



# 2_ Илюстрация уровней логгирования
import logging

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
# Вывод:
# WARNING:root:This is a warning message
# ERROR:root:This is an error message
# CRITICAL:root:This is a critical message

# Так как уровень WARNING стоит по умолчанию, то логгер не обработал сообщения,
#   стоящие уровнем ниже чем WARNING




# 3_ Конфигурация root логгера
"""
Для настройки root логгера используется метод basicConfig(), его параметры:
    level: Уровень обрабатываемых сообщений
    filename: Путь к файлу лога. То есть с каким файлом работает логгер. Если путь не указан,
      то лог выводится в консоль.
      filemode: Если путь указан, то можно указать тип работы (аналогично функции open()):
        - 'a' - append - по умолчанию
        - 'w' - write - при каждом запуске программы и конфигурации логгера, файл логов будет перезаписан
        - 'x' open for exclusive creation, failing if the file already exists
        - 'b' binary mode
        - 't' text mode (default)
    format: Строка форматирования записи лога, какие параметры можно указать:
        - %(name)s - имя логгера
        - %(asctime)s - формат времени ‘2003-07-08 16:49:45,896’
        - %(levelname)s - уровень сообщения
        - %(message)s - текст сообщения
    Подробнее: https://docs.python.org/3/library/logging.html#logrecord-attributes

    !!! метод basicConfig можно вызвать единожды, дальнешие вызовы будут игнорироваться !!!
    но это не точно
"""

logging.basicConfig(
    level=logging.ERROR,
    format='(%(name)s) %(asctime)s: <%(levelname)s> - %(message)s'
    # Так как аргумент filename не указан, будет использоваться режим вывода по умолчанию - в консоль.
)




# 4_ Обработчики ошибок и логгирование
a = 5
b = 0


# 4_1 С использованием спец. флага exc_info
"""
Флаг exc_info в значении True всегда выводит traceback в сообщении
"""
try:
    print('Exception logging v1')
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
# Вывод:
# (root) 2021-03-30 20:04:13,331: <ERROR> - Exception occurred
# Traceback (most recent call last):
#   File "d:\Programming\Python\projects\python_notes\logging_notes.py", line 45, in <module>
#     c = a / b
# ZeroDivisionError: division by zero


# 4_2 Использование спец. метода exception
"""
Если вкратце, то logging.exception() == logging.error(exc_info=True)
По сути это синтаксический сахар, делающий код более лаконичным
"""
try:
    print('\n\nException logging v2')
    c = a / b
except Exception as e:
    logging.exception("Exception occurred v2")
# Вывод:
# Exception logging v2
# (root) 2021-03-30 21:50:50,273: <ERROR> - Exception occurred v2
# Traceback (most recent call last):
#   File "d:\Programming\Python\projects\python_notes\logging_notes.py", line 69, in <module>
#     c = a / b
# ZeroDivisionError: division by zero




# 5_ Кастомные логгеры
# 5_1 Создаём кастомный логгер
my_logger = logging.getLogger('my_custom_logger')
try:
    print('\n\nException logging custom')
    c = a / b
except Exception as e:
    my_logger.exception("Exception occurred v2 via custom logger")
# Вывод:
# Exception logging custom
# (my_custom_logger) 2021-03-30 21:50:50,275: <ERROR> - Exception occurred v2 via custom logger
# Traceback (most recent call last):
#   File "d:\Programming\Python\projects\python_notes\logging_notes.py", line 78, in <module>
#     c = a / b
# ZeroDivisionError: division by zero


print()
# 5_2 Создаём логгер с именем модуля, в котором он находится
test_logger = logging.getLogger(__name__)
test_logger.info('Hello from module logger')
# Вывод:
# (__main__) 2021-03-30 21:44:30,174: <INFO> - Hello from module logger


# 5_3 Проверяем обработку лога сформированного в другом файле
"""
Код файла logging_test_submodule:
    from logging import getLogger


    logger = getLogger(__name__)

    def say_hi():
        logger.info('Hi from logging_test_submodule')
"""
import logging_test_submodule

logging_test_submodule.say_hi()
#Вывод:
# (logging_test_submodule) 2021-03-30 21:44:30,175: <INFO> - Hi from logging_test_submodule




# 6_ Конфигурируем кастомный логгер
# 6_1 Введение в основные сущности библиотеки logging
"""
Logger: Непосредственно сам логгер, через экземпляры логгера как раз таки вызываются методы info(), warning(), critical() и другие

LogRecord: Запись лога, экземпляры этого класса хранят в себе всю информацию, которую указали для логирования

Handler: Отправляют записи лога в указанную точку вывода. Класс Handled является базовым для классов:
    StreamHandler - вывод в консоль (по умолчанию)
    FileHandler - вывод в файл
    SMTPHandler - вывод отправляется по почте
    HTTPHandler - отправка вывода по сети

Formatter: Ну тут всё говорит за себя. Класс форматирования лога перед отправкой в точку вывода
"""


# 6_2 Пример конфигурации кастомного логгера
logger = logging.getLogger('some_custom_logger')
# Создаём обработчики логов
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')
console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

# Создаём строки форматирования и связываем с обработчиками
console_log_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
file_log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_log_format)
file_handler.setFormatter(file_log_format)

# Добавляем обработчики в логгер
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.warning('This is a warning')
logger.error('This is an error')
# Вывод:
# some_custom_logger - WARNING - This is a warning
# WARNING:some_custom_logger:This is a warning
# some_custom_logger - ERROR - This is an error
# ERROR:some_custom_logger:This is an error

# Запись в файле file.log:
# 2021-03-31 00:32:54,256 - some_custom_logger - ERROR - This is an error