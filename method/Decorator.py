# -- coding: utf-8 --


#想在调用函数前后自动打印日志，而又不希望修改函数定义，这种在代码运行期间动态增加功能的方式，称为：装饰器（"decorator"）

def log(func):
    def wrapper(*args, **kv):
        print 'call {0}()'.format(func.__name__)
        return func(*args, **kv)
    return wrapper

def now():
    print '2018-9-14'

now()

#因为log函数是一个装饰器，所以支持传入一个函数，并返回一个函数。我们可以使用python的@语法，把decorator置于函数的定义处

@log
def nowDate():
    print '10:30'

nowDate()

#>>call nowDate()
#>>10:30

#把@log放到函数nowDate定义处，相当于执行语句：nowDate = log(nowDate)

#由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
#wrapper函数的参数定义是(*args, **kv)，因此，可以接受任意参数的调用。在wrapper函数内，首先打印日志，紧接着调用原始函数

#如果decorator本身需要传入参数，就需要编写一个返回decorator的高阶函数

def log(text):
    def decorator(func):
        def wrapper(*args, **kv):
            print '{0} call {1}'.format(text, func.__name__)
            return func(*args, **kv)
        return wrapper
    return decorator

@log('execute')
def now():
    print '10:55'

now()


#函数也是对象，也有__name__属性，但看被decorator装饰后的函数的名字，发现name是装饰函数的name，"wrapper"

#可以使用functools解决

import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kv):
            print '{0} call {1}():'.format(text, func.__name__)
            return func(*args, **kv)
        return wrapper
    return decorator

@log('execure')

def now():
    print '2018-09-14 11:28'


now()
print now.__name__

print max((10, 123, 44))



