"""
Заметки по обработчикам ошибок
"""

# Иерархия ошибок (неполная)
# Источник: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# символ "—" - alt+0151
# BaseException
#
#  +-- KeyboardInterrupt — вызывается при нажатии ctrl+c или delete в момент работы программы
#
#  +-- 1_ Exception — non-system-exiting exceptions are derived from this class. На русском слишком
            # длинное описание :D
#
#       +-- 1_1 StopIteration — некуда итерироваться при выполнении next() или метода итератора
            # __next__()
#       +-- 1_2 StopAsyncIteration — вызывает метод асинхронного итератора __anext__()
#
#       +-- 1_3 ArithmeticError — базовый класс арифметических ошибок
#       |    +-- 1_3_1 FloatingPointError — Not currently used. Нуок О_о
#       |    +-- 1_3_2 OverflowError — ошибка переполнения. Редко используют если integer вышел за
                        # рекомендованый диапазон.
                    # Чаще для integer используют MemoryError
#       |    +-- 1_3_3 ZeroDivisionError — если второе число при делении (делитель) равен нулю
#
#       +-- 1_4 AssertionError — если assert (утверждение) не истинно
#
#       +-- 1_5 AttributeError — ошибка определения или присвоения значения атрибуту. Если эти
                    # операции не поддерживаются объектом в принципе, вызывается TypeError
#
#       +-- 1_6 EOFError — EndOfFile. если в input() был передан только символ конца строки,
                    # то есть пустая строка.
#
#       +-- 1_7 ImportError — import имеет проблемы при импорте модуля. Или from ... import не
                    # находит модуль из списка
#       |    +-- 1_7_1 ModuleNotFoundError — при import модуль не найден
#
#       +-- 1_8 LookupError — базовый класс ошибки при поиске элемента в последовательности
#       |    +-- 1_8_1 IndexError — выход индекса из диапазона. если тип индекса не int,
                        # вызывается TypeError
#       |    +-- 1_8_2 KeyError — ключ в словаре не найден
#
#       +-- 1_9 NameError — локальное или глобальное имя не найдено.
#       |    +-- 1_9_1 UnboundLocalError — локальная переменная внутри функции и\или метода ЕСТЬ,
                        # а вот значения в ней НЕТ, но это не точно
#
#       +-- 1_10 ReferenceError — ошибка при использовании модуля weakref (слабые ссылки)
#
#       +-- 1_11 RuntimeError — ошибка, классификацию которой не определили. Из разряда: тут
                    # ошибка братан. И всё. Дальше сам разбирайся.
                # я думаю это самая "любимая" ошибка программистов на питоне
#       |    +-- 1_11_1 NotImplementedError — используется при работе с абстрактными методами
#                   https://docs.python.org/3/library/exceptions.html#NotImplementedError
#       |    +-- 1_11_2 RecursionError — первышение глубины рекурсии
#       +-- 1_12 SystemError — если возникает ошибка, то стоит отправить данные разработчикам Python.
#
#       +-- 1_13 TypeError — ошибка работы типов. при попытке сложить int и str например
#
#       +-- 1_14 ValueError — тип данных правильный, но значение не валидно




# схема конструкции try ... except
# try:
#     код, который необходимо выполнить
# except:
#     обработка исключения
# else:
#     код, который выполнится если ошибок не произошло
# finally:
#     код, выполняющийся вне зависимости были ошибки или нет

# Как НЕ НАДО использовать try ... except
try:
    do_something()
except:
    pass

# Как НЕ НАДО использовать try ... except вариант 2
try:
    do_something()
except Exception as e:
    print('something going wrong')
# Такая конструкция спрячет ВСЕ остальные варианты ошибок

# Если всё же хочется охватывать все ошибки через Exception, то только так:
import logging

def get_number():
    return int('foo')
try:
    x = get_number()
except Exception as ex:
    logging.exception('Caught an error')
# Через логирование, с полной записью traceback в лог-файл
print('Дальше всё работает')
# Вывод:
# ERROR:root:Caught an error
# Traceback (most recent call last):
#   File "c:\ilya\programming\python\reps\python_notes\exceptions_notes.py", line 93, in <module>  
#     x = get_number()
#   File "c:\ilya\programming\python\reps\python_notes\exceptions_notes.py", line 91, in get_number
#     return int('foo')
# ValueError: invalid literal for int() with base 10: 'foo'
# Дальше всё работает 

# TODO Расписать примеры того, как правильно создавать свои классы ошибок
