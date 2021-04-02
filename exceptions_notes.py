"""
Заметки по обработчикам ошибок
"""


# Содержание:
# 1_ Иерархия ошибок (неполная)

# 2_ схема конструкции try ... except
    # 2_1 Примеры использования try ... except
        # 2_1_1 Как НЕ НАДО использовать try ... except
        # 2_1_2 Как НЕ НАДО использовать try ... except вариант 2
        # 2_1_3 Если всё же хочется охватывать все ошибки через Exception, то только так:

# 3_ Связанные исключения
    # 3_1 С использованием конструкции raise <exc> from <exc>
    # 3_2 Без использования конструкции
    # 3_3 Отличие между вызовами использования raise ... с использованием from ... и без
    # 3_4 Хороший пример использования raise ... from ...

# 4_ Как создавать свои классы исключений
    # 4_1 Правила:
    # 4_2 Исключение без параметров
    # 4_3 Хороший пример иерархии собственных исключений




# 1_ Иерархия ошибок (неполная)
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




# 2_ схема конструкции try ... except
# try:
#     код, который необходимо выполнить
# except:
#     обработка исключения
# else:
#     код, который выполнится если ошибок не произошло
# finally:
#     код, выполняющийся вне зависимости были ошибки или нет


# настройки перед практическими примерами
from datetime import datetime
import logging
logging.basicConfig(filename='exc.log', level=logging.INFO)
logging.info(f'{datetime.now()}')




# 2_1 Примеры использования try ... except
# 2_1_1 Как НЕ НАДО использовать try ... except
try:
    do_something()
except:
    pass


# 2_1_2 Как НЕ НАДО использовать try ... except вариант 2
try:
    do_something()
except Exception as e:
    print('something going wrong')
# Такая конструкция спрячет ВСЕ остальные варианты ошибок


# 2_1_3 Если всё же хочется охватывать все ошибки через Exception, то только так:
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




print('\n')
# 3_ Связанные исключения
# 3_1 С использованием конструкции raise <exc> from <exc>
"""
Эта конструкция изменяет контекст вывода связанных ошибок
"""
try:
    try:
        print(1 / 0)
    except Exception as exc:
        raise RuntimeError("Something bad happened") from exc
except Exception:
    logging.exception('chaining exceptions WITH raise ... from')


# 3_2 Без использования конструкции
try:
    try:
        print(1 / 0)
    except Exception as exc:
        raise RuntimeError("Something bad happened")
except Exception:
    logging.exception('chaining exceptions WITHOUT raise ... from')


# 3_3 Отличие между вызовами использования raise ... с использованием from ... и без
"""
Запись в лог при использовании raise <exc1> from <exc2>
<сообщение переданное как аргумент логирования>
<traceback от exc1>
!!! The above exception was the direct cause of the following exception: !!!
(Перевод: Вышеупомянутое исключение явилось прямой причиной следующего исключения:)
<traceback от exc2>

Запись в лог при использовании просто raise <exc>
<сообщение переданное как аргумент логирования>
<traceback от exc1>
!!! During handling of the above exception, another exception occurred: !!!
(Перевод: Во время обработки вышеуказанного исключения произошло другое исключение:)
<traceback от exc2>

Вывод: Такой контекст между двумя записями об ошибке явно указывает что ошибки связаны между собой
"""

# 3_4 Хороший пример использования raise ... from ...
# https://stackoverflow.com/questions/24752395/python-raise-from-usage#comment38446019_24752607


# 4_ Как создавать свои классы исключений
# 4_1 Правила:
#   1. Наследоваться можно только от класса Exception
#   2. Если необходима целая иерархия собственных исключений, то базовый класс наследуется от Exception,
#       а далее классы наследуются от базового.

# 4_2 Исключение без параметров
class MyCustomException(Exception):
    pass


try:
    some_val = 2 + 2
    if some_val == 4:
        # raise - оператор вызова исключения
        raise MyCustomException("custom message text from raise")
except MyCustomException:
    print('MyCustomException is called')
# Вывод:
# MyCustomException is called


# 4_3 Хороший пример иерархии собственных исключений
# Источник: https://stackoverflow.com/a/60465422
# To define your own exceptions correctly, there are a few best practices that you should follow:
# Define a base class inheriting from Exception. This will allow to easily catch any exceptions related to the project:
class MyProjectError(Exception):
    """A base class for MyProject exceptions."""
# To add support for extra argument(s) to a custom exception, define a custom __init__() method with a
#   variable number of arguments. Call the base class's __init__(), passing any positional
#   arguments to it (remember that BaseException/Exception expect any number of positional arguments):
class CustomError(MyProjectError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.foo = kwargs.get('foo')
# To raise such exception with an extra argument you can use:
raise CustomError('Something bad happened', foo='foo')


