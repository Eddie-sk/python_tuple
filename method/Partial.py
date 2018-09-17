# -- coding: utf-8 --

#在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下

#int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
#但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：

print int('10001', base=16)

#假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：

def int2(x, b):
    if not isinstance(b, int):
        raise TypeError('base must be int')

    return int(x, base = b)

print int2('1001', 2)

from functools import partial

int2 = partial(int, base=2)

print int2('100')

def add(x, y):
    return x + y

add2 = partial(add, 10)

print add2(13)
