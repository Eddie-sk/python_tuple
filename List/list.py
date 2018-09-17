# -- coding: utf-8 --


class person(object):

    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None



arr1 = [1, 23]
arr1.append(123)
arr1.extend([4, 5, 6])
arr1.insert(0, 15)
print arr1
arr1.pop()  # 删除列表中给定位置的项目，然后将其返回。如果未指定索引，则删除列表中的最后一项

arr1.count(23)  # 返回列表中'23'出现的次数

arr1.sort(cmp=lambda x, y: cmp(y, x), reverse=1)
print arr1

t = person()
t.name = '张三'
t.age = 10
t.gender = '男'

t2 = person()
t2.name = '李四'
t2.age = 15
t2.gender = '女'

arr2 = [t, t2]

arr2.sort(cmp=lambda x, y: cmp(x.age, y.age), reverse=False)
print arr2


from collections import deque

#其中添加的第一个元素是检索的第一个元素（“先进先出”）; 但是，列表不能用于此目的。虽然列表末尾的追加和弹出很快，
# 但是从列表的开头进行插入或弹出是很慢的（因为所有其他元素都必须移动一个）。
queue = deque(['Eric', 'John', 'Michael'])
queue.append('Terry')
queue.appendleft('Graham')

print queue

queue.pop()
print queue

queue.popleft()
print queue

#功能编程工具

#filter (function, sequence)返回一个序列，该序列由序列中function(item)为true 的那些项组成。
# 如果sequence是a str，unicode或者tuple，结果将是相同的类型; 否则，它总是一个list。
# 例如，要计算可被3或5整除的数字序列：

def f(x): return x % 3 == 0 or x % 5 == 0

fil = filter(f, range(1, 20))
print fil

#map(function, sequence)调用function(item)每个序列的项目并返回返回值列表。例如，要计算一些立方体：
def cube(x):
    print x
    return x * x * x

#cu =  map(cube, range(1, 12))
cu = map(cube, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print 'cu', cu

seq = range(10)
seq1 = range(10, 20)

def add(x, y):
    print x, y
    return x + y

# ad =  map(add, seq, seq1)
# print ad
#reduce(function, sequence)返回通过在序列的前两项上调用二元函数函数构造的单个值，然后在结果和下一项上调用，依此类推。reduce:归纳为
reduceResult = reduce(add, range(1, 13))
print reduceResult
print '-------------------'

#reduce 可以传递第三个参数来指示起始值。在这种情况下，返回空序列的起始值，该函数首先应用于起始值和第一个序列项，然后应用于结果和下一个项，依此类推。例如，
def sum1(seq12):
    def add1(x, y):
        print x, y
        return x + y
    return reduce(add1, seq12, 9)#其中9为起始值

sumTest1 = sum1((1, 3, 4))
print 'sum1', sumTest1
