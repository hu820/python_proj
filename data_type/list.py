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
