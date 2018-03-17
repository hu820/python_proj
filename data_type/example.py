# coding=utf-8
##数值
x = 3
print(type(x))  # Prints "<class 'int'>"
print(x)  # Prints "3"
print(x + 1)  # Addition; prints "4"
print(x - 1)  # Subtraction; prints "2"
print(x * 2)  # Multiplication; prints "6"
print(x ** 2)  # Exponentiation; prints "9"
x += 1
print(x)  # Prints "4"
x *= 2
print(x)  # Prints "8"
y = 2.5
print(type(y))  # Prints "<class 'float'>"
print(y, y + 1, y * 2, y ** 2)  # Prints "2.5 3.5 5.0 6.25"

##字符串
hello = 'hello'
world = 'world'
print(hello)
print(hello + world)
print(len(hello + world))
hw = hello + ' ' + world
print(hw)
print(len(hw))
hw2 = '%s %s %d' % (hw, hello, 12)
print(hw2)

s = 'hello xi dada'
print(s.capitalize())
print(s.upper())

# replace
s = 'hello python'
s = s.replace('python', 'world')
print(s)

d = {'person': 2, 'cat': 4}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))


##list
# list []
xs = [3, 1, 2]  # Create a list
print(xs, xs[2])  # Prints "[3, 1, 2] 2"
print(xs[-1])  # Negative indices count from the end of the list; prints "2"
xs[2] = 'foo'  # Lists can contain elements of different types
print(xs)  # Prints "[3, 1, 'foo']"
xs.append('bar')  # Add a new element to the end of the list
print(xs)  # Prints "[3, 1, 'foo', 'bar']"
x = xs.pop()  # Remove and return the last element of the list
print(x, xs)  # Prints "bar [3, 1, 'foo']"

nums = list(range(5))  # range is a built-in function that creates a list of integers
print(nums)  # Prints "[0, 1, 2, 3, 4]"
print(nums[2:4])  # Get a slice from index 2 to 4 (exclusive); prints "[2, 3]"
print(nums[2:])  # Get a slice from index 2 to the end; prints "[2, 3, 4]"
print(nums[:2])  # Get a slice from the start to index 2 (exclusive); prints "[0, 1]"
print(nums[:])  # Get a slice of the whole list; prints "[0, 1, 2, 3, 4]"
print(nums[:-1])  # Slice indices can be negative; prints "[0, 1, 2, 3]"
nums[2:4] = list(range(9, 18, 1))  # Assign a new sublist to a slice
print(nums)

for data in nums:
    print(data)
for idx, data in enumerate(nums):
    print('%d:%d' % (idx, data))

# 带条件初始化
seq = [x * 5 for x in nums if x % 2 == 0]
print(seq)


##字典
# A dictionary stores (key, value) pairs,
# similar to a Map in Java or an object in Javascript
nums = {'cat': 2, 'person': 2, 'pig': 4}
print(nums['pig'])
print('cat' in nums)
print('cat' not in nums)
nums['fish'] = 0
print(nums)
print(nums.get('pig'))
del nums['fish']
print(nums)
print(nums.get('fish', 'NA'))
for key, value in nums.items():
    print('%s:%d' % (key, value))


#集合（set）：不重复数据的集合
data = {'cat','dog','tiger'}
print('cat' in data)
data.add('fish')
print(data)
print(len(data))
data.add('cat')
print(data)
data.remove('cat')
print(data)

#loop
for animal in data:
    print(animal)
for idx,animal in enumerate(data):
    print("#%d:%s" % (idx,animal))
set_data = {x**2 for x in range(20)}
print(set_data)

#tuple
#A tuple is an (immutable) ordered list of values.
# A tuple is in many ways similar to a list;
# one of the most important differences is that tuples can be used as keys in dictionaries
# and as elements of sets, while lists cannot.

d={(x,x*2):x for x in range(10)}
print(d)
print(type(d))
t=(1,2)
print(type(t))
print(d[t])




