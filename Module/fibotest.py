# -- coding: utf-8 --
#import fibo


# fibo.fib(10)
# result = fibo.fib2(20)
#
# print 'result1', result


#如果您打算经常使用某个函数，可以将其分配给本地名称：

# fib = fibo.fib

# fib(13)

#模块可以包含可执行语句以及函数定义，这些语句用于初始化模块。仅在第一次出现在import语句时执行。如果文件作为脚本执行，他们也会运行
#每个模块都有自己的私有符号表，该表用作模块中定义的所有函数的全局符号表。因此，模块的作者可以在模块中使用全局变量，
# 而不必担心与用户的全局变量的意外冲突。另一方面，如果您知道自己在做什么，则可以使用与其函数相同的符号来触摸模块的全局变量modname.itemname。

#一个模块可以导入其他模块，习惯但不要求将所有import语句放在模块开头。导入的模块名称放在导入模块的全局符号表中。

#from fibo import fib,fib2 #不会引入从本地符号表中获取导入的模块名称，因为没有导入fibo模块，也就没有定义fibo模块

#它的变体
#from fibo import *  #这将导入除以下划线开头的所有名称，注：不欢迎的做法

# import fibo as fib #导入模块名后跟as，则以下名称as将直接绑定到导入的模块
# print fib.__name__
# fib.fib(100)

# from fibo import fib2 as fibonacci
# print fibonacci(100)

#print fibo   没有导入fibo模块，so，调用fibo不可行

#作为脚本运行
#运行python模块

import sys, fibo
fibo.fib(10)
#python fibotest.py <arguments> #将执行fibotest模块中的代码，但需要将模块的名称__name__设置为"__main__"，只有将模块作为主程序才会执行

#内置函数dir()用于找出模块定义的名称。它返回一个排序的字符串列表：
print dir(fibo)

#没有参数，dir()列出您当前定义的名称：请注意，它列出了所有类型的名称：变量，模块，函数等。
fib = fibo.fib
print dir()

#dir()不列出内置函数和变量的名称。如果您需要这些列表，则在标准模块中定义它们 __builtin__：
import __builtin__

print dir(__builtin__)

if __name__ == "__main__":
    import sys
    fibo.fib(int(sys.argv[1]))

