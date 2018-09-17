# -- coding: utf-8 --

#列表推导

squares = []

for x in range(10):
    square = x ** 2
    print x, '** 2 =', square #x ** n 表示x的n次方
    squares.append(square)

print squares

#可以得到相同结构
sq = [x ** 2 for x in range(10)]
print sq

sqForMap = map(lambda x: x ** 2, range(5))

print sqForMap

print [(x, y) for x in [1, 3, 5] for y in (1, 7, 5, 8) if x != y]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print [weapon.strip() for weapon in freshfruit]#去除头尾空格.strip()

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [num for elem in vec for num in elem]

from math import pi

print [round(pi, i) for i in range(3, 10)]


#嵌套列表

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8, 9],
          [10, 11, 12, 13]]  # type: List[List[int]]
print [row[i] for row in matrix for i in range(len(row))]

#删除列表切片数据，或删除真个列表数据



# del matrix[0:2]
# print matrix

del matrix[:]
print matrix

#也可以用来删除整个变量，执行删除变量之后再引用变量名称，会报编译错误

del matrix
print matrix

