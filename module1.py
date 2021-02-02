from module2 import *


def add():
    print('this is add')
    print(__name__)


def sub():
    print('this is sub')


def addsubb():
    add()
    sub()


if __name__=='__main__':
    addsubb()