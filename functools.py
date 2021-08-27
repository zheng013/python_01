def bubble_sort(lst):
    for j in range(len(lst) - 1, 0, -1):
      for i in range(j):
            if lst[i] > lst[i + 1]:
                # temp = lst[i]
                # lst[i] = lst[i + 1]
                # lst[i + 1] = temp
                (lst[i],lst[i+1])=(lst[i+1],lst[i])  #利用元组的解构规则进行替换
    return  lst

'''
利用双层循环时间上换取空间大小 冒泡排序
'''

'''
递归和归并排序的重点在于当list只有一个时直接返回当前list，否则则继续拆分合并。
'''

def merge(left,right):
    result=[]
    while(len(left)>0 and len(right)>0):
      if left[0]<=right[0]:
          result.append(left.pop(0))
      else:
          result.append(right.pop(0))

    while(len(left)):
          result.append(left.pop(0))
    while(len(right)):
          result.append(right.pop(0))
    return result


def merge_sort(lst):
  if(len(lst)<2):
      return lst
  middle=int(len(lst)/2)
  left=lst[0:middle]
  right=lst[middle:]

  return merge(merge_sort(left),merge_sort(right))
print('2'*30)
print(bubble_sort([23,12,3,4,1,2,2321,4,2]))
print(merge_sort([23,12,3,4,1,2]))


def difference(a,b):
    return [item  for item in a if item not in b]


print(difference([23,12,3,4,1,222,77],[23,12,3,4,1,222,2]))

#列表推导

x=[m**2 if m>10 else m**4 for m in range(50)]

print(x)

multistr="select * from multi_row \
  where row_id<5"
#多行字符串连接符

print(multistr)

multistr=("select * from multi_row:="
"where row_id<5"
 "order by age")


1
# python -m http.server  python 允许开启一个http服务器从根目录共享文件

test=[1,2,5,6,8,8,55]

print(dir(test)) #检查python中的对象

# use following way to verify multi values
m=0
if m in [1, 2, 3, 4]:
  pass
# do not use following way
if m==1 or m==2 or m==3 or m==4:
  pass


# 运行时检测python版本 动态检测当前python软件版本

import sys
if not hasattr(sys, "hexversion") or sys.version_info != (2, 7):
    print("sorry, you are not running on python 2.7")
    print("current python version:", sys.version)

# 指定符号对于多个字符串进行组合
test=['I','Like','Javascript']
print("2".join(test))

# 用枚举在循环中找到索引
test = [10, 20, 30]
for i, value in enumerate(test):
    print(i, ':', value)
#定义枚举量

class shapes:
    circle, square, triangle, quadrangle = range(4)
print(shapes.circle)
print(shapes.square)
print(shapes.triangle)
print(shapes.quadrangle)


# 从方法中返回多个值

def x():
    return 1, 2, 3, 4
a, b, c, d = x()
print(a, b, c, d)

# 找到列表中出现次数最多的数

test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4, 4]
print(max(set(test), key=test.count))

stdcal={
  "sum":lambda x,y:x+y,
  "subtract":lambda x,y:x-y
}

# 搜索字符串的多个前后缀
''.endswith(('xxx','xxx'))
''.startswith(('sss','xxx'))