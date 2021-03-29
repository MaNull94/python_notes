# Уровни сообщений в логгере:
"""
- CRITICAL
- ERROR
- WARNING - по умолчанию
- INFO
- DEBUG

У логгера можно выставить уровень сообщений, которые будут обрабатываться.
Всё что находится ниже указанного уровня, обрабатываться логгером не будет.
"""

# Конфигурация логгера
"""
Для настройки логгера можно использовать метод basicConfig(), его параметры:
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
"""





import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(name)s) %(asctime)s: <%(levelname)s> - %(message)s'
)
my_logger = logging.getLogger('my_logger')
a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)

try:
    c = a / b
except Exception as e:
    logging.exception("Exception occurred v2")

try:
    c = a / b
except Exception as e:
    logging.debug("Exception occurred", exc_info=True)