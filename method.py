# -- coding: utf-8 --
import math
def cus_abs(x):
    if x >= 0:
        return x
    else:
        return -x

a = cus_abs(-10)
b = cus_abs(15.5)
c = cus_abs(12)

print a, b, c

#空函数，如果想定义一个什么都不做的函数，或者还没想好方法实现，可以在方法体重输入占位符：pass

def test():
    pass

#参数检查
#1、参数个数不对：Python解释器会自动检测，并抛出TypeError异常
#2、参数类型不对：Python解释器无法检测，需使用内置函数isinstance()自行检查

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# e = my_abs('123')
# f = my_abs(1, 3, 4)
g = my_abs(-3)
print g

#返回多个值
#angle=0,默认值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 200, 2)

print x, y


def quadratic(a, b, c):
    x1 = 0.0
    x2 = 0.0
    descriminant = b * b - 4 * a * c
    if descriminant == 0:
        x1 = x2 = -b / (2 * a)
    else:#两个不同的实数根
        x1 = (-b + math.sqrt(descriminant)) / (2 * a)
        x2 = (-b - math.sqrt(descriminant)) / (2 * a)
    return x1, x2
print('quadratic(2, 3, 1) = ',quadratic(2, 3, 1))
print(quadratic(1, 3, -4))


def power(z, n):

    #类型判断，非int类型报类型异常
    if not isinstance(n, int):
        raise TypeError('param n must be int')
    s = 1
    f = abs(n)
    while f > 0:
        f = f - 1
        s = s * z
    if n < 0:
        return float(1.0 / s)
    return s
# print ('power(12, 10) = ', power(12, 10))
# print ('power(12, -0.2) = ', power(12, -0.2))

def enroll(name, gender, age = 10, city = 'Shanghai'):
    print('name: ', name)
    print('gender: ', 'boy' if gender == 1 else 'girl')
    print('age: ', age)
    print 'city', city

enroll('あい', 1, 23)
enroll(gender=0, name='あいぃ')

def addEnd(L=[]):
    L.append('End')#如果使用默认参数，默认参数L指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用是会后呢，默认参数的内容就变了
    return L

ar = addEnd(['123','3455'])

print(ar)
print(addEnd())
print(addEnd())
print(addEnd())

def fixAddEndBug(L = None):
    if L is None:
        L = []
    L.append('End')
    return L

print(fixAddEndBug(['123']))

print(fixAddEndBug(['123']))

#可变参数
def cal(numbers):
    sum = 0
    for number in numbers:
        sum += number * number
    print(sum)
    return sum

#调用的时候需要组装成list或元组tuple
cal([1, 2, 3])
cal((2, 3, 4))
#可变参数可以简化调用方式：cal(2, 3, 5)

def calmult(*numbers):
    num = 0
    for n in numbers:
        if not isinstance(n,(int, float))
            raise  TypeError('number mast be init or float')
        num += n * n
    print num
    return num

calmult(1, 2, 3)
calmult(2, 3, 4)

#如果有一个list或者元组
numbers = [1, 2, 3, 4]
numberTuple = (1, 2, 3, 4, 5)
calmult(*numbers)
calmult(*numberTuple)


#关键字参数
##可变参数允许传入任意个参数，


