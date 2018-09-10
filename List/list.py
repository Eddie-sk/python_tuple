# --coding : utf-8 --

arr1 = [1, '23', 'Hello']
arr1.append(123)
arr1.extend([4, 5, 6])
print arr1
arr1.pop()#删除列表中给定位置的项目，然后将其返回。如果未指定索引，则删除列表中的最后一项

arr1.count('23')#返回列表中'23'出现的次数