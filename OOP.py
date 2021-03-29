"""файл-шпаргалка по ООП в python

Блоки кода подписаны для поиска
"""
# Содержание:

# 1_ Класс и экземпляр класса
    # 1_1 класс
    # 1_2 создаём экземпляр класса SimpleClass
    # 1_3 создать новый экземпляр класса используя существующий экземляр класса:

# 2_ Пространства имён класса и экземпляра
    # 2_1 Выводим уникальные атрибуты объекта SC_object относительно базовой сущности ЯП python - object

# 3_ конструктор или инициализатор экземпляра класса
    # 3_1 аргумент self в методах экземпляра

# 4_ Методы
    # 4_1 Объявляем класс Server
        # 4_1_1 show_info, toggle_on и toggle_off являются методами экземпляра
        # 4_1_2 get_servers_host и change_host - методы класса
        # 4_1_3 show_users - статический метод
    # 4_2 методы экземпляра
        # 4_2_1 проходим циклом по списку экземпляров и запускаем у каждого метод show_info
        # 4_2_2 Изменяем статус серверов database и mail. После снова выводим информацию по ним
    # 4_3 методы класса
        # 4_3_1 Выводим значение поля класса используя метод класса
        # 4_3_2 Изменяем поле класса используя метод класса
    # 4_4 Попытка изменить поле класса через экземпляр
    # 4_5 Ответ на вопрос 'Поле экземпляра с таким же именем "спрячет" поле класса'
    # 4_6 статические методы
        # 4_6_1 Вызываем статический метод из класса и из экземпляра

# 5_ Наследование
    # 5_1 Наследование без инициализации экземпляров
        # 5_1_1 Создаем базовый класс
        # 5_1_2 Создаем наследника без функционала
        # 5_1_3 Пробуем вызвать метод класса show_some_attr у наследника
        # 5_1_4 Пробуем получить значение show_some_attr через наследника напрямую
        # 5_1_5 Выводим словарь имён класса ChildClass
    # 5_2 Наследование и инициализация экземпляров. Оператор super
        # 5_2_1 Переопределяем базовый класс
        # 5_2_2 Наследование от базового класса
            # 5_2_2_1 Переопределяем класс наследника
            # 5_2_2_2 Создаем экзепляр наследника
            # 5_2_2_3 Выводим словарь имён экземпляра наследника
        # 5_2_3 Наследование от наследника
            # 5_2_3_1 Создаем класс наследника от наследника
            # 5_2_3_2 Создаем экзепляр
            # 5_2_3_3 Выводим словарь имён экземпляра наследника наследника
    # 5_3 Наследник наследника пробует через оператор super вызвать метод BaseClass
    # 5_4 Множественное наследование. MRO (Method Resolution Order)
        # 5_4_1 Пример для демонстрации. Как мне кажется в реальной разработке не надо так делать.
            # 5_4_1_1 Объявляем FirstClass и SecondClass, указываем у каждого поле class_name
            # 5_4_1_2 Объявляем класс-наследник с порядком наследования: FirstClass, SecondClass
            # 5_4_1_3 Объявляем еще один класс-наследник с порядком наследования: SecondClass, FirstClass
            # 5_4_1_4 Выводим порядок поиска (MRO) у экземпляров FirSec_obj и SecFir_obj
    # 5_5 Выводы из блока 5_4 и краткая заметка об иерархии наследования в python
    # 5_6 Миксины - расширяющий класс, для подмешивания функционала (mix in)
        # 5_6_1 Описание примера
        # 5_6_2 объявлем класс FoodMixin
        # 5_6_3 объявляем класс Person, Animal
        # 5_6_4 Расширяем иерархию классов и объявлем классы Employee и Cat с использованием mixin класса
        # 5_6_5 Вызываем метод get_food у экземпляров

# 6_ Полиморфизм
    # 6_1 Задача: найти площадь прямоугольника, квадрата, круга
        # 6_1_1 Объявляем класс Rectangle, Square, Circle.
        # 6_1_2 В каждом классе определяем метод с именем get_area (получить площадь)
        # 6_1_3 создаем экземпляры и помещаем в список
        # 6_1_4 Проходим циклом по списку фигур и вызываем у каждой метод get_area

# 7_ Модификаторы доступа полей и методов: публичный, защищенный, приватный
    # 7_1 Объявляем класс и указываем публичное, не публичное и приватное поле экземпляра
    # 7_2 Создаем экземпляр и присваиваем значения полям
    # 7_3 Выводим значение публичного и не-публичного поля
    # 7_4 Пытаемся вывести приватное поле
    # 7_5 Выводим словарь экземпляра

# 8_ Инкапсуляция
    # 8_1 Свойства (property)
        # 8_1_1 Объявляем класс Account
            # 8_1_1_1 Первый вариант использования свойств
            # 8_1_1_2 Второй вариант использования свойств (буэээээ)
        # 8_1_2 Создаем экземпляры и тестируем работу свойств
            # 8_1_2_1 Выводим значения полей и атрибутов экземпляров
            # 8_1_2_2 Изменяем значения атрибутов
            # 8_1_2_3 Снова выводим значения полей и атрибутов
    # 8_2 дескрипторы(блок не готов. Оставил на потом)
    # 8_3 __getattr__, __setattr__, __getattribute__(тоже отмена, сложная тема. 


# 1_ Класс и экземпляр класса
"""Итак, ООП. Базовые сущности ООП:
    - класс
    - экземпляр класса
"""
print('\n\n1_  ********************')
# 1_1 класс
class SimpleClass:
    pass

# 1_2 создаём экземпляр класса SimpleClass
simple_object = SimpleClass()
print(f'type(simple_object): {type(simple_object)}\n')
# Вывод: <class '__main__.SimpleClass'> 

# 1_3 создать НОВЫЙ экземпляр класса используя СУЩЕСТВУЮЩИЙ экземляр класса:
another_simple_object = type(simple_object)()
print(f'type(another_simple_object): {type(another_simple_object)}\n')
# Вывод: <class '__main__.SimpleClass'>



# TODO Дополнить коммент. Указать что именно содержат пространство класса и экземпляров
# 2_ Пространства имён класса и экземпляра
"""У класса и у КАЖДОГО экземпляра класса есть своё пространство имён
- У класса — пространство имён класса (поля класса и т. д.)
- У экземпляра - пространство имён экземпляра,
    то есть на каждый экземпляр создается его УНИКАЛЬНОЕ пространство имён
При этом ЭКЗЕМПЛЯРЫ класса могут получить значение полей КЛАССА, так как идет поиск по иерархии наследования
"""

print('\n\n2_  ********************')
class SomeClass:
    class_attr = 'class attribute'

# Создаем экземпляр класса
SC_object = SomeClass()

# присваиваем значение НОВОМУ атрибуту экземпляра
SC_object.object_attr = 'object attribute'

# Выводим словарь содержащий элементы пространства имён ЭКЗЕМПЛЯРА класса
print(f'SC_object.__dict__: {SC_object.__dict__}\n')
# Вывод: {'object_attr': 'object attribute'}

# Выводим словарь содержащий элементы пространства имён класса
print(f'SomeClass.__dict__: {SomeClass.__dict__}\n')
# Вывод:
# {'__module__': '__main__', 'class_attr': 'class attribute',
# '__dict__': <attribute '__dict__' of 'SomeClass' objects>,
# '__weakref__': <attribute '__weakref__' of 'SomeClass' objects>, '__doc__': None}

# 2_1 Выводим уникальные атрибуты объекта SC_object относительно базовой сущности ЯП python - object
print(f'set(dir(SC_object)) - set(dir(object)): {set(dir(SC_object)) - set(dir(object))}')
# Вывод: {'__module__', 'class_attr', '__dict__', 'object_attr', '__weakref__'}

# Пробуем получить значение class_attr у экземпляра класса
print(f'SC_object.class_attr: {SC_object.class_attr}')
# Вывод: class attribute




# 3_ конструктор и инициализатор экземпляра класса
"""
https://docs.python.org/3/reference/datamodel.html?highlight=__new__#object.__new__

При создании экземпляра класса сначала вызывается метод new а затем метод init.
Переопределять метод __new__ нужно только в редких случаях работы с наследованием типов....

new() is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to
customize instance creation.  It is also commonly overridden in custom metaclasses in order to
customize class creation.

Because new() and init() work together in constructing objects (new() to create it, and init() to customize it),
no non-None value may be returned by init(); doing so will cause a TypeError to be raised at runtime.

Таким образом конструктор экземпляра вызывается неявно (__new__), а добавление 
атрибутов экземпляра при необходимости происходит в методе __init__
"""

print('\n\n3_  ********************')
# 3_1 аргумент self в методах экземпляра
"""главное отличие метода от функции в дополнительном аргументе self
self - это ссылка на конкретный экземпляр класса, который вызывает данный метод
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('self name:', self.name)
        print('self age:', self.age)
        print('self:', self)


print('create Person object')
# Так как в методе инициализации указаны принты, они выводятся на экран при создании экземпляра
ivan = Person('Ivan', 15)
# Вывод:
# self name: Ivan
# self age: 15
# self: <__main__.Person object at 0x000001E5ED2232B0>

# переводим id в шеснадцатеричную систему и получаем адрес памяти экземпляра ivan
print('hex(id(ivan)):', hex(id(ivan)))
# Вывод: hex(id(ivan)): 0x1e5ed2232b0
print()
print('create another Person object')
egor = Person('Egor', 29)
# Вывод:
# self name: Egor
# self age: 29
# self: <__main__.Person object at 0x000001E5ED223370>

# так же получаем адрес памяти экземпляра egor
print('hex(id(egor)):', hex(id(egor)))
# Вывод: hex(id(egor)): 0x1e5ed223370




# 4_ Методы
"""
 ___________________________________________________________________________________________
|                   |        доступ к         |            вызов из            |  вызов из  |
|      метод        |    пространству имен    |             класса             | экземпляра |
|———————————————————|—————————————————————————|————————————————————————————————|————————————|
|   метод класса    |         класса          |               ДА               |     ДА     |
|———————————————————|—————————————————————————|————————————————————————————————|————————————|
|                   | экземпляра либо класса, | ДА, указав ссылку на экземпляр |     ДА     |
| метод экземпляра  | если поля или метода    |    класса первым аргументом    |            |
|                   | нет в П.И. экземпляра   |                                |            |
|———————————————————|—————————————————————————|————————————————————————————————|————————————|
| статический метод |       не имеет          |                ДА              |     ДА     |
 ———————————————————————————————————————————————————————————————————————————————————————————
Метод класса и метод экземпляра не ограничивается текущим классом, т.е.
  поиск поля и\или метода идет по иерархии классов, вплоть до базовой сущности - object
"""
# В блоке 5_5 подробнее расписан порядок поиска
"""
С функцией внутри класса дела обстоят сложнее.
При вызове функции из класса ошибок не будет. Но если вызвать функцию из экземпляра,
  то в функцию будет передан self - ссылка на экземпляр. Что либо приведет к ошибке лишнего аргумента,
  либо изменит поведение функции, потому как первым аргументом будет self.                                            
Для функций лучше добавлять декоратор @staticmethod.  Тогда функция будет работать как обычно.
"""

print('\n\n4_ ********************')
# 4_1 Объявляем класс Server
class Server:
    host = 'localhost'

    def __init__(self, name, ip, isOn=False):
        self.name = name
        self.ip = ip
        self.isOn = isOn

    # 4_1_1 show_info, toggle_on и toggle_off являются методами экземпляра
    def show_info(self):
        server_info = f"""
        Server info:
        Name: {self.name}
        IP: {self.ip}
        Status: {'ON' if self.isOn==True else 'OFF'}
        """
        print(server_info)

    def toggle_on(self):
        self.isOn = True
        print(f'Server "{self.name}" is toggled ON')
    
    def toggle_off(self):
        self.isOn = False
        print(f'Server "{self.name}" is toggled OFF')

    # 4_1_2 get_servers_host и change_host - методы класса
    # Для перевода в метод класса используется декоратор @classmethod
    # Отличие от обычного метода в том, что метод класса принимает
    #   ссылку на сам КЛАСС, а не на ЭКЗЕМПЛЯР класса.
    # Поэтому первый аргумент пишется как cls 
    @classmethod
    def get_servers_host(cls):
        return cls.host
    
    @classmethod
    def change_host(cls, new_host):
        cls.host = new_host
        print(f'Servers host was changed to {cls.host}')
    
    # 4_1_3 show_users - статический метод
    # По сути статический метод это функция класса. спец декоратор нужен для того чтобы
    # статический метод мог без ошибки вызываться экземплярами класса
    @staticmethod
    def show_users():
        return 'Список пользователей:' + str(users)

# Создаем экземпляры класса Server
domain_server = Server('domain', ip='127.0.0.5', isOn=True)
database_server = Server('database', ip='127.0.0.6')
mail_server = Server('mail', ip='127.0.0.10', isOn=True)

servers = (
    domain_server,
    database_server,
    mail_server
)


# 4_2 методы экземпляра
# 4_2_1 проходим циклом по списку экземпляров и запускаем у каждого метод show_info
for server in servers:
    server.show_info()
# Вывод:
# Server info:
# Name: domain
# IP: 127.0.0.5
# Status: ON
# 
# Server info:
# Name: database
# IP: 127.0.0.6
# Status: OFF
# 
# Server info:
# Name: mail
# IP: 127.0.0.10
# Status: ON

# 4_2_2 Изменяем статус серверов database и mail. После снова выводим информацию по ним
database_server.toggle_on()
# Вывод: Server "database" is toggled ON

mail_server.toggle_off()
# Вывод: Server "mail" is toggled OFF

database_server.show_info()
# Вывод:
# Server info:
# Name: database
# IP: 127.0.0.6
# Status: ON

mail_server.show_info()
# Вывод:
# Server info:
# Name: mail
# IP: 127.0.0.10
# Status: OFF

# Хоть вызов поля host идет из экземпляров, это по прежнему поле класса Server
database_host = database_server.host
mail_host = mail_server.host
print('database_host and mail_host is Server.get_servers_host():',
       database_host and mail_host is Server.get_servers_host())
# Вывод: True


# 4_3 методы класса
# 4_3_1 Выводим значение поля класса используя метод класса
print('Server.get_servers_host():', Server.get_servers_host())
# Вывод: localhost

# 4_3_2 Изменяем поле класса используя метод класса
Server.change_host('Amazon')
# Вывод: Servers host was changed to Amazon

# Выводим значение поля класса - host используя экземляр domain_server
print('domain_server.host:', domain_server.host)
# Вывод: domain_server.host: Amazon


# 4_4 Попытка изменить поле класса через экземпляр
database_server.host = 'localhost'

# Выводим словарь имен экземпляра database_server, что увидеть значение поля host
print('database_server.__dict__', database_server.__dict__)
# Вывод:
# database_server.__dict__ {'name': 'database', 'ip': '127.0.0.6',
#                           'isOn': True, 'host': 'localhost'}

# Снова выводим значение поля класса
print('Server.host is:', Server.host)
# Вывод: Server.host is: Amazon

# Проходим циклом список серверов и выводим значение поля host 
for server in servers:
    print(f'{server.name} host:', server.host)
# Вывод
# domain host: Amazon
# database host: localhost
# mail host: Amazon

# 4_5 Ответ на вопрос 'Поле экземпляра с таким же именем "спрячет" поле класса'
"""
Когда объект обращается к полю, python ищет поле последовательно:
  - экземпляр
  - класс
  - класс родитель (при наличии такого)
  - и далее по областям видимости
В нашем случае поле host появилось в пространстве имен экземпляра,
  то есть в пространстве имен класса Server python искать не будет
"""

# Совершенно непонятное для меня поведение.  id методов класса Servers совпадает с id методов класса Empty_class
# TODO нужно потом уточнить чей это id
# 
# for server in servers:
#     print(f'server {server.name} method toggle_on :', server.toggle_on)
#     print(f'server {server.name} method toggle_on id:', id(server.toggle_on))
# 
# class Empty_class:
#     pass
# 
#     def metod(self):
#         print(f'hi from {self}')
# 
# e1 = Empty_class()
# e2 = Empty_class()
# 
# e_list = (e1, e2)
# 
# for obj in e_list:
#    print(f'obj {obj} metod:', obj.metod)
#    print(f'obj {obj} metod id:', id(obj.metod))


# 4_6 статические методы
# Добавляем список пользователей для теста статического метода
users = (
    'Vasya',
    'Misha',
    'Oleg',
    'Dima',
)

# 4_6_1 Вызываем статический метод из класса и из экземпляра
print('From class Server:', Server.show_users())
# Вывод: From class Server: Список пользователей:('Vasya', 'Misha', 'Oleg', 'Dima')
print('From database server:', database_server.show_users())
# Вывод:
# From database server: Список пользователей:('Vasya', 'Misha', 'Oleg', 'Dima')




# 5_ Наследование 
"""Наследование - механизм ООП, который позволяет снизить сложность программы, уменьшая дублирование кода.

При наследовании классы разделяются на:
  - Базовый (SUPERclass, родительский, parent)
  - Дочерний (SUBclass, наследуемый, child)

В python это выглядит таким образом:
class Child(Parent):
    ...

Для того чтобы Child мог вызвать методы Parent, чаще всего это __init__, у питона есть оператор super()
  super() - позволяет обращаться к родителям вверх по иерархии наследования

Так же есть множественное наследование, довольно опасная вещь, нужно использовать с особой осторожностью.
Множественное наследование - когда один дочерний класс наследуется от нескольких родительских классов.
При множественном наследовании в Python срабатывает MRO (Method Resolution Order)
  Если вкратце, при наследовании от нескольких классов, приоритет переопределения поля или методов выше у того
  класса, который находится ЛЕВЕЕ в определении дочернего класса.
  Также у классов есть атрибут __mro__ - это кортеж, в нём упорядочено указываются ссылки на классы,
    которые учавствуют в поиске близжайшего поля и/или метода.
"""

print('\n\n5_  ********************')
# 5_1 Наследование без инициализации экземпляров
# 5_1_1 Создаем базовый класс
class BaseClass:
    some_attr = 'some_attribute'

    @classmethod
    def show_some_attr(cls):
        return cls.some_attr

# 5_1_2 Создаем наследника без функционала
class ChildClass(BaseClass):
    pass

# 5_1_3 Пробуем вызвать метод класса show_some_attr у наследника
print('ChildClass.show_some_attr():', ChildClass.show_some_attr())
# Вывод: ChildClass.show_some_attr(): some_attribute

# 5_1_4 Пробуем получить значение show_some_attr через наследника напрямую
print('ChildClass.some_attr:', ChildClass.some_attr)
# Вывод: ChildClass.some_attr: some_attribute

# 5_1_5 Выводим словарь имён класса ChildClass
print('ChildClass.__dict__:',ChildClass.__dict__)
# Вывод: ChildClass.__dict__: {'__module__': '__main__', '__doc__': None}

# Таким образом ChildClass получал атрибут и метод от класса BaseClass, а не копировал его в свой словарь.


# 5_2 Наследование и инициализация экземпляров. Оператор super
# https://realpython.com/python-super

# 5_2_1 Переопределяем базовый класс
class BaseClass:
    def __init__(self, base_attr, some_attr):
        print('BaseClass __init__ was started')
        self.base_attr = base_attr
        self.some_attr = 'some attr from BaseClass'
        print('BaseClass __init__ was complited')

    def say_hi(self):
        return 'hi from BaseClass'


# 5_2_2 Наследование от базового класса
# 5_2_2_1 Переопределяем класс наследника
class ChildClass(BaseClass):
    def __init__(self, base_attr, some_attr, child_attr):
        print('ChildClass __init__ was started')
        super().__init__(base_attr, some_attr)
        self.child_attr = child_attr
        self.some_attr = some_attr
        print('ChildClass __init__ was complited')

# 5_2_2_2 Создаем экзепляр наследника
CC_object = ChildClass('base attr from CC_object',
                       'some attr from CC_object',
                       'child attr from CC_object')
# Вывод:
# ChildClass __init__ was started
# BaseClass __init__ was started
# BaseClass __init__ was complited
# ChildClass __init__ was complited


# 5_2_2_3 Выводим словарь имён экземпляра наследника
print('CC_object.__dict__:', CC_object.__dict__)
# Вывод:
# CC_object.__dict__: {'base_attr': 'base attr from CC_object',
#                      'some_attr': 'some attr from CC_object',
#                      'child_attr': 'child attr from CC_object'}


# 5_2_3 Наследование от наследника
# 5_2_3_1 Создаем класс наследника от наследника
class SubChildClass(ChildClass):
    def __init__(self, base_attr, some_attr, child_attr, sub_child_attr):
        print('SubChildClass __init__ was started')
        super().__init__(base_attr, some_attr, child_attr)
        self.sub_child_attr = sub_child_attr
        print('SubChildClass __init__ was complited')

    def say_hi_from_super(self):
        return super().say_hi()


# 5_2_3_2 Создаем экзепляр
SCC_object = SubChildClass('base attr from SCC_object',
                           'some attr from SCC_object',
                           'child attr from SCC_object',
                           'sub_child attr from SCC_object')
# Вывод:
# SubChildClass __init__ was started
# ChildClass __init__ was started
# BaseClass __init__ was started
# BaseClass __init__ was complited
# ChildClass __init__ was complited
# SubChildClass __init__ was complited


# 5_2_3_3 Выводим словарь имён экземпляра наследника наследника
print('SCC_object.__dict__:', SCC_object.__dict__)
# Вывод:
# SCC_object.__dict__: {'base_attr': 'base attr from SCC_object',
#                       'some_attr': 'some attr from SCC_object',
#                       'child_attr': 'child attr from SCC_object',
#                       'sub_child_attr': 'sub_child attr from SCC_object'}


# 5_3 Наследник наследника пробует через оператор super вызвать метод BaseClass
print('SCC_object.say_hi_from_super():', SCC_object.say_hi_from_super())
# Вывод: SCC_object.say_hi_from_super(): hi from BaseClass


# 5_4 Множественное наследование. MRO (Method Resolution Order)
# 5_4_1 Пример для демонстрации. Как мне кажется в реальной разработке не надо так делать.
# Не нужно делать зависимость поведения объекта от порядка наследования

# 5_4_1_1 Объявляем FirstClass и SecondClass, указываем у каждого поле class_name
class FirstClass:
    class_name = 'First'


class SecondClass:
    class_name = 'Second'


# 5_4_1_2 Объявляем класс-наследник с порядком наследования: FirstClass, SecondClass
class FirstSecondClass(FirstClass, SecondClass):
    def show_some_attr(self):
        return super().class_name


# создаём экземпляр и выводим поле class_name, объявленное у класса-родителя
FirSec_obj = FirstSecondClass()
print('FirSec_obj.show_some_attr():', FirSec_obj.show_some_attr())
# Вывод: FirSec_obj.show_some_attr(): First

# 5_4_1_3 Объявляем еще один класс-наследник с порядком наследования: SecondClass, FirstClass
class SecondFirstClass(SecondClass, FirstClass):
    def show_some_attr(self):
        return super().class_name

# Также создаём экземпляр и выводим поле class_name
SecFir_obj = SecondFirstClass()
print('SecFir_obj.show_some_attr():', SecFir_obj.show_some_attr())
# Вывод: SecFir_obj.show_some_attr(): Second


# 5_4_1_4 Выводим порядок поиска (MRO) у экземпляров FirSec_obj и SecFir_obj
print('FirSec_obj.__class__.__mro__', FirSec_obj.__class__.__mro__)
# Вывод:
# FirSec_obj.__class__.__mro__ (<class '__main__.FirstSecondClass'>,
#                               <class '__main__.FirstClass'>,
#                               <class '__main__.SecondClass'>,
#                               <class 'object'>)

print('SecFir_obj.__class__.__mro__', SecFir_obj.__class__.__mro__)
# Вывод:
# SecFir_obj.__class__.__mro__ (<class '__main__.SecondFirstClass'>,
#                               <class '__main__.SecondClass'>,
#                               <class '__main__.FirstClass'>,
#                               <class 'object'>)

# 5_5 Выводы из блока 5_4 и краткая заметка об иерархии наследования в python
"""
При поиске поля и\или метода python начинает искать в самом экзмпляре,
  затем в классе экземпляра,
  после поднимаясь выше по иерархии, соблюдая MRO
  и наконец базовая сущность - object
"""


# 5_6 Миксины - расширяющий класс, для подмешивания функционала (mix in)
"""
Миксины используются в тех случаях, когда необходимо расширить функционал классов, 
  которые между собой не связаны наследованием.
Миксин только расширяет функционал, поэтому создавать экземпляры миксина нельзя.
"""

# 5_6_1 Описание примера
"""
К примеру программа работает только с живыми сущностями, например люди и животные.
И уточнять возраст и другие общие атрибуты нет необходимости. Значит нет нужды делать сложную
  иерархию наследования. Создаётся класс Person и Animal.
К какому-то моменту появляется потребность хранить и выводить любимое блюдо у класса Person и
  у класса Animal. Как это реализовать? Можно создать надкласс Being (сущность) тогда могут возникнуть
  side-эффекты. Потому как у класса Person и Animal могут быть схожие атрибуты и\или методы.
  Но это усложнит программу. Тут-то на помощь и приходит mixin.
"""

# 5_6_2 объявлем класс FoodMixin
class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError('Food does not set')
        else:
            return self.food


# 5_6_3 объявляем класс Person, Animal
# классы без функционала, просто для примера.
class Person:
    pass


class Animal:
    pass


# 5_6_4 Расширяем иерархию классов и объявлем классы Employee и Cat с использованием mixin класса
class Employee(FoodMixin, Person):
    def __init__(self, food):
        self.food = food


class Cat(FoodMixin, Animal):
    def __init__(self, food):
        self.food = food


# Создаем экземпляры классов Employee, Cat
bob = Employee('картоха')
snowball = Cat('мясо')

# 5_6_5 Вызываем метод get_food у экземпляров
print('bob.get_food():', bob.get_food())
print('snowball.get_food():', snowball.get_food())
# Вывод:
# bob.get_food(): картоха
# snowball.get_food(): мясо




# 6_ Полиморфизм
"""
Одна из самых запутанных и неоднозначных тем. Объяснение ниже касается только ЯП python.
Полиморфизм - один из принципов ООП. Но полиморфизм есть не только в ООП.

Дальше идут глубины глубин.
P.S. В Python используется ad-hoc полиморфизм. Но это не точно.
Полиморфизм означает интерфейсы, а не сигнатуры вызовов
Некоторые языки ООП определяют полиморфизм как подразумевающий перегрузку функций на основе
  сигнатур типов их аргументов — количестве и/или типах переданных аргументов. Ввиду отсутствия
  объявлений типов в Python такая концепция фактически неприменима; полиморфизм в Python
  базируется на интерфейсах объектов, а не на типах.

Поскольку атрибуты всегда распознаются во время выполнения, объекты, которые реализуют те же самые
  интерфейсы, автоматически становятся взаимозаменяемыми; клиенты не обязаны знать о том, какие
  виды объектов реализуют методы, вызываемые клиентами.

Этот момент когда текст перед кодом не объясняет, а наоборот запутывает.
Просто глянь пример
"""


print('\n\n6_  ********************')

# Источник: https://www.youtube.com/watch?v=aEOSBkzNImw
    
# 6_1 Задача: найти площадь прямоугольника, квадрата, круга

# 6_1_1 Объявляем класс Rectangle, Square, Circle.
# 6_1_2 В каждом классе определяем метод с именем get_area (получить площадь)
class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a 
        self.side_b = side_b 

    def get_area(self):
        return self.side_a * self.side_b


class Square:
    def __init__(self, side):
        self.side = side 

    # можно было возвести в квадрат (**2), но это дорогая операция
    def get_area(self):
        return self.side * self.side


class Circle:
    def __init__(self, radius):
        self.radius = radius 

    def get_area(self):
        return 3.14 * (self.radius * self.radius) 


# 6_1_3 создаем экземпляры и помещаем в список
rect = Rectangle(3, 16)
sq = Square(5)
cir = Circle(8)

figure_list = [
    rect,
    sq,
    cir,
]

# 6_1_4 Проходим циклом по списку фигур и вызываем у каждой метод get_area
for figure in figure_list:
    print(f'{figure} area is {figure.get_area()}')
# Вывод:
# <__main__.Rectangle object at 0x000001B260195730> area is 48
# <__main__.Square object at 0x000001B2601957C0> area is 25
# <__main__.Circle object at 0x000001B260195820> area is 200.96




# 7_ Модификаторы доступа полей и методов: публичный, защищенный, приватный
# https://pythoner.name/documentation/tutorial/classes 
"""В питоне всё печально с приватностью данных и с какими-либо ограничениями.
Всё держится на соглашениях, что если переменная начинается на такой символ, 
  то мы её не используем тут и тут. Но может это и к лучшему. Потому как при
  адекватной работе с кодом излишние ограничения не нужны. Потому что если
  ограничения есть, их рано или поздно приходится обходить эти ограничения с
  помощью костылей.

Итак. Видимости полей и методов:
- публичная (public) - все поля и методы по умолчанию публичные

- не публичная или защищённая (protected) - в питоне в начале имени ставится одиночное '_' подчеркивание,
    считается как не публичная часть API.
    Из документации python: a name prefixed with an underscore (e.g. _spam) should be treated as a
    non-public part of the API (whether it is a function, a method or a data member). It should be
    considered an implementation detail and subject to change without notice.
  
- приватная (private)
Поскольку есть действительные прецеденты для приватных членов класса (а именно, чтобы избежать конфликтов
  имен с именами, определенными подклассами), есть ограниченная поддержка такого механизма, называемого
  корректировкой имен (name mangling). Любой идентификатор вида __spam (по крайней мере с двумя первыми
  подчеркиваниями и не более чем одним завершающим) текстуально заменяются на _classname__spam, где
  classname - это текущее имя класса с начальным символом(ами) подчеркивания. Эта корректировка делается
  безотносительно к синтаксической позиции идентификатора до тех пор, пока это происходит в определении класса.

Корректировка имен полезна для того, чтобы позволить подклассам переопределять методы, не нарушая
  внутриклассовых вызовов методов.  


Какой бы ни была область видимости, к полю или методу можно обратиться.
Но в случае с _не-публичной или __приватной сущностью - это равносильно выстрелу себе в ногу.
Можно но не нужно.
"""
# TODO добавить ссылку на блок по теме наследования, чтобы показать примером как это работает


print('\n\n7_  ********************')
# 7_1 Объявляем класс и указываем публичное, не публичное и приватное поле экземпляра
class MyClass:
    def __init__(self, public_var, protected_var, private_var):
        self.public_var = public_var
        self._protected_var = protected_var
        self.__private_var = private_var

# 7_2 Создаем экземпляр и присваиваем значения полям
my_object = MyClass('public', 'protected', 'private')

# 7_3 Выводим значение публичного и не-публичного поля
print('my_object.public_var:',my_object.public_var)
print('my_object._protected_var:',my_object._protected_var)
# Вывод: 
# my_object.public_var: public
# my_object._protected_var: protected

# 7_4 Пытаемся вывести приватное поле
try:
    print('my_object.__private_var:', my_object.__private_var)
except Exception as e:
    print(type(e).__name__, e)
# Вывод: 
# AttributeError 'MyClass' object has no attribute '__private_var'

# 7_5 Выводим словарь экземпляра
print('my_object.__dict__:', my_object.__dict__)
# Вывод:
# my_object.__dict__: { 'public_var': 'public',
#                       '_protected_var': 'protected',
#                       '_MyClass__private_var': 'private'}

# TODO Инкапсуляция

# 8_ Инкапсуляция
""" Один из принципов ООП. Но также как и полиморфизм, инкапсуляция встречается не только в ООП.
Инкапсуляцию я бы описал следующей фразой - взаимодействуй только с интерфейсом, без доступа к реализации.
Простейший пример инкапсуляции вне ООП - функция.
Интерфейс функции:
 - её имя, для вызова функции
 - принимаемые функцией аргументы

Есть функция restart()
Она может принимать аргументы, или же касаться какой то конкретной сущности в рамках контекста программы.
Но нам неизвестно, каким именно образом происходит перезагрузка, что и в каком порядке перезагружается.
Этот процесс, в котором опускаются детали реализации, можно назвать инкапсуляцией.

Что на этот счет говорит Википедия:
Инкапсуляция (англ. encapsulation, от лат. in capsula) — в информатике размещение в одном компоненте
  данных и методов, которые с ними работают. Также может означать скрытие внутренней реализации от
  других компонентов. Например, доступ к скрытой переменной может предоставляться не напрямую, а с
  помощью методов для чтения (геттер) и изменения (сеттер) её значения.
В ООП инкапсуляция тесно связана с принципом абстракции данных (не путать с абстрактными типами
  данных, реализации которых предоставляют возможность инкапсуляции, но имеют иную природу).
Это, в частности, влечёт за собой различия в терминологии в разных источниках. В сообществе C++ или
  Java принято рассматривать инкапсуляцию без сокрытия как неполноценную. Однако, некоторые языки
  (например, Smalltalk, Python) реализуют инкапсуляцию, но не предусматривают возможности сокрытия в принципе.

Как-то так. Получается инкапсуляция это не сокрытие, ExtremeCode может спать по ночам спокойно :D

Что по поводу инкапсуляции в Python пишет М. Лутц:
Инкапсуляция — помещение операционной логики в оболочку интерфейсов, чтобы код каждой операции
  был написан только один раз в программе. Тогда если в будущем возникнет необходимость в
  изменении, то изменять нужно будет только одну копию. Более того, мы можем практически произвольно
  изменять внутренности одиночной копии, не нарушая работу кода, который ее потребляет.
Инкапсуляция
Методы и операции реализуют поведение, хотя сокрытие данных по умолчанию является соглашением.
Инкапсуляция
Помещение деталей реализации позади объектных интерфейсов изолирует пользователей класса от изменений в коде.

Какого-то илюстрирующего примера я не придумал. Думаю описания инкапсуляции достаточно.
"""

# 8_1 Свойства (property)
"""свойства - атрибуты классов и объектов.
Забегая вперед от себя хочу добавить что как минимум один из способов определения
  свойств просто уебанский (уж простите за французский)
Первый вариант: объявить имя свойства и присвоить ему экземпляр класса property,
  указав аргументы:
  fget - функция-getter атрибута
  fset - ф-ия-setter
  fdel - ф-ия удаления
  fdoc - строка документации свойства

любой аргумент по умолчанию None, так что если нужно свойство только для чтения,
  то аргумент fset не нужно указывать

Второй вариант: Использование декоратора @property
Именно второй вариант мне не нравится.
В декоратор оборачивается функция, имя которой должно быть такое же как ПОЛЕ.
То есть функция, которая подразумевает действие, в имени которой вместо глагола - СУЩЕСТВИТЕЛЬНОЕ?!
Вот тут шаблон порвало напрочь. Дальше попросту не хочу это описывать. Пример наглядно покажет.
"""

# 8_1_1 Объявляем класс Account
class Account:
	__id = 0

	def __init__(self, owner_name, owner_id, amount):
		self.id = Account.get_new_id()
		self.owner_name = owner_name
		self.__owner_id = owner_id
		self.__amount = amount

	@classmethod
	def get_new_id(cls):
		new_id = cls.__id
		cls.__id += 1 
		return new_id

	# 8_1_1_1 Первый вариант использования свойств
	def get_amount(self):
		# при каждом обращении к свойству будет вызываться этот метод,
		#  в котором можно сделать форматирование перед выводом.
		# Возможно еще добавить проверку на то, кто именно запрашивает
		#   данные, но думаю что это делается как-то по другому.
		print(f'get_amount is called by {self.owner_name}')
		return self.__amount

	def set_amount(self, amount):
		# при каждом присвоении значения свойства будет вызываться этот метод.
		# Здесь можно будет сделать валидацию значений перед записью
		print(f'set_amount is called by {self.owner_name}')
		self.__amount = amount
		
	amount = property(fget=get_amount, fset=set_amount)

	# 8_1_1_2 Второй вариант использования свойств (буэээээ)
	@property
	def owner_id(self):
		print(f'get owner_id is called by {self.owner_name}')
		return self.__owner_id

	@owner_id.setter
	def owner_id(self, value):
		print(f'set owner_id is called by {self.owner_name}')
		self.__owner_id = value

# 8_1_2 Создаем экземпляры и тестируем работу свойств
a1 = Account('Ivan', 740529556101, 15000)
a2 = Account('Dima', 850608779652, 9800)

# 8_1_2_1 Выводим значения полей и атрибутов экземпляров
for acc in (a1, a2):
	print('acc.owner_name', acc.owner_name)
	print('acc.id', acc.id)
	print('acc.owner_id',acc.owner_id)
	print('acc.amount', acc.amount)
# Вывод
# acc.owner_name Ivan
# acc.id 0
# get_amount is called by Ivan
# acc.amount 15000
# acc.owner_name Dima
# acc.id 1
# get_amount is called by Dima
# acc.amount 9800

print()

# 8_1_2_2 Изменяем значения атрибутов
a1.amount = 6000
a2.amount = 49000
# Вывод:
# set_amount is called by Ivan
# set_amount is called by Dima
print()

# 8_1_2_3 Снова выводим значения полей и атрибутов
for acc in (a1, a2):
	print('acc.owner_name', acc.owner_name)
	print('acc.id', acc.id)
	print('acc.amount', acc.amount)
# Вывод:
# acc.owner_name Ivan
# acc.id 0
# get_amount is called by Ivan
# acc.amount 6000
# acc.owner_name Dima
# acc.id 1
# get_amount is called by Dima
# acc.amount 49000


# TODO Когда созрею, доделать блок
# 8_2 дескрипторы(блок не готов. Оставил на потом)
"""
Дескрипторы - специальный класс, который содержит в себе методы операций извлечения,
  установки и удаления конкретного атрибута.
Свойства (property) по сути являются упрощенными дескрипторами 

Однако, у дескриптора есть преимущество: Если у экземпляра есть несколько полей,
  которые имеют схожее поведение, например имя и фамилия у класса Person, то нет
  нужды делать Property на каждый из них.
"""
# сделать принты при вызове поля, которое является экземпляром дескриптора, через
#  экземпляр класса и через сам класс


class StringDescriptor:
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name
    
    def __get__(self, instance, owner_class):
        print('__get__ from StringDescriptor instance was called')
        print(f'self:', self)
        print(f'instance:',instance)
        print(f'owner_class:',owner_class)
        return instance.__dict__.get(self.property_name, None)
    
    def __set__(self, instance, value):
        print('__set__ from StringDescriptor instance was called')
        print(f'self:', self)
        print(f'instance:',instance)
        instance.__dict__[self.property_name] = value


class Person:
    country = StringDescriptor()
    def __init__(self, name, surname):
        self.name = StringDescriptor()
        self.surname = StringDescriptor()
    # кажется не так всё работает

petr = Person('Petr', 'Crouch')
Person.country = 'England'
# Вывод: А вывода нет. Как это работает? Непонятно. Отложу тему дескрипторов,
#  я пока до них не дорос.




# 8_3 __getattr__, __setattr__, __getattribute__(тоже отмена, сложная тема. 
#   Вообще я понял что не по питоновски делать хоть какое то ограничение. Очень странно)