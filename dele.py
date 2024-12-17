from logging import exception
from os import write
import sys

def del_all(list):
    list.clear()

def del_task(list):
    x = int(input("номер задачи: "))
    try:
        list.pop(x)
    except Exception as e:
        print("== задачи под таким номером нет ==", file = sys.stderr)

