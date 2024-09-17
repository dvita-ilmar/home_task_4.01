'''
Дегтярев Виталий (группа 22/08)
Домашнее задание №4.1
Модуль функции истинного деления
'''


from math import inf


def divide(first, second):
    if second == 0:
        return inf
    else:
        return first/second