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
