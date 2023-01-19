#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from papka import help, add, list, select

if __name__ == '__main__':
    # Список людей.
    peoples = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ", ).lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            add.add()

        elif command == 'list':
            list.list()

        elif command.startswith('select '):
            select.select()

        elif command == 'help':
            help.help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
