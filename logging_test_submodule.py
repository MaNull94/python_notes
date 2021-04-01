"""Подмодуль файла logging_notes.py для тестирования логгирования"""
from logging import getLogger


logger = getLogger(__name__)

def say_hi():
    logger.info('Hi from logging_test_submodule')