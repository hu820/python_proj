#set is an unordered collection of distinct element
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