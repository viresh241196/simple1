from module1 import *
def mul():
    print('this is mul')
    add()



def div():
    print('this is div')


def adivmul():
    div()
    mul()


if __name__=='__main__':
    adivmul()