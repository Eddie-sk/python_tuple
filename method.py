# -- coding: utf-8 --
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

